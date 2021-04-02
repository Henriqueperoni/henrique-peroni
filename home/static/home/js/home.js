const introAnim = gsap.timeline({ defaults: { ease: "power1.out" } });

introAnim.to(".greeting", { y: "0%", duration: 1, delay: 0.2, stagger: 0.4 });
introAnim.fromTo(
  ".intro-image",
  { transform: 'scale(1.5)', opacity: 0 },
  { transform: 'scale(1)', opacity: 1, duration: 1 },
  "=-1"
);
introAnim.to(".btn-portfolio", { opacity: 1, duration: 0.5 }, "=-0.3");
introAnim.fromTo(
  ".path",
  { strokeDashoffset: 2000, opacity: 0 },
  { strokeDashoffset: 0, opacity: 1, duration: 0.8 },
  "=-1.5"
);
