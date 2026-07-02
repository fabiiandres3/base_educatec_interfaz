const items = document.querySelectorAll('.carousel-item');
let current = 0;

function goTo(index) {
    items[current].classList.add('d-none');
    items[current].classList.remove('active');

    current = (index + items.length) % items.length;

    items[current].classList.remove('d-none');
    items[current].classList.add('active');
}

document.getElementById('btnPrev')
    .addEventListener('click', () => goTo(current - 1));

document.getElementById('btnNext')
    .addEventListener('click', () => goTo(current + 1));
