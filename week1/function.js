const burger = document.querySelector(".burger");
const popup = document.querySelector(".popup-menu");
const closeBtn = document.querySelector(".popup-close");

burger.addEventListener("click", () => {
    popup.classList.add("open");
    });

closeBtn.addEventListener("click", () => {
    popup.classList.remove("open");
    });