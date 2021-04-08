const contactAnim = gsap.timeline({ defaults: { ease: "power1.out" } });

contactAnim
  .from(".circle1", { opacity: 0, y: "450px", x: "-400px", duration: 2 })
  .from(
    ".circle2",
    { opacity: 0, y: "-450px", x: "400px", duration: 2 },
    "<0.1"
  )
  .from(
    ".circle3",
    { opacity: 0, y: "-400px", x: "-200px", duration: 2 },
    "<0.1"
  )
  .from(
    ".circle4",
    { opacity: 0, y: "400px", x: "-200px", duration: 2 },
    "<0.1"
  )
  .from(
    ".circle5",
    { opacity: 0, y: "-400px", x: "-300px", duration: 2 },
    "<0.1"
  );
