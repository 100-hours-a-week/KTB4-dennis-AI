const postId = getPostIdFromUrl();

const postLoadingMessage = document.getElementById("post-loading-message");
const postErrorMessage = document.getElementById("post-error-message");
const postDetail = document.getElementById("post-detail");

const postTitle = document.getElementById("post-title");
const postAuthor = document.getElementById("post-author");
const postDate = document.getElementById("post-date");
const postContent = document.getElementById("post-content");

const commentList = document.getElementById("comment-list");
const commentErrorMessage = document.getElementById("comment-error-message");
const emptyCommentMessage = document.getElementById("empty-comment-message");

const commentForm = document.getElementById("comment-form");
const commentAuthorNameInput = document.getElementById("comment-author-name");
const commentContentInput = document.getElementById("comment-content");

async function initializePage() {
  if (postId === null) {
    hideElement(postLoadingMessage);
    postErrorMessage.textContent = "올바르지 않은 게시글 주소입니다.";
    showElement(postErrorMessage);
    commentForm.classList.add("hidden");
    return;
  }

  await loadPostDetail();
  await loadComments();
}

async function loadPostDetail() {
  hideElement(postErrorMessage);
  showElement(postLoadingMessage);
  hideElement(postDetail);

  try {
    const post = await requestAPI(`/posts/${postId}`);

    postTitle.textContent = post.title;
    postAuthor.textContent = `작성자: ${post.author_name}`;
    postDate.textContent = `작성일: ${formatDateTime(post.created_at)}`;
    postContent.textContent = post.content;

    hideElement(postLoadingMessage);
    showElement(postDetail);
  } catch (error) {
    hideElement(postLoadingMessage);
    postErrorMessage.textContent = error.message;
    showElement(postErrorMessage);
    commentForm.classList.add("hidden");
  }
}

async function loadComments() {
  hideElement(commentErrorMessage);
  hideElement(emptyCommentMessage);

  commentList.innerHTML = "";

  try {
    const comments = await requestAPI(`/posts/${postId}/comments`);

    if (comments.length === 0) {
      showElement(emptyCommentMessage);
      return;
    }

    comments.forEach(comment => {
      const li = document.createElement("li");
      li.className = "comment-item";

      const meta = document.createElement("div");
      meta.className = "meta";

      const author = document.createElement("span");
      author.textContent = `작성자: ${comment.author_name}`;

      const date = document.createElement("span");
      date.textContent = `작성일: ${formatDateTime(comment.created_at)}`;

      const content = document.createElement("p");
      content.className = "comment-content";
      content.textContent = comment.content;

      meta.appendChild(author);
      meta.appendChild(date);

      li.appendChild(meta);
      li.appendChild(content);

      commentList.appendChild(li);
    });
  } catch (error) {
    commentErrorMessage.textContent = error.message;
    showElement(commentErrorMessage);
  }
}

commentForm.addEventListener("submit", async event => {
  event.preventDefault();

  hideElement(commentErrorMessage);

  const authorName = commentAuthorNameInput.value.trim();
  const content = commentContentInput.value.trim();

  if (!authorName) {
    showCommentError("댓글 작성자 이름을 입력해주세요.");
    return;
  }

  if (!content) {
    showCommentError("댓글 내용을 입력해주세요.");
    return;
  }

  try {
    await requestAPI(`/posts/${postId}/comments`, {
      method: "POST",
      body: JSON.stringify({
        author_name: authorName,
        content: content
      })
    });

    commentContentInput.value = "";
    await loadComments();
  } catch (error) {
    showCommentError(error.message);
  }
});

function showCommentError(message) {
  commentErrorMessage.textContent = message;
  showElement(commentErrorMessage);
}

initializePage();