const postForm = document.getElementById("post-form");
const authorNameInput = document.getElementById("author-name");
const titleInput = document.getElementById("title");
const contentInput = document.getElementById("content");
const errorMessage = document.getElementById("error-message");

postForm.addEventListener("submit", async event => {
  event.preventDefault();

  hideElement(errorMessage);

  const authorName = authorNameInput.value.trim();
  const title = titleInput.value.trim();
  const content = contentInput.value.trim();

  if (!authorName) {
    showError("작성자 이름을 입력해주세요.");
    return;
  }

  if (!title) {
    showError("제목을 입력해주세요.");
    return;
  }

  if (!content) {
    showError("내용을 입력해주세요.");
    return;
  }

  try {
    const newPost = await requestAPI("/posts", {
      method: "POST",
      body: JSON.stringify({
        author_name: authorName,
        title: title,
        content: content
      })
    });

    window.location.href = `detail.html?id=${newPost.id}`;
  } catch (error) {
    showError(error.message);
  }
});

function showError(message) {
  errorMessage.textContent = message;
  showElement(errorMessage);
}