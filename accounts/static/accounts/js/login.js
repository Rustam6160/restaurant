// JavaScript for the registration form functionality

// Выбор элементов
const usernameInput = document.querySelector("input[placeholder='Enter username']");
const passwordInput = document.querySelector("input[placeholder='Enter password']");
const submitButton = document.querySelector(".section-btn button");

// Функция проверки ввода
function validateInputs() {
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    if (!username) {
        alert("Имя пользователя не может быть пустым");
        return false;
    }

    if (!password) {
        alert("Пароль не может быть пустым");
        return false;
    }

    if (password.length < 6) {
        alert("Пароль должен содержать минимум 6 символов");
        return false;
    }

    return true;
}

// Функция обработки отправки формы
function handleFormSubmit(event) {
    event.preventDefault();

    if (validateInputs()) {
        const userData = {
            username: usernameInput.value,
            password: passwordInput.value,
        };

        // Имитация отправки данных
        console.log("Данные пользователя отправлены:", userData);
        alert("Регистрация успешна!");

        // Очистка полей ввода
        usernameInput.value = "";
        passwordInput.value = "";
    }
}

// Добавление обработчика события на кнопку
submitButton.addEventListener("click", handleFormSubmit);
