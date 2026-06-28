const burger = document.querySelector(".burger");
const popup = document.querySelector(".popup-menu");
const closeBtn = document.querySelector(".popup-close");

burger.addEventListener("click", () => {
    popup.classList.add("open");
    });

closeBtn.addEventListener("click", () => {
    popup.classList.remove("open");
    });

const url1 = "https://cwpeng.github.io/test/assignment-3-1";
const url2 = "https://cwpeng.github.io/test/assignment-3-2";

const section2 = document.querySelector(".section2");
const section3 = document.querySelector(".section3");
const loadMoreBtn = document.querySelector(".load-more");

let attractions = [];
let rendered = 0;

async function loadAttractions() {
    try {
        const [res1, res2] = await Promise.all([fetch(url1), fetch(url2)]);
        const [info, picture] = await Promise.all([res1.json(), res2.json()]);

        const picMap = new Map();
        picture.rows.forEach(row => picMap.set(row.serial, row.pics));

        attractions = info.rows.map(row => ({
            name: row.sname,
            image: getFirstImage(picture.host, picMap.get(row.serial))
        }));

        renderBars(attractions.slice(0, 3));
        rendered = 3;
        loadMore();
    } catch (err) {
        console.error(err);
    }
}

function loadMore() {
    const next = attractions.slice(rendered, rendered + 10);
    renderBlocks(next);
    rendered += next.length;
    if (rendered >= attractions.length) {
        loadMoreBtn.style.display = "none";
    }
}

function getFirstImage(host, pics) {
    if (!pics) return "";
    const first = pics.split(".jpg")[0] + ".jpg";
    return host + first;
}

function renderBars(items) {
    items.forEach(item => {
        const bar = document.createElement("div");
        bar.className = "bar";

        const img = document.createElement("img");
        img.src = item.image;
        img.alt = item.name;

        const text = document.createElement("span");
        text.className = "bar-text";
        text.textContent = item.name;

        bar.appendChild(img);
        bar.appendChild(text);
        section2.appendChild(bar);
    });
}

function renderBlocks(items) {
    items.forEach(item => {
        const block = document.createElement("div");
        block.className = "block";

        const img = document.createElement("img");
        img.className = "block-img";
        img.src = item.image;
        img.alt = item.name;

        const star = document.createElement("img");
        star.className = "block-star";
        star.src = "star_473699.png";
        star.alt = "star";

        const text = document.createElement("div");
        text.className = "block-text";
        text.textContent = item.name;

        block.appendChild(img);
        block.appendChild(star);
        block.appendChild(text);
        section3.appendChild(block);
    });
}

loadMoreBtn.addEventListener("click", loadMore);

loadAttractions();