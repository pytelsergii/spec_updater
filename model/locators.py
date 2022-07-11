from selenium.webdriver.common.by import By

locators = {
    'jysk.ua': {
        'name': (By.CSS_SELECTOR, 'div.product-name-sku span.product-name'),
        'image': (By.CSS_SELECTOR, 'img.img-responsive.carousel-image'),
        'price': (By.CSS_SELECTOR, 'span.ssr-product-price__value')
    },
    'shoploft.com.ua': {
        'name': (By.CSS_SELECTOR, 'h1.product_information_title'),
        'image': (By.CSS_SELECTOR, 'div.product span.product__img img'),
        'price': (By.CSS_SELECTOR, 'div.product_information_price span.current_price')
    },
    'his.ua': {
        'name': (By.CSS_SELECTOR, 'div.product_layout_info h1.name span'),
        'image': (By.CSS_SELECTOR, 'div.product_big_slideshow_img img'),
        'price': (By.CSS_SELECTOR, 'span#product_price')
    },
    'home-club.com.ua': {
        'name': (By.CSS_SELECTOR, 'div.product-name h1'),
        'image': (By.CSS_SELECTOR, 'img.cloudzoom'),
        'price': (By.CSS_SELECTOR, 'div.product-price span')
    },
    'bt.rozetka.com.ua': {
        'name': (By.CSS_SELECTOR, 'h1.product__title'),
        'image': (By.CSS_SELECTOR, 'img.picture-container__picture'),
        'price': (By.CSS_SELECTOR, 'p.product-prices__big')
    }
}
