(function () {
    // Cookie consent banner logic (used on storefront pages)
    var STORAGE_KEY = 'cookie_consent_v1';
    var banner = document.getElementById('cookie-consent');
    if (!banner) return;
    var acceptBtn = document.getElementById('cookie-consent-accept') || banner.querySelector('button');

    function hideBanner() {
        banner.style.display = 'none';
    }

    try {
        if (localStorage.getItem(STORAGE_KEY) === '1') {
            hideBanner();
            return;
        }
    } catch (e) { /* ignore storage errors */ }

    if (acceptBtn) {
        acceptBtn.addEventListener('click', function (e) {
            e.preventDefault();
            try { localStorage.setItem(STORAGE_KEY, '1'); } catch (e) { /* ignore */ }
            hideBanner();
        });
    }
})();

(function () {
    // Smooth scroll helper for elements with data-scroll-to (home page)
    var triggers = document.querySelectorAll('[data-scroll-to]');
    if (!triggers || !triggers.forEach) return;

    triggers.forEach(function (el) {
        el.addEventListener('click', function () {
            var id = el.getAttribute('data-scroll-to');
            if (!id) return;
            var target = document.getElementById(id);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
})();

(function () {
    // Premium Business Cards price calculator and gallery (business-cards.html)
    var quantitySelect = document.getElementById('quantity');
    var finishSelect = document.getElementById('finish');
    var priceDisplay = document.getElementById('price-display');

    if (!quantitySelect || !finishSelect || !priceDisplay) return;

    var basePrices = {
        '100': 6500,
        '250': 12000,
        '500': 20000,
        '1000': 35000
    };

    var finishPrices = {
        'matte': 0,
        'glossy': 500,
        'spot-uv': 1500,
        'foil': 2000
    };

    function updatePrice() {
        var quantity = quantitySelect.value;
        var finish = finishSelect.value;
        var basePrice = basePrices[quantity];
        var finishPrice = finishPrices[finish];
        var totalPrice = basePrice + finishPrice;

        priceDisplay.textContent = '₦' + totalPrice.toLocaleString();
    }

    quantitySelect.addEventListener('change', updatePrice);
    finishSelect.addEventListener('change', updatePrice);

    // Thumbnail gallery
    var thumbnails = document.querySelectorAll('.thumbnail');
    var mainImage = document.getElementById('main-image');

    if (thumbnails && mainImage) {
        thumbnails.forEach(function (thumb) {
            thumb.addEventListener('click', function () {
                thumbnails.forEach(function (t) { t.classList.remove('active'); });
                thumb.classList.add('active');

                var imageType = thumb.dataset.image;
                if (!imageType) return;
                mainImage.innerHTML = '<span>' +
                    imageType.charAt(0).toUpperCase() + imageType.slice(1) +
                    ' Finish</span>';
            });
        });
    }

    // FAQ accordion on business-cards page
    window.toggleAccordion = function (trigger) {
        var content = trigger.nextElementSibling;
        var icon = trigger.querySelector('span:last-child');
        if (!content || !icon) return;

        document.querySelectorAll('.accordion-content').forEach(function (ac) {
            if (ac !== content) {
                ac.classList.remove('open');
                if (ac.previousElementSibling) {
                    var otherIcon = ac.previousElementSibling.querySelector('span:last-child');
                    if (otherIcon) otherIcon.textContent = '+';
                }
            }
        });

        content.classList.toggle('open');
        icon.textContent = content.classList.contains('open') ? '−' : '+';
    };

    // WhatsApp order intent button
    var orderBtn = document.getElementById('order-btn');
    if (orderBtn) {
        orderBtn.addEventListener('click', function () {
            var quantity = quantitySelect.value;
            var finish = finishSelect.value;
            var price = priceDisplay.textContent;

            var message = "Hi! I'd like to order business cards:\n\n" +
                "Quantity: " + quantity + " cards\n" +
                "Finish: " + finish + "\n" +
                "Total: " + price + "\n\n" +
                "Please send me the next steps.";

            var whatsappUrl = 'https://wa.me/12894367868?text=' + encodeURIComponent(message);
            window.open(whatsappUrl, '_blank');
        });
    }
})();

(function () {
    // Rigid boxes configurator (product-detail-premium.html)
    var groups = document.querySelectorAll('[data-option-group]');
    if (!groups || !groups.forEach) return;

    var totalEl = document.getElementById('quote-total');
    var perUnitEl = document.getElementById('quote-per-unit');
    var configEl = document.getElementById('quote-config');
    var timelineEl = document.getElementById('quote-timeline');
    var noteEl = document.getElementById('quote-note');
    var separator = ' \u2022 ';

    function formatCurrency(value) {
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    }

    function getActive(groupEl) {
        return groupEl.querySelector('.option.is-active') || groupEl.querySelector('.option');
    }

    function updateSummary() {
        var selections = {};
        var notes = [];
        var timelines = [];
        var total = 0;
        var units = 1;

        groups.forEach(function (groupEl) {
            var active = getActive(groupEl);
            if (!active) { return; }
            var key = groupEl.getAttribute('data-option-group');
            selections[key] = active;
            if (active.dataset.note) {
                notes.push(active.dataset.note);
            }
            if (active.dataset.timeline) {
                timelines.push(active.dataset.timeline);
            }

            if (key === 'quantity') {
                total += Number(active.dataset.total || 0);
                units = Number(active.dataset.units || 1);
            } else {
                total += Number(active.dataset.upcharge || 0);
            }
        });

        if (!selections.quantity || !totalEl || !perUnitEl || !configEl || !timelineEl || !noteEl) {
            return;
        }

        totalEl.innerHTML = '&#8358;' + formatCurrency(Math.round(total));
        var perUnit = units ? Math.round(total / units) : total;
        perUnitEl.textContent = '&#8358;' + formatCurrency(perUnit) + ' per unit';

        var configText = ['quantity', 'finish', 'insert'].map(function (key) {
            return selections[key] ? selections[key].dataset.label : null;
        }).filter(Boolean).join(separator);

        configEl.textContent = configText;
        timelineEl.textContent = timelines.length
            ? timelines.join(separator)
            : 'Production timeline shared after CAD sign-off.';
        noteEl.textContent = notes.length
            ? notes.join(' | ')
            : 'Project manager assigns QC checkpoints for you.';
    }

    groups.forEach(function (groupEl) {
        groupEl.addEventListener('click', function (event) {
            var target = event.target.closest('.option');
            if (!target) { return; }
            groupEl.querySelectorAll('.option').forEach(function (btn) {
                btn.classList.toggle('is-active', btn === target);
            });
            updateSummary();
        });
    });

    updateSummary();
})();

// Door hanger product detail gallery (product-detail.html)
(function () {
    var mainImage = document.querySelector('body.product-detail .media-card img');
    var thumbs = document.querySelectorAll('body.product-detail .media-thumb');

    if (!mainImage || !thumbs.length) return;

    thumbs.forEach(function (thumb) {
        thumb.addEventListener('click', function () {
            // swap image
            mainImage.src = thumb.src;
            mainImage.alt = thumb.alt || mainImage.alt;

            // simple active state
            thumbs.forEach(function (t) { t.classList.remove('is-active'); });
            thumb.classList.add('is-active');
        });
    });
})();


