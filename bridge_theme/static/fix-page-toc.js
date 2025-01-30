window.addEventListener('DOMContentLoaded', removePageTocNumbers);

function removePageTocNumbers(event) {
    for (const $a of document.querySelectorAll(".page-toc .toc-entry .nav-link")) {
        $a.innerText = $a.innerText.replace(/[\d.]+ /, '')
    }
}
