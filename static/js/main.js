// static/js/main.js
// Comportamentos JS para o layout inspirado no PDF:
// - preview de avatar / imagem do projeto
// - fake file input (Clique para adicionar imagem)
// - mostrar nome do arquivo selecionado
// - favoritos (toggle visual + submit de form ou fetch POST se data-url presente)
// - proteção silenciosa caso elementos não existam

document.addEventListener('DOMContentLoaded', () => {
    console.log('main.js (PDF-style) carregado');
  
    // --------------------------
    // File inputs: fake + preview
    // HTML esperado:
    // <div class="file-input">
    //   <div class="fake">Clique para adicionar imagem</div>
    //   <input type="file" name="file" accept="image/*">
    //   <div class="file-name">Nenhum arquivo selecionado</div>
    // </div>
    // Para avatar:
    // <div class="avatar-preview"><img src="..." /></div>
    // <input id="profile_photo" type="file" ...>
    // --------------------------
    function initFileInputs() {
      document.querySelectorAll('.file-input').forEach(wrapper => {
        const fake = wrapper.querySelector('.fake');
        const real = wrapper.querySelector('input[type="file"]');
        const nameEl = wrapper.querySelector('.file-name');
  
        if (!real || !fake) return;
  
        // clique na área fake abre o file chooser
        fake.addEventListener('click', () => real.click());
  
        // quando um arquivo é selecionado
        real.addEventListener('change', (e) => {
          const f = e.target.files && e.target.files[0];
          if (f) {
            nameEl.textContent = f.name;
            // se for imagem, mostrar preview se houver .img-preview no wrapper
            const preview = wrapper.querySelector('.img-preview');
            if (preview && f.type.startsWith('image/')) {
              const reader = new FileReader();
              reader.onload = (ev) => {
                // cria image ou substitui
                let img = preview.querySelector('img');
                if (!img) {
                  img = document.createElement('img');
                  preview.appendChild(img);
                }
                img.src = ev.target.result;
                img.style.width = '100%';
                img.style.height = '100%';
                img.style.objectFit = 'cover';
              };
              reader.readAsDataURL(f);
            }
          } else {
            nameEl.textContent = 'Nenhum arquivo selecionado';
          }
        });
      });
    }
  
    // Avatar preview (input com id profile_photo e container .avatar-preview img)
    function initAvatarInput() {
      const input = document.querySelector('#profile_photo');
      const previewWrap = document.querySelector('.avatar-preview');
      if (!input || !previewWrap) return;
      const img = previewWrap.querySelector('img') || document.createElement('img');
      img.style.width = '100%';
      img.style.height = '100%';
      img.style.objectFit = 'cover';
      previewWrap.appendChild(img);
  
      input.addEventListener('change', (e) => {
        const f = e.target.files && e.target.files[0];
        if (!f) return;
        if (!f.type.startsWith('image/')) return;
        const reader = new FileReader();
        reader.onload = (ev) => {
          img.src = ev.target.result;
        };
        reader.readAsDataURL(f);
      });
    }
  
    // --------------------------
    // Favoritar: botão .btn-fav
    // - Se botão estiver dentro de um form (.fav-form) -> submete o form
    // - Se botão tiver data-url -> faz fetch POST para esse url e atualiza visual
    // - Se nada -> apenas toggle visual
    // --------------------------
    async function initFavButtons() {
      document.querySelectorAll('.btn-fav').forEach(btn => {
        btn.addEventListener('click', async (e) => {
          e.preventDefault();
          if (btn.classList.contains('favorited')) {
            btn.classList.remove('favorited');
          } else {
            btn.classList.add('favorited');
          }
  
          // se estiver dentro de um form com .fav-form → submete (fallback para csrf)
          let form = btn.closest('.fav-form');
          if (form) {
            try { form.submit(); } catch (err) { console.warn('Não foi possível submeter o form de favorito.', err); }
            return;
          }
  
          // se data-url disponível → fetch POST (assume CSRF token via meta[name="csrf-token"])
          const url = btn.getAttribute('data-url');
          if (url) {
            try {
              // tenta pegar token
              const tokenMeta = document.querySelector('meta[name="csrf-token"]');
              const headers = { 'Accept': 'application/json' };
              if (tokenMeta) headers['X-CSRFToken'] = tokenMeta.getAttribute('content');
  
              const res = await fetch(url, { method: 'POST', credentials: 'same-origin', headers });
              if (!res.ok) {
                console.warn('Erro ao favoritar (status ' + res.status + ')');
              }
            } catch (err) {
              console.warn('Erro fetch favorito:', err);
            }
          }
        });
      });
    }
  
    // --------------------------
    // Confirm delete for forms with .confirm-delete
    // --------------------------
    function initDeleteConfirm() {
      document.querySelectorAll('form.confirm-delete').forEach(f => {
        f.addEventListener('submit', (e) => {
          if (!confirm('Deseja excluir este projeto?')) e.preventDefault();
        });
      });
    }
  
    // small: toggle for mobile menu if present
    function initMisc() {
      const toggle = document.querySelector('.toggle-theme');
      if (toggle) {
        toggle.addEventListener('click', () => document.body.classList.toggle('theme-alt'));
      }
    }
  
    // RUN
    initFileInputs();
    initAvatarInput();
    initFavButtons();
    initDeleteConfirm();
    initMisc();
  });
  