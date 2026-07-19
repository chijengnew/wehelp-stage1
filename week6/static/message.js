const contentInput = document.querySelector("#content");
const messageList = document.querySelector("#messages");

async function loadMessages() {
    const response = await fetch("/api/message");
    const result = await response.json();
    if (!result.ok) {
        return;
        }
    messageList.innerHTML = "";
    for (const message of result.data) {
        const line = document.createElement("p");
        const author = document.createElement("b");
        author.textContent = message.name + "：";
        line.appendChild(author);
        line.appendChild(document.createTextNode(message.content));
        if (message.self) {
            const removeButton = document.createElement("button");
            removeButton.textContent = "x";
            removeButton.addEventListener("click", function () {
                removeMessage(message.id);
            });
            line.appendChild(removeButton);
            }
        messageList.appendChild(line);
        }
    }

async function submitMessage() {
    const content = contentInput.value.trim();
    if (content === "") {
        return;
        }
    const response = await fetch("/api/message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: content })
    });
    const result = await response.json();
    if (result.ok) {
        contentInput.value = "";
        loadMessages();
        }
    }

async function removeMessage(id) {
    if (!confirm("確定要刪除這則留言嗎？")) {
        return;
    }
    const response = await fetch("/api/message/" + id, { method: "DELETE" });
    const result = await response.json();
    if (result.ok) {
        loadMessages();
        }
    }

document.querySelector("#submit").addEventListener("click", submitMessage);
loadMessages();