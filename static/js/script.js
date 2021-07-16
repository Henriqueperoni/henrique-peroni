const navSlide = () => {
    const burger = document.querySelector(".burger")
    const nav = document.querySelector(".nav-links")
    const navLinks = document.querySelectorAll(".nav-links li")

    burger.addEventListener("click", () => {

        // Toggle Navbar
        nav.classList.toggle("nav-active")

        // Animate Each li
        navLinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = ''
            } else {
                link.style.animation = `navLinksFade 0.5s ease forwards ${index / 7 + .4}s`
            }
        })

        // Burger Animation
        burger.classList.toggle("close-burger")

    });

}

navSlide()

// Close message container
function closeMessage() {
    const message = document.querySelector(".message-container")
    message.classList.add('delete-message')
    console.log('close')
}

const closeMessageBtn = document.querySelector(".close-message")

closeMessageBtn.addEventListener("click", () => {
    closeMessage()
})
