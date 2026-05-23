const postList = document.getElementById("post-list");
const loadingMessage = document.getElementById("loading-message");
const errorMessage = document.getElementById("error-message");
const emptyMessage = document.getElementById("empty-message");
const refreshButton = document.getElementById("refresh-button");

async function loadPosts() {
  hideElement(errorMessage);
  hideElement(emptyMessage);
  showElement(loadingMessage);

  postList.innerHTML = "";

  try {
    const posts = await requestAPI("/posts");

    hideElement(loadingMessage);

    if (posts.length === 0) {
      showElement(emptyMessage);
      return;
    }

    posts.forEach(post => {
      const li = document.createElement("li");
      li.className = "post-item";

      const titleLink = document.createElement("a");
      titleLink.className = "post-title";
      titleLink.href = `detail.html?id=${post.id}`;
      titleLink.textContent = post.title;

      const meta = document.createElement("div");
      meta.className = "meta";

      const author = document.createElement("span");
      author.textContent = `작성자: ${post.author_name}`;

      const date = document.createElement("span");
      date.textContent = `작성일: ${formatDateTime(post.created_at)}`;

      const summary = document.createElement("p");
      summary.className = "post-summary";
      summary.textContent = makeSummary(post.content);

      meta.appendChild(author);
      meta.appendChild(date);

      li.appendChild(titleLink);
      li.appendChild(meta);
      li.appendChild(summary);

      postList.appendChild(li);
    });
  } catch (error) {
    hideElement(loadingMessage);
    errorMessage.textContent = error.message;
    showElement(errorMessage);
  }
}

function makeSummary(content) {
  if (!content) {
    return "";
  }

  if (content.length <= 80) {
    return content;
  }

  return `${content.slice(0, 80)}...`;
}

refreshButton.addEventListener("click", loadPosts);

loadPosts();