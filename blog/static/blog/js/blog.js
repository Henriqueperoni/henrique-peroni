const postAnim = gsap.timeline({ defaults: { ease: "power1.out" } });

postAnim.to(".post", { opacity: 1, duration: .6, stagger: 0.3 });

$(document).on("click", "#like-button", function (e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: '{% url "like" %}',
    data: {
      csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
      postid: $("#like-button").val(),
      action: "post",
    },
    success: function (json) {
      document.getElementById("like_count").innerHTML = json["result"];
      console.log(json);
    },
    error: function (xhr, errmsg, err) {},
  });
});