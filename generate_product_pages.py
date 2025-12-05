#!/usr/bin/env python3
"""
Script to generate product detail pages with full SEO optimization
"""

products = [
    {
        "name": "T-Shirts",
        "slug": "t-shirts",
        "title": "Custom T-Shirt Printing | T-Shirt Printing Lagos Nigeria | Avitprint",
        "description": "Custom t-shirt printing in Lagos, Nigeria. Full-color t-shirt printing, cotton t-shirts, promotional t-shirts, event t-shirts. Fast delivery t-shirt printing services.",
        "keywords": "t-shirts, t-shirt printing, custom t-shirts, t-shirt printing Lagos, Nigeria t-shirts, promotional t-shirts, event t-shirts, cotton t-shirts, full color t-shirt printing, custom apparel",
        "image": "tshirt-printing-in-lagos.jpeg",
        "price": "₦7,500",
        "category": "Apparel",
        "eyebrow": "Brand apparel"
    },
    {
        "name": "Mugs",
        "slug": "mugs",
        "title": "Custom Mugs Printing | Promotional Mugs Lagos | Avitprint",
        "description": "Custom mugs printing in Lagos, Nigeria. Dishwasher-safe ceramic mugs, promotional mugs, branded mugs with vibrant full-color printing. Fast delivery mug printing services.",
        "keywords": "mugs, custom mugs, promotional mugs, mug printing, ceramic mugs, branded mugs, mug printing Lagos, Nigeria mugs, dishwasher safe mugs, custom drinkware",
        "image": "mug-printing.jpg",
        "price": "₦4,500",
        "category": "Promotional",
        "eyebrow": "Promotional items"
    },
    {
        "name": "Roll-up Banners",
        "slug": "roll-up-banners",
        "title": "Roll-Up Banners Printing | Retractable Banners Lagos | Avitprint",
        "description": "Roll-up banners printing in Lagos, Nigeria. Retractable banners with aluminium stand, tear-resistant printing, portable display banners. Professional banner printing services.",
        "keywords": "roll-up banners, retractable banners, portable banners, display banners, banner printing, roll-up banner printing Lagos, Nigeria banners, event banners, trade show banners",
        "image": "Roll-Up Banner.jpg",
        "price": "₦28,000",
        "category": "Events",
        "eyebrow": "Event signage"
    },
    {
        "name": "A5 Jotters",
        "slug": "jotters",
        "title": "Custom Jotters Printing | Notebook Printing Lagos | Avitprint",
        "description": "Custom jotters and notebooks printing in Lagos, Nigeria. A5 jotters with soft cover spiral binding, hard cover options available. Custom branded notebooks printing services.",
        "keywords": "jotters, notebooks, custom notebooks, jotter printing, notebook printing Lagos, Nigeria jotters, branded notebooks, spiral notebooks, custom stationery",
        "image": "jotter-printing-in-lagos.jpg",
        "price": "₦1,500",
        "category": "Stationery",
        "eyebrow": "Office essentials"
    },
    {
        "name": "Desk Calendars",
        "slug": "desk-calendars",
        "title": "Custom Desk Calendars | Calendar Printing Lagos | Avitprint",
        "description": "Custom desk calendars printing in Lagos, Nigeria. A4 desk calendars with custom branding, monthly calendars, promotional calendars. Professional calendar printing services.",
        "keywords": "desk calendars, custom calendars, calendar printing, promotional calendars, branded calendars, calendar printing Lagos, Nigeria calendars, office calendars, marketing calendars",
        "image": "table-calender.jpg",
        "price": "₦3,500",
        "category": "Promotional",
        "eyebrow": "Promotional items"
    },
    {
        "name": "Brochures",
        "slug": "brochures",
        "title": "Brochure Printing | Custom Brochures Lagos | Avitprint",
        "description": "Brochure printing in Lagos, Nigeria. Tri-fold brochures, bi-fold brochures, custom brochure layouts. Premium brochure printing with full-color design. Fast delivery brochure services.",
        "keywords": "brochures, brochure printing, custom brochures, tri-fold brochures, bi-fold brochures, brochure printing Lagos, Nigeria brochures, marketing brochures, promotional brochures",
        "image": "brochures.jpg",
        "price": "₦1,500",
        "category": "Marketing",
        "eyebrow": "Marketing essentials"
    },
    {
        "name": "Letterheads",
        "slug": "letterheads",
        "title": "Letterhead Printing | Custom Letterheads Lagos | Avitprint",
        "description": "Letterhead printing in Lagos, Nigeria. A4 letterheads with company branding, professional letterheads, corporate stationery. Premium letterhead printing services.",
        "keywords": "letterheads, letterhead printing, custom letterheads, corporate letterheads, business letterheads, letterhead printing Lagos, Nigeria letterheads, professional stationery",
        "image": "letterheads.jpg",
        "price": "₦20,000",
        "category": "Stationery",
        "eyebrow": "Office essentials"
    },
    {
        "name": "Premium Business Cards",
        "slug": "premium-business-cards",
        "title": "Premium Business Cards | Luxury Business Cards Lagos | Avitprint",
        "description": "Premium business cards printing in Lagos, Nigeria. Luxury business cards with spot UV, foil stamping, embossed finish. High-end business card printing services.",
        "keywords": "premium business cards, luxury business cards, spot UV cards, foil stamping, embossed business cards, premium cards Lagos, Nigeria luxury cards, high-end business cards",
        "image": "luxury-cards.jpg",
        "price": "₦20,000",
        "category": "Professional",
        "eyebrow": "Premium essentials"
    },
    {
        "name": "Custom Pens",
        "slug": "custom-pens",
        "title": "Custom Pens Printing | Promotional Pens Lagos | Avitprint",
        "description": "Custom pens printing in Lagos, Nigeria. Ballpoint pens with logo printing, promotional pens, branded pens. Fast delivery custom pen printing services.",
        "keywords": "custom pens, promotional pens, branded pens, pen printing, logo pens, custom pens Lagos, Nigeria pens, promotional items, branded merchandise",
        "image": "pens.jpg",
        "price": "₦1,500",
        "category": "Promotional",
        "eyebrow": "Promotional items"
    },
    {
        "name": "Promotional Bags",
        "slug": "promotional-bags",
        "title": "Promotional Bags Printing | Custom Bags Lagos | Avitprint",
        "description": "Promotional bags printing in Lagos, Nigeria. Tote bags, jute bags, custom printed bags with full-color printing. Durable promotional bag printing services.",
        "keywords": "promotional bags, custom bags, tote bags, jute bags, branded bags, bag printing Lagos, Nigeria bags, shopping bags, promotional merchandise",
        "image": "paper-bag-printing.jpg",
        "price": "₦6,800",
        "category": "Promotional",
        "eyebrow": "Promotional items"
    },
    {
        "name": "Polo T-Shirts",
        "slug": "polo-t-shirts",
        "title": "Polo T-Shirt Printing | Custom Polo Shirts Lagos | Avitprint",
        "description": "Polo t-shirt printing in Lagos, Nigeria. Custom polo shirts with full-color printing, soft cotton polos, promotional polo shirts. Professional polo shirt printing services.",
        "keywords": "polo shirts, polo t-shirts, custom polo shirts, polo printing, branded polos, polo printing Lagos, Nigeria polo shirts, promotional polos, corporate apparel",
        "image": "polo-printing-near-me.jpg",
        "price": "₦10,000",
        "category": "Apparel",
        "eyebrow": "Brand apparel"
    },
    {
        "name": "Backdrops",
        "slug": "backdrops",
        "title": "Custom Backdrops Printing | Event Backdrops Lagos | Avitprint",
        "description": "Custom backdrops printing in Lagos, Nigeria. Event backdrops, photo backdrops, promotional backdrops with full-color printing. Large format backdrop printing services.",
        "keywords": "backdrops, event backdrops, photo backdrops, custom backdrops, backdrop printing, backdrop printing Lagos, Nigeria backdrops, event signage, large format printing",
        "image": "backdrop-.jpg",
        "price": "₦250,000",
        "category": "Events",
        "eyebrow": "Event signage"
    },
    {
        "name": "Nylon Bags",
        "slug": "nylon-bags",
        "title": "Nylon Bags Printing | Custom Nylon Bags Lagos | Avitprint",
        "description": "Nylon bags printing in Lagos, Nigeria. Durable LD nylon bags with spot color printing, waterproof nylon bags, promotional nylon bags. Custom nylon bag printing services.",
        "keywords": "nylon bags, custom nylon bags, LD bags, nylon bag printing, waterproof bags, nylon bags Lagos, Nigeria nylon bags, promotional bags, durable bags",
        "image": "nylon-printing-near-me.jpg",
        "price": "₦22,000",
        "category": "Promotional",
        "eyebrow": "Promotional items"
    },
    {
        "name": "Wedding Invitations",
        "slug": "wedding-invitations",
        "title": "Wedding Invitations Printing | Custom Wedding Cards Lagos | Avitprint",
        "description": "Wedding invitations printing in Lagos, Nigeria. Elegant wedding invites with RSVP cards, custom wedding cards, premium wedding stationery. Luxury wedding invitation printing.",
        "keywords": "wedding invitations, wedding cards, custom wedding invitations, wedding stationery, RSVP cards, wedding printing Lagos, Nigeria wedding cards, luxury invitations",
        "image": "wedding-invitation-card.jpg",
        "price": "₦2,500",
        "category": "Events",
        "eyebrow": "Special events"
    },
    {
        "name": "Courier Bags",
        "slug": "courier-bags",
        "title": "Courier Bags Printing | Custom Courier Bags Lagos | Avitprint",
        "description": "Courier bags printing in Lagos, Nigeria. Marketing courier bags, tamper-proof poly mailers, custom courier packaging. Durable courier bag printing services.",
        "keywords": "courier bags, poly mailers, shipping bags, courier packaging, custom mailers, courier bags Lagos, Nigeria courier bags, tamper proof bags, shipping supplies",
        "image": "courier-bags.jpg",
        "price": "₦15,000",
        "category": "Packaging",
        "eyebrow": "Packaging"
    },
    {
        "name": "Menu Cards",
        "slug": "menu-cards",
        "title": "Menu Cards Printing | Restaurant Menu Printing Lagos | Avitprint",
        "description": "Menu cards printing in Lagos, Nigeria. Custom menu cards with lamination, restaurant menus, cafe menus, food menu printing. Professional menu card printing services.",
        "keywords": "menu cards, restaurant menus, custom menus, menu printing, cafe menus, menu printing Lagos, Nigeria menus, food menus, restaurant stationery",
        "image": "menu.jpg",
        "price": "₦15,000",
        "category": "Hospitality",
        "eyebrow": "Hospitality"
    },
    {
        "name": "Vehicle Branding",
        "slug": "vehicle-branding",
        "title": "Vehicle Branding | Car Wrap Printing Lagos | Avitprint",
        "description": "Vehicle branding services in Lagos, Nigeria. Car wrap printing, vehicle graphics, truck branding, van wrapping. Professional vehicle branding with full-color printing.",
        "keywords": "vehicle branding, car wraps, vehicle graphics, truck branding, van wrapping, car wrap printing Lagos, Nigeria vehicle branding, mobile advertising, fleet branding",
        "image": "vehicle-branding.jpg",
        "price": "₦5,500",
        "category": "Advertising",
        "eyebrow": "Outdoor advertising"
    },
    {
        "name": "Wedding Banners",
        "slug": "wedding-banners",
        "title": "Wedding Banners Printing | Custom Wedding Banners Lagos | Avitprint",
        "description": "Wedding banners printing in Lagos, Nigeria. Premium wedding banners with full-color printing, event banners, wedding decoration banners. Luxury wedding banner printing.",
        "keywords": "wedding banners, event banners, wedding decoration, custom banners, wedding printing Lagos, Nigeria wedding banners, premium banners, wedding signage",
        "image": "weddingRedcarpet design.jpg",
        "price": "₦200,000",
        "category": "Events",
        "eyebrow": "Special events"
    },
    {
        "name": "Branded Caps",
        "slug": "branded-caps",
        "title": "Branded Caps Printing | Custom Caps Lagos | Avitprint",
        "description": "Branded caps printing in Lagos, Nigeria. Embroidered caps, custom caps, promotional caps, various colors available. Professional cap branding services.",
        "keywords": "branded caps, custom caps, embroidered caps, promotional caps, cap printing Lagos, Nigeria caps, branded headwear, corporate caps, promotional headwear",
        "image": "Branded-Cap.jpg",
        "price": "₦6,800",
        "category": "Apparel",
        "eyebrow": "Brand apparel"
    },
    {
        "name": "Custom Keychains",
        "slug": "custom-keychains",
        "title": "Custom Keychains | Promotional Keychains Lagos | Avitprint",
        "description": "Custom keychains printing in Lagos, Nigeria. Acrylic keychains, metal keychains, rubber keychains. Durable promotional keychain printing services.",
        "keywords": "keychains, custom keychains, promotional keychains, acrylic keychains, metal keychains, keychain printing Lagos, Nigeria keychains, branded keychains",
        "image": "Keychain.jpg",
        "price": "₦2,500",
        "category": "Promotional",
        "eyebrow": "Promotional items"
    },
    {
        "name": "Presentation Folders",
        "slug": "presentation-folders",
        "title": "Presentation Folders Printing | Custom Folders Lagos | Avitprint",
        "description": "Presentation folders printing in Lagos, Nigeria. Professional folders with business card slots, custom folders, corporate folders. Premium folder printing services.",
        "keywords": "presentation folders, custom folders, corporate folders, folder printing, professional folders, folder printing Lagos, Nigeria folders, business folders",
        "image": "Presentation-Folder.jpg",
        "price": "₦9,200",
        "category": "Professional",
        "eyebrow": "Office essentials"
    },
    {
        "name": "Employee ID Cards",
        "slug": "employee-id-cards",
        "title": "Employee ID Cards Printing | PVC ID Cards Lagos | Avitprint",
        "description": "Employee ID cards printing in Lagos, Nigeria. PVC ID cards with lanyards included, custom ID cards, corporate ID cards. Professional ID card printing services.",
        "keywords": "ID cards, employee ID cards, PVC ID cards, custom ID cards, corporate ID cards, ID card printing Lagos, Nigeria ID cards, access cards, identification cards",
        "image": "id-card-printing.jpg",
        "price": "₦4,800",
        "category": "Professional",
        "eyebrow": "Office essentials"
    },
    {
        "name": "Burial Program",
        "slug": "burial-program",
        "title": "Burial Program Printing | Funeral Programs Lagos | Avitprint",
        "description": "Burial program printing in Lagos, Nigeria. Full-color burial programs, funeral programs, memorial programs. Respectful and professional program printing services.",
        "keywords": "burial programs, funeral programs, memorial programs, program printing, funeral printing Lagos, Nigeria programs, memorial stationery, funeral stationery",
        "image": "burial-program-near-me.jpg",
        "price": "₦5,200",
        "category": "Special",
        "eyebrow": "Special services"
    },
    {
        "name": "Invitations Cards",
        "slug": "invitation-cards",
        "title": "Invitation Cards Printing | Custom Invitations Lagos | Avitprint",
        "description": "Invitation cards printing in Lagos, Nigeria. Elegant invitation cards with RSVP cards, custom invitations, event invitations. Premium invitation card printing services.",
        "keywords": "invitation cards, custom invitations, event invitations, RSVP cards, invitation printing Lagos, Nigeria invitations, party invitations, formal invitations",
        "image": "invitation-card.jpg",
        "price": "₦12,500",
        "category": "Events",
        "eyebrow": "Special events"
    },
    {
        "name": "Custom Lanyards",
        "slug": "custom-lanyards",
        "title": "Custom Lanyards Printing | Lanyard Printing Lagos | Avitprint",
        "description": "Custom lanyards printing in Lagos, Nigeria. Printed lanyards with safety clips included, ID card lanyards, event lanyards. Professional lanyard printing services.",
        "keywords": "lanyards, custom lanyards, ID lanyards, event lanyards, lanyard printing, lanyard printing Lagos, Nigeria lanyards, badge lanyards, conference lanyards",
        "image": "lanyard-printing.jpg",
        "price": "₦3,800",
        "category": "Events",
        "eyebrow": "Event essentials"
    }
]

template = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="author" content="Avitprint">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="assets/styles.css">
</head>

<body class="product-detail">
    <div class="page-shell">
        <header class="site-header">
            <div class="header-strip">
                <strong>PRINT SHOP HQ</strong>
                <span>Need help? <a href="mailto:support@avitprint.com">support@avitprint.com</a></span>
            </div>
            <div class="header-main">
                <div class="brand-row">
                    <a class="logo" href="index.html">Avitprint</a>
                    <div class="header-actions">
                        <a href="products.html">All products</a>
                        <a href="about.html">About</a>
                        <a href="index.html#workflow">How we work</a>
                        <a href="mailto:sales@avitprint.com">Talk to sales</a>
                    </div>
                </div>
                <nav class="breadcrumbs" aria-label="Breadcrumb">
                    <a href="index.html">Home</a>
                    <span>&rsaquo;</span>
                    <a href="products.html">Products</a>
                    <span>&rsaquo;</span>
                    <span aria-current="page">{name}</span>
                </nav>
            </div>
        </header>

        <main>
            <section class="hero" aria-labelledby="product-title">
                <div class="media-stack">
                    <div class="media-card">
                        <img src="assets/images/products/{image}" alt="{name} printing Lagos Nigeria, custom {name.lower()} with full-color printing">
                    </div>
                    <div class="media-thumbs" aria-label="{name} thumbnails">
                        <img src="assets/images/products/{image}" alt="Custom {name.lower()} design examples" class="media-thumb">
                        <img src="assets/images/products/{image}" alt="Premium {name.lower()} printing quality" class="media-thumb">
                        <img src="assets/images/products/{image}" alt="Professional {name.lower()} close-up view" class="media-thumb">
                        <img src="assets/images/products/{image}" alt="{name} in use for branding and marketing" class="media-thumb">
                    </div>
                    <div class="swatch-row" aria-label="Popular color swatches">
                        <span class="swatch"></span>
                        <span class="swatch"></span>
                        <span class="swatch"></span>
                        <span class="swatch"></span>
                    </div>
                </div>
                <div class="hero-content">
                    <p class="eyebrow">{eyebrow}</p>
                    <h1 id="product-title">{name}</h1>
                    <p>Professional {name.lower()} printing services in Lagos, Nigeria. High-quality custom {name.lower()} with vibrant full-color printing. Perfect for businesses, events, and promotional campaigns. Fast delivery and competitive pricing.</p>
                    <ul class="selling-points">
                        <li><span>&#10003;</span>Premium quality materials and printing</li>
                        <li><span>&#10003;</span>Full-color CMYK printing available</li>
                        <li><span>&#10003;</span>Custom designs and branding options</li>
                        <li><span>&#10003;</span>Ready in 48-72hrs, rush service available</li>
                    </ul>
                </div>
            </section>

            <section class="section" id="quote">
                <h2>Get a custom quote</h2>
                <p>Fill out the form below and our team will send you a detailed quote with pricing, timelines, and recommendations within 3 business hours.</p>
                <div class="order-panel" style="max-width: 600px; margin: 0 auto;">
                    <form action="mailto:sales@avitprint.com" method="post" enctype="text/plain" onsubmit="return handleQuoteSubmit(event)">
                        <div style="display: grid; gap: 18px;">
                            <div>
                                <label for="quote-name" style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Full Name *</label>
                                <input type="text" id="quote-name" name="name" required style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1px solid #e8e8f5; font-size: 14px; font-family: inherit;">
                            </div>
                            <div>
                                <label for="quote-email" style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Email Address *</label>
                                <input type="email" id="quote-email" name="email" required style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1px solid #e8e8f5; font-size: 14px; font-family: inherit;">
                            </div>
                            <div>
                                <label for="quote-phone" style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Phone Number *</label>
                                <input type="tel" id="quote-phone" name="phone" required style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1px solid #e8e8f5; font-size: 14px; font-family: inherit;">
                            </div>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                                <div>
                                    <label for="quote-quantity" style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Quantity *</label>
                                    <select id="quote-quantity" name="quantity" required style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1px solid #e8e8f5; font-size: 14px; font-family: inherit; background: #fff;">
                                        <option value="">Select quantity</option>
                                        <option value="100">100 units</option>
                                        <option value="250">250 units</option>
                                        <option value="500">500 units</option>
                                        <option value="1000">1,000 units</option>
                                        <option value="2000">2,000+ units</option>
                                    </select>
                                </div>
                                <div>
                                    <label for="quote-options" style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Options *</label>
                                    <select id="quote-options" name="options" required style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1px solid #e8e8f5; font-size: 14px; font-family: inherit; background: #fff;">
                                        <option value="">Select option</option>
                                        <option value="standard">Standard</option>
                                        <option value="premium">Premium</option>
                                        <option value="custom">Custom</option>
                                    </select>
                                </div>
                            </div>
                            <div>
                                <label for="quote-message" style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Additional Details</label>
                                <textarea id="quote-message" name="message" rows="4" placeholder="Tell us about your design requirements, delivery location, or any special requests..." style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1px solid #e8e8f5; font-size: 14px; font-family: inherit; resize: vertical;"></textarea>
                            </div>
                            <div>
                                <label for="quote-design" style="display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px;">Upload Design Files</label>
                                <input type="file" id="quote-design" name="design" accept=".pdf,.ai,.psd,.jpg,.jpeg,.png,.eps,.indd" multiple style="width: 100%; padding: 12px 16px; border-radius: 12px; border: 1px solid #e8e8f5; font-size: 14px; font-family: inherit; background: #fff; cursor: pointer;">
                                <p style="margin: 8px 0 0; font-size: 12px; color: #6b7280;">
                                    Accepted formats: PDF, AI, PSD, JPG, PNG, EPS, INDD. You can select multiple files. Please attach them in your email client when the email opens.
                                </p>
                            </div>
                            <button type="submit" class="btn-primary" style="width: 100%; padding: 14px 22px; border-radius: 12px; font-size: 15px; font-weight: 600; cursor: pointer; border: none; background: #6c5ce7; color: #fff; box-shadow: 0 14px 32px rgba(108, 92, 231, 0.35);">
                                Request Quote
                            </button>
                            <p style="margin: 0; font-size: 12px; color: #6b7280; text-align: center;">
                                We'll respond within 3 business hours with a detailed quote.
                            </p>
                        </div>
                    </form>
                </div>
            </section>

            <section class="section" id="specs">
                <h2>Specifications</h2>
                <div class="feature-grid">
                    <article class="spec-card">
                        <h3>Materials</h3>
                        <p>Premium quality materials selected for durability and professional appearance. Various material options available based on your needs.</p>
                    </article>
                    <article class="spec-card">
                        <h3>Print quality</h3>
                        <p>Full-color CMYK printing with 300 DPI resolution. Vibrant colors that remain fade-resistant and professional.</p>
                    </article>
                    <article class="spec-card">
                        <h3>Customization</h3>
                        <p>Fully customizable designs, sizes, and finishes. We work with your brand guidelines to create the perfect product.</p>
                    </article>
                    <article class="spec-card">
                        <h3>File requirements</h3>
                        <p>PDF, AI, or PSD files preferred. Minimum 300 DPI resolution. CMYK color mode. Our team can help with file preparation.</p>
                    </article>
                </div>
            </section>

            <section class="section" id="related-products">
                <h2>Other products you might like</h2>
                <div class="feature-grid">
                    <article class="feature-card">
                        <div class="related-product-image">
                            <img src="assets/images/products/business-card.jpg" alt="Business cards printing">
                        </div>
                        <h3>Business Cards</h3>
                        <p>Pair your {name.lower()} with premium business cards for complete branding packages.</p>
                        <a href="product-detail-business-cards.html">View business cards &rarr;</a>
                    </article>
                    <article class="feature-card">
                        <div class="related-product-image">
                            <img src="assets/images/products/flyer-printing-in-lagos.jpg" alt="Flyers printing">
                        </div>
                        <h3>Custom Flyers</h3>
                        <p>High-impact flyers that complement your {name.lower()} campaigns.</p>
                        <a href="product-detail-flyers.html">View flyers &rarr;</a>
                    </article>
                    <article class="feature-card">
                        <div class="related-product-image">
                            <img src="assets/images/products/stickers.jpg" alt="Stickers printing">
                        </div>
                        <h3>Custom Stickers</h3>
                        <p>Durable waterproof stickers perfect for reinforcing your brand message.</p>
                        <a href="product-detail-stickers.html">View stickers &rarr;</a>
                    </article>
                    <article class="feature-card">
                        <div class="related-product-image">
                            <img src="assets/images/products/brochures.jpg" alt="Brochures printing">
                        </div>
                        <h3>Brochures</h3>
                        <p>Tri-fold and bi-fold brochures for detailed product information.</p>
                        <a href="products.html">View brochures &rarr;</a>
                    </article>
                </div>
            </section>

            <section class="section" id="faqs">
                <h2>Frequently asked</h2>
                <div class="feature-grid">
                    <article class="faq-item">
                        <h3>Can you help design the {name.lower()}?</h3>
                        <p>Yes. Our in-house designers can create concepts from brief or polish your existing layout. Design starts from &#8358;15,000.</p>
                    </article>
                    <article class="faq-item">
                        <h3>What's the minimum order quantity?</h3>
                        <p>Minimum order is typically 100 units. For smaller quantities, please contact us for a custom quote.</p>
                    </article>
                    <article class="faq-item">
                        <h3>Do you offer rush delivery?</h3>
                        <p>Yes. Rush delivery available for urgent orders. Standard delivery is 48-72 hours in Lagos, 3-5 days nationwide.</p>
                    </article>
                    <article class="faq-item">
                        <h3>Where do you deliver?</h3>
                        <p>Nationwide delivery via courier partners. Lagos pickup is free. We can also coordinate bulk distribution services.</p>
                    </article>
                    <article class="faq-item">
                        <h3>Can I see a proof before printing?</h3>
                        <p>Yes. We provide digital proofs for approval before production. Physical samples available for large orders.</p>
                    </article>
                    <article class="faq-item">
                        <h3>What payment methods do you accept?</h3>
                        <p>We accept bank transfers, card payments, and cash on delivery (Lagos only). Payment terms available for large orders.</p>
                    </article>
                </div>
            </section>

            <section class="section" id="cta">
                <div class="cta-banner">
                    <h2>Ready to print {name.lower()} that make an impact?</h2>
                    <p>Share your artwork or campaign goals and our team will send pricing, timelines, and print recommendations within 3 business hours.</p>
                    <a href="mailto:sales@avitprint.com">Start your order</a>
                </div>
            </section>
        </main>

        <footer class="site-footer">
            <div class="footer-brand">Avitprint</div>
            <p>All-in-one print partner for marketing teams, hospitality brands, and fast growing startups.</p>
            <ul class="footer-nav">
                <li><a href="index.html">Home</a></li>
                <li><a href="products.html">Products</a></li>
                <li><a href="product-detail-{slug}.html" aria-current="page">{name}</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="index.html#resources">Resources</a></li>
                <li><a href="index.html#workflow">FAQs</a></li>
            </ul>
            <div class="footer-grid">
                <div>
                    <strong>Talk to us</strong>
                    <a href="mailto:support@avitprint.com">support@avitprint.com</a>
                    <a href="tel:+12894367868">+1 289 436 7868</a>
                    <span>Lagos, Nigeria</span>
                </div>
                <div>
                    <strong>Follow</strong>
                    <div class="socials">
                        <a href="https://facebook.com/avitprint" target="_blank" rel="noopener noreferrer">Fb</a>
                        <a href="https://instagram.com/avitprint" target="_blank" rel="noopener noreferrer">Ig</a>
                        <a href="https://twitter.com/avitprint" target="_blank" rel="noopener noreferrer">Tw</a>
                        <a href="https://linkedin.com/company/avitprint" target="_blank" rel="noopener noreferrer">In</a>
                    </div>
                </div>
            </div>
            <p class="footer-note">&copy; 2024 - 2025 Avitprint. All rights reserved.</p>
        </footer>
    </div>
    <script src="assets/scripts.js"></script>
    <script>
        function handleQuoteSubmit(event) {{
            event.preventDefault();
            var name = document.getElementById('quote-name').value;
            var email = document.getElementById('quote-email').value;
            var phone = document.getElementById('quote-phone').value;
            var quantity = document.getElementById('quote-quantity').value;
            var options = document.getElementById('quote-options').value;
            var message = document.getElementById('quote-message').value;
            var designFiles = document.getElementById('quote-design').files;
            
            var subject = '{name} Quote Request - ' + quantity + ' units (' + options + ')';
            var body = 'Name: ' + name + '%0D%0A' +
                      'Email: ' + email + '%0D%0A' +
                      'Phone: ' + phone + '%0D%0A' +
                      'Quantity: ' + quantity + ' units%0D%0A' +
                      'Options: ' + options + '%0D%0A';
            
            if (message) {{
                body += 'Additional Details: ' + encodeURIComponent(message) + '%0D%0A';
            }}
            
            if (designFiles.length > 0) {{
                body += '%0D%0A--- Design Files ---%0D%0A';
                for (var i = 0; i < designFiles.length; i++) {{
                    body += 'File ' + (i + 1) + ': ' + designFiles[i].name + '%0D%0A';
                }}
                body += '%0D%0ANote: Please attach the design files to this email before sending.%0D%0A';
            }}
            
            window.location.href = 'mailto:sales@avitprint.com?subject=' + encodeURIComponent(subject) + '&body=' + body;
            return false;
        }}
    </script>
</body>

</html>'''

# Generate pages
for product in products:
    filename = f"product-detail-{product['slug']}.html"
    content = template.format(**product)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {filename}")

print(f"\nGenerated {len(products)} product detail pages successfully!")

