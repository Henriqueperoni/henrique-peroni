const projectAnim = gsap.timeline({ defaults: { ease: "power1.out" } });
if (window.location.href === "http://127.0.0.1:8000/projects/" || window.location.href === "http://www.henriqueperoni.com/projects/") {
  projectAnim.from(".projects", { y: 200, duration: 1 });
  projectAnim.from(
    "body > div > div:nth-child(1) > div.image-wrapper ",
    { opacity: 0, duration: 2 },
    "-=0.5"
  );
  projectAnim.from(
    "body > div > div:nth-child(1) > div.image-wrapper > a > img",
    { opacity: 0, transform: "scale(1.5)", duration: 0.8 },
    "-=2"
  );
  projectAnim.from(
    "body > div > div:nth-child(1) > div.line",
    { width: 0, duration: 0.8 },
    "-=1.5"
  );
}

function startModal() {
    const modal = document.getElementById("modal-delete");
    modal.classList.add("show-modal");
    
    modal.addEventListener("click", (e) => {
        if (e.target.id == "modal-delete" || e.target.className == "close-modal" || e.target.className == "btn btn-cancel")
            modal.classList.remove("show-modal");
    });
};

document.addEventListener("DOMContentLoaded", () => {
    const deleteButton = document.getElementById("delete-button");
    if (deleteButton) {
        deleteButton.addEventListener("click", () => {
            startModal();
        });
    }
});