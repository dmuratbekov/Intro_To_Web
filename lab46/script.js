const gallery = document.getElementById("gallery");

const modal = document.getElementById("modal");
const modalImg = document.getElementById("modalImg");
const captionText = document.getElementById("captionText");

const closeBtn = document.getElementById("closeBtn");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

const images = [
    { url: "https://picsum.photos/id/1015/900/600", title: "Mountain Lake" },
    { url: "https://picsum.photos/id/1025/900/600", title: "Dog Portrait" },
    { url: "https://picsum.photos/id/1035/900/600", title: "Forest Road" },
    { url: "https://picsum.photos/id/1043/900/600", title: "Ocean Coast" },
    { url: "https://picsum.photos/id/1050/900/600", title: "Desert" },
    { url: "https://picsum.photos/id/1069/900/600", title: "City View" },
    { url: "https://picsum.photos/id/1074/900/600", title: "Bridge" },
    { url: "https://picsum.photos/id/1084/900/600", title: "Snow" }
];

let currentIndex = 0;

function renderGallery() {
    gallery.innerHTML = "";

    images.forEach((img, index) => {
        const el = document.createElement("img");
        el.src = img.url.replace("/900/600", "/400/280");
        el.alt = img.title;
        el.title = img.title;

        el.addEventListener("click", () => openModal(index));
        gallery.appendChild(el);
    });
}

function openModal(index) {
    currentIndex = index;
    updateModalImage();
    modal.classList.remove("hidden");
    localStorage.setItem("lastViewedIndex", String(currentIndex));
}

function closeModal() {
    modal.classList.add("hidden");
}

function updateModalImage() {
    const { url, title } = images[currentIndex];
    modalImg.src = url;
    captionText.textContent = `${title} (${currentIndex + 1}/${images.length})`;

    modalImg.classList.add("zoom");
    setTimeout(() => modalImg.classList.remove("zoom"), 150);
}

function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    updateModalImage();
    localStorage.setItem("lastViewedIndex", String(currentIndex));
}

function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateModalImage();
    localStorage.setItem("lastViewedIndex", String(currentIndex));
}

modal.addEventListener("click", (e) => {
    if (e.target === modal) closeModal();
});

closeBtn.addEventListener("click", closeModal);
nextBtn.addEventListener("click", nextImage);
prevBtn.addEventListener("click", prevImage);

document.addEventListener("keydown", (e) => {
    if (modal.classList.contains("hidden")) return;

    if (e.key === "Escape") closeModal();
    if (e.key === "ArrowRight") nextImage();
    if (e.key === "ArrowLeft") prevImage();
});

function restoreLastViewed() {
    const saved = localStorage.getItem("lastViewedIndex");
    if (saved === null) return;

    const index = Number(saved);
    if (!Number.isFinite(index) || index < 0 || index >= images.length) return;

    openModal(index);
}

renderGallery();
restoreLastViewed();