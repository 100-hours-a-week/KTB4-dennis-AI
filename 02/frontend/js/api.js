const API_BASE_URL = "http://127.0.0.1:8000";

async function requestAPI(path, options = {}) {
  const url = `${API_BASE_URL}${path}`;

  const defaultOptions = {
    headers: {
      "Content-Type": "application/json"
    }
  };

  const finalOptions = {
    ...defaultOptions,
    ...options,
    headers: {
      ...defaultOptions.headers,
      ...(options.headers || {})
    }
  };

  const response = await fetch(url, finalOptions);

  if (!response.ok) {
    let errorMessage = "요청 처리 중 오류가 발생했습니다.";

    try {
      const errorData = await response.json();

      if (errorData.detail) {
        if (Array.isArray(errorData.detail)) {
          errorMessage = errorData.detail
            .map(error => error.msg)
            .join(", ");
        } else {
          errorMessage = errorData.detail;
        }
      }
    } catch (error) {
      errorMessage = `서버 오류가 발생했습니다. 상태 코드: ${response.status}`;
    }

    throw new Error(errorMessage);
  }

  if (response.status === 204) {
    return null;
  }

  return response.json();
}

function formatDateTime(dateTimeText) {
  if (!dateTimeText) {
    return "";
  }

  const date = new Date(dateTimeText);

  if (Number.isNaN(date.getTime())) {
    return dateTimeText;
  }

  return date.toLocaleString("ko-KR", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function getPostIdFromUrl() {
  const params = new URLSearchParams(window.location.search);
  const postId = Number(params.get("id"));

  if (!Number.isInteger(postId) || postId <= 0) {
    return null;
  }

  return postId;
}

function showElement(element) {
  element.classList.remove("hidden");
}

function hideElement(element) {
  element.classList.add("hidden");
}