const introAnim = gsap.timeline({ defaults: { ease: "power1.out" } });

introAnim.to(".greeting", { y: "0%", duration: 1, delay: 0.2, stagger: 0.4 });
introAnim.to(
  ".intro-image",
  { transform: "scale(1.5)", opacity: 1, duration: 1 },
  "=-1"
);
introAnim.fromTo(
  ".path",
  { strokeDashoffset: 2000, opacity: 0 },
  { strokeDashoffset: 0, opacity: 1, duration: 1.5 },
  "=-1.8"
);
introAnim.to(".btn", { opacity: 1, duration: 0.5 }, "=-0.3");

const showAbout = gsap.timeline({
  scrollTrigger: {
    trigger: ".about-text",
    start: "top bottom",
  },
});

showAbout.from(".hard-work-wrapper h2", {
  opacity: 0,
  x: -250,
  duration: 1,
  stagger: 0.3,
});
showAbout.from(".about-text", { opacity: 0, x: 100, duration: 1 }, "=-1");
showAbout.from(".path-polygon", { strokeDashoffset: 5500, duration: 4 }, "=-1");
