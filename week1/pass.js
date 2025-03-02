document.addEventListener(`DOMContentLoaded`, () => {
    const registerForm = document.getElementById("formReg")


    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const formData = new FormData(registerForm);
        const Email = formData.get(`Email`);
        const UserName = formData.get(`Username`);
        const Password = formData.get(`Password`);

        try {
            const response = await fetch("http://localhost:8000/pass", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ Email, UserName, Password })

            });
            if (response.ok) {
                alert(`registration successful`)
            } else { alert(`registration Failed`) }
        }
        catch (error) {
            console.log(error);
        }
    });
});