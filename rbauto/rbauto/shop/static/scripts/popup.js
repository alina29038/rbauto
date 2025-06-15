document.addEventListener('DOMContentLoaded', () => {
    function showPopup(popup) {
        popup.className = 'popup popup__active';
        const closeBtn = popup.querySelector('.popup__close');
        const closeX = popup.querySelector('.popup__header__close');
        closeBtn.onclick = () => popup.className = "popup";
        closeX.onclick = () => popup.className = "popup";
    }

    const popupHolders = document.querySelectorAll('[data-popup]');
    for (const popupHolder of popupHolders) {
        const popup = document.getElementById(popupHolder.dataset.popup);
        if (!popup) {
            continue;
        }
        
        popupHolder.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            showPopup(popup);
        });
    }
});