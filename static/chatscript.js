const chatBotImage = "../static/uc.png";
      const userImage = "../static/person.png";
      const botName = "UC BOT";
      const userName = "YOU";

      const messagerForm = get(".chatbot-input");
      const messagerInput = get(".input-message");
      const messagerChat = get(".messager-inner-container");

      messagerForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const msgText = messagerInput.value;
        if (!msgText) return;
        addNewMessage(userName, userImage, "user", msgText);
        messagerInput.value = "";
        botResponse(msgText);
      });

      function addNewMessage(name, img, side, text) {
        const msgHTML = `
<div class="msg ${side}-msg">
  <div class="message-image" style="background-image: url(${img})"></div>

  <div class="message-container">
    <div class="message-info">
      <div class="message-info-name">${name}</div>
    </div>

    <div class="message-content">${text}</div>
  </div>
</div>
`;

        messagerChat.insertAdjacentHTML("beforeend", msgHTML);
        messagerChat.scrollTop += 500;
      }
      function botResponse(rawText) {
        $.get("/get", { msg: rawText }).done(function (data) {
          console.log(rawText);
          console.log(data);
          const msgText = data;
          addNewMessage(botName, chatBotImage, "bot", msgText);
        });
      }
      function get(selector, root = document) {
        return root.querySelector(selector);
      }