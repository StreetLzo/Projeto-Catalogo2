// static/js/main.js

document.addEventListener("DOMContentLoaded", () => {
  // Efeito nos botões
  const buttons = document.querySelectorAll(".btn");
  buttons.forEach(btn => {
    btn.addEventListener("mousedown", () => {
      btn.style.transform = "scale(0.97)";
    });
    btn.addEventListener("mouseup", () => {
      btn.style.transform = "scale(1)";
    });
  });

  // Animação leve nos cards ao rolar
  const cards = document.querySelectorAll(".card");
  const revealCards = () => {
    cards.forEach(card => {
      const rect = card.getBoundingClientRect();
      if (rect.top < window.innerHeight - 100) {
        card.style.opacity = 1;
        card.style.transform = "translateY(0)";
      }
    });
  };
  cards.forEach(card => {
    card.style.opacity = 0;
    card.style.transform = "translateY(20px)";
    card.style.transition = "all 0.5s ease-out";
  });
  window.addEventListener("scroll", revealCards);
  revealCards();
});

// Adiciona sombra na navbar quando rola a página
window.addEventListener("scroll", () => {
  const nav = document.querySelector(".navbar");
  if (window.scrollY > 20) nav.classList.add("shadow");
  else nav.classList.remove("shadow");
});

// Pré-visualização em tempo real de novo projeto
document.addEventListener("DOMContentLoaded", () => {
  const titulo = document.getElementById("titulo");
  const descricao = document.getElementById("descricao");
  const autores = document.getElementById("autores");

  const prevTitulo = document.getElementById("prevTitulo");
  const prevDescricao = document.getElementById("prevDescricao");
  const prevAutores = document.getElementById("prevAutores");

  if (titulo && descricao && autores) {
    const atualizarPreview = () => {
      prevTitulo.textContent = titulo.value || "Título do Projeto";
      prevDescricao.textContent = descricao.value || "A descrição aparecerá aqui...";
      prevAutores.textContent = autores.value
        ? `Autores: ${autores.value}`
        : "Autores...";
    };
    titulo.addEventListener("input", atualizarPreview);
    descricao.addEventListener("input", atualizarPreview);
    autores.addEventListener("input", atualizarPreview);
  }
});

