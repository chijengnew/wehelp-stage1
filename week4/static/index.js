const form = document.getElementById("login-form");
const agree = document.getElementById("agree");

form.addEventListener("submit", (event) => {
    if (!agree.checked) {
        event.preventDefault();
        alert("請勾選同意條款");
        }
    });

const hotelInput = document.getElementById("hotel-id");
const hotelButton = document.getElementById("hotel-button");

hotelButton.addEventListener("click", () => {
    const value = hotelInput.value.trim();
    if (!/^\d+$/.test(value) || Number(value) < 1) {
        alert("請輸入正整數");
        return;
        }
    window.location.href = "/hotel/" + value;
    });