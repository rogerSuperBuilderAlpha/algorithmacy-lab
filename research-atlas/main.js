const REPO = "https://github.com/rogerSuperBuilderAlpha/algorithmacy-lab";
const BASE = `${REPO}/blob/main/`;

const sections = {
  open: { title: "Open questions", eyebrow: "WHAT THE LAB STILL NEEDS", description: "Questions waiting for a test, real data, tooling, or review. Status comes from OPEN_QUESTIONS.md." },
  question: { title: "Research questions", eyebrow: "FULL QUESTION PIPELINE", description: "Each entry points to a question taken through the lab's research protocol." },
  probe: { title: "Probes", eyebrow: "FOCUSED EXPERIMENTS", description: "Small tests of a specific hypothesis. A catalog row is not an independent finding." },
  study: { title: "Studies", eyebrow: "STUDY CORPUS", description: "Study folders with reported findings, linked back to their source files." },
  foundations: { title: "Foundations", eyebrow: "THE INSTRUMENT", description: "Experiments that examine exact Φ and proposed measurement shortcuts." },
};

let catalog = [];
let view = "overview";
let selected = null;
let limit = 60;

const $ = (selector) => document.querySelector(selector);
const el = (tag, className, text) => {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
};
const words = (value) => String(value || "").replace(/_/g, " ");

function sourceUrl(row, file) {
  if (row.kind === "open") return `${BASE}OPEN_QUESTIONS.md`;
  const path = row.path.split("/").map(encodeURIComponent).join("/");
  return `${REPO}/${file ? "blob" : row.path.endsWith(".py") ? "blob" : "tree"}/main/${path}${file ? `/${file}` : ""}`;
}

function pageTitle(row) {
  return row.title || row.concept || row.question || words(row.id);
}

function summary(row) {
  return row.finding || row.result || row.question || row.hypothesis || "Open the source to read more.";
}

function setView(next) {
  const [section, id] = next.split(":");
  view = section in sections ? section : "overview";
  selected = null;
  limit = 60;
  $("#overview").hidden = view !== "overview";
  $("#catalog-view").hidden = view === "overview";
  document.querySelectorAll(".nav-item").forEach((node) => {
    node.classList.toggle("active", node.dataset.view === view);
    node.setAttribute("aria-current", node.dataset.view === view ? "page" : "false");
  });
  if (view !== "overview") {
    const section = sections[view];
    $("#list-title").textContent = section.title;
    $("#list-eyebrow").textContent = section.eyebrow;
    $("#list-description").textContent = section.description;
    $("#search").value = "";
    $("#needs-filter").value = "all";
    $("#needs-wrap").hidden = view !== "open";
    renderList();
    const target = catalog.find((row) => row.kind === view && row.id === id);
    if (target) {
      selected = target;
      renderList();
      renderDetail(target);
    }
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function overviewCard(number, title, description, kind, count) {
  const button = el("button", "overview-card");
  button.type = "button";
  button.append(el("span", "card-index", number), el("strong", "", title), el("p", "", description));
  const foot = el("footer");
  foot.append(el("span", "", `${count} ${count === 1 ? "entry" : "entries"}`), el("span", "", "Explore ↗"));
  button.append(foot);
  button.addEventListener("click", () => { location.hash = kind; });
  return button;
}

function renderOverview() {
  const counts = Object.fromEntries(Object.keys(sections).map((kind) => [kind, catalog.filter((row) => row.kind === kind).length]));
  $("#open-nav-count").textContent = counts.open || 0;
  const cards = [
    ["01", "Open questions", "See what needs data, computation, tooling, or review.", "open"],
    ["02", "Research questions", "Follow full questions through hypotheses and findings.", "question"],
    ["03", "Probes", "Inspect focused tests and the verdicts they report.", "probe"],
    ["04", "Studies", "Explore the study corpus and its source material.", "study"],
    ["05", "Foundations", "Understand the instrument behind the verdicts.", "foundations"],
  ];
  $("#overview-grid").replaceChildren(...cards.map((card) => overviewCard(...card, counts[card[3]])));
}

function filteredRows() {
  const term = $("#search").value.trim().toLocaleLowerCase();
  const need = $("#needs-filter").value;
  return catalog.filter((row) => row.kind === view && (view !== "open" || need === "all" || row.needs === need) && (!term || [row.id, row.title, row.question, row.concept, row.hypothesis, row.finding, row.result, row.slug].some((field) => String(field || "").toLocaleLowerCase().includes(term))));
}

function researchCard(row) {
  const button = el("button", `research-card${selected === row ? " selected" : ""}`);
  button.type = "button";
  const meta = el("span", "meta");
  meta.append(el("span", "", row.id), el("span", "", row.kind === "open" ? `${row.status} · needs ${row.needs}` : row.runtime === "fast" ? "Reproduction command registered" : row.runtime === "slow" ? "Nightly reproduction check" : "Source in repo"));
  button.append(meta, el("strong", "", pageTitle(row)), el("p", "", summary(row)));
  button.addEventListener("click", () => {
    selected = row;
    document.querySelectorAll(".research-card").forEach((card) => card.classList.remove("selected"));
    button.classList.add("selected");
    renderDetail(row);
    if (window.innerWidth < 721) $("#detail").scrollIntoView({ behavior: "smooth", block: "start" });
  });
  return button;
}

function renderList() {
  const all = catalog.filter((row) => row.kind === view);
  const rows = filteredRows();
  $("#list-total").textContent = all.length.toLocaleString();
  $("#shown-count").textContent = `${rows.length.toLocaleString()} matching`;
  const list = $("#card-list");
  list.replaceChildren(...rows.slice(0, limit).map(researchCard));
  if (!rows.length) list.append(el("div", "empty-state", "No entries match these filters."));
  if (rows.length > limit) {
    const more = el("button", "research-card", `Show more (${rows.length - limit} remaining)`);
    more.type = "button";
    more.addEventListener("click", () => { limit += 60; renderList(); });
    list.append(more);
  }
  if (!selected || !rows.includes(selected)) {
    selected = null;
    $("#detail").replaceChildren();
    const placeholder = el("div", "detail-placeholder");
    placeholder.append(el("span", "", "↗"), el("h2", "", "Choose a card"), el("p", "", "Open an entry to see its claim, available files, and path into the repo."));
    $("#detail").append(placeholder);
  }
}

function detailField(parent, label, value) {
  if (!value) return;
  parent.append(el("p", "detail-label", label), el("p", "detail-text", value));
}

function detailLink(parent, label, href) {
  const a = el("a", "", `${label} ↗`);
  a.href = href;
  a.target = "_blank";
  a.rel = "noopener";
  parent.append(a);
}

function renderDetail(row) {
  const box = $("#detail");
  box.replaceChildren(el("p", "eyebrow", `${row.kind === "open" ? "OPEN THREAD" : row.kind.toUpperCase()} · ${row.id}`), el("h2", "", pageTitle(row)));
  detailField(box, "Question", row.question || row.hypothesis);
  detailField(box, "Reported finding", row.finding || row.result || row.verdict);
  if (row.kind === "open") {
    detailField(box, "What is needed", `${row.needs || "Unknown"} · ${row.status || "Unknown status"}`);
    detailField(box, "Where the repo points", row.where);
    detailField(box, "First command", row.first_command);
  }
  if (row.artifacts) detailField(box, "Available files", Object.entries(row.artifacts).filter(([, exists]) => exists).map(([name]) => name).join(" · ") || "No listed artifacts");
  if (row.reproduce?.length) detailField(box, "Reproduce", row.reproduce.slice(0, 2).join("  /  "));
  if (row.kind !== "open") detailField(box, "Evidence label", row.runtime === "fast" ? "Registered reproduction command" : row.runtime === "slow" ? "Registered nightly check" : "No registered reproduction command in the catalog");
  const links = el("div", "detail-links");
  detailLink(links, row.kind === "open" ? "Open question list" : "Open source", sourceUrl(row));
  if (row.kind === "open") {
    const path = row.where?.match(/(?:org_frontier|foundations|submissions|tools|ci)\/[A-Za-z0-9_./-]+|(?:MAINTAINERS|PUBLISHING|CONTRIBUTING)\.md/)?.[0];
    if (path) detailLink(links, "Open related work", `${REPO}/${path.endsWith(".md") || path.endsWith(".py") ? "blob" : "tree"}/main/${path.split("/").map(encodeURIComponent).join("/")}`);
  }
  if (row.kind === "question" && row.artifacts?.paper) detailLink(links, "Read paper", sourceUrl(row, "paper.md"));
  if (row.kind === "study") detailLink(links, "Read findings", sourceUrl(row, "FINDINGS.md"));
  box.append(links);
}

async function start() {
  try {
    const response = await fetch("../catalog.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    if (!Array.isArray(data.rows)) throw new Error("Catalog has no rows");
    catalog = data.rows;
    $("#source-status").textContent = `${catalog.length.toLocaleString()} catalog entries · from repo`;
    renderOverview();
    setView(location.hash.slice(1));
  } catch (error) {
    $("#source-status").textContent = "Catalog unavailable";
    $("#overview-grid").replaceChildren(el("div", "empty-state", `Could not load ../catalog.json (${error.message}). Serve the repository root with python3 -m http.server.`));
  }
}

$("#nav").addEventListener("click", (event) => {
  const item = event.target.closest("[data-view]");
  if (item) location.hash = item.dataset.view;
});
$("#overview").addEventListener("click", (event) => {
  const item = event.target.closest("[data-go]");
  if (item) location.hash = item.dataset.go;
});
$("#search").addEventListener("input", () => { limit = 60; renderList(); });
$("#needs-filter").addEventListener("change", () => { limit = 60; renderList(); });
window.addEventListener("hashchange", () => setView(location.hash.slice(1)));
start();
