document.getElementById("loginForm")
    .addEventListener("submit", function (e) {

        e.preventDefault();

        const email =
            document.getElementById("email")
                .value
                .trim();

        const password =
            document.getElementById("password")
                .value
                .trim();

        const error =
            document.getElementById("errorLogin");

        error.textContent = "";

        // DOCENTE

        if (
            email === "docente@educatec.com" &&
            password === "12345"
        ) {

            localStorage.setItem(
                "rol",
                "docente"
            );

            window.location.href =
                "dashboard_docente.html";

            return;
        }

        // ALUMNO

        if (
            email === "alumno@educatec.com" &&
            password === "12345"
        ) {

            localStorage.setItem(
                "rol",
                "alumno"
            );

            window.location.href =
                "dashboard_alumno.html";

            return;
        }

        error.textContent =
            "Correo o contraseña incorrectos";
    });