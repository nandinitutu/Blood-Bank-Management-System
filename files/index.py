import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
    <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="icon" href="img/titlelogo.png">
    <meta name="viewport" content="width=device-width, maximum-scale=1.0, user-scalable=no">
    <meta name="format-detection" content="telephone=no">
    <link rel="preconnect" href="https://static3.jdomni.in">
    <link rel="dns-prefetch" href="https://static1.jdomni.in">
    <link rel="dns-prefetch" href="https://static2.jdomni.in">
    <link rel="dns-prefetch" href="https://static3.jdomni.in">
    <link rel="dns-prefetch" href="https://image1.jdomni.in">
    <link rel="dns-prefetch" href="https://image2.jdomni.in">
    <link rel="dns-prefetch" href="https://image3.jdomni.in">
    <link rel="dns-prefetch" href="https://api1.jdomni.com">
    <link rel="dns-prefetch" href="https://api2.jdomni.com">
    <link rel="dns-prefetch" href="https://api3.jdomni.com">
    <link rel="dns-prefetch" href="&ZeroWidthSpace;https://fonts.gstatic.com">
    <meta property="og:image" content="https://image1.jdomni.in/defaultogimages/v2/S/L/SL.png">
    <meta property="og:image:width" content="200"><meta property="og:image:height" content="200">
    <meta property="og:type" content="company">
    <meta property="og:site_name" content="Safe Life Blood Banks">
    <title class="notranslate">Blood Bank Management System</title>
    <meta name="twitter:card" content="summary">
    <meta name="title" content="Safe Life Blood Banks - 404">
    <meta property="og:title" content="Safe Life Blood Banks - 404">
    <meta name="twitter:title" content="Safe Life Blood Banks - 404">
    <meta property="og:url">
    <style id="colourscheme">
        body 
        .theme-bg-color{background:#fff !important}body.web-theme-background{}body.jd-webp.web-theme-background{}body.wap.jd-webp.web-theme-background{}body
        .btmblk.webheader.header-content,body
         .custom-template,body .footer-container,
         .wap .footer-main,body 
         .edit-content,body 
         .mobileHeaderBlock,body.wap 
         .sticky-footer{font-family:Gilroy !important;font-weight:400 !important}body 
         .custom-template.global-block-padding{padding-top:45px;padding-bottom:45px}body.wap 
         .custom-template.global-block-padding{padding-top:30px;padding-bottom:30px}.webheader{background-color:rgba(255,255,255,0) 
         !important}.webheader-color{color:rgba(255,255,255,0) !important}.store-name-color{color:#bf2f2f !important}.social-icon{color:#333 !important}.social-icon:hover{color:#bf2f2f !important}.signupLogin 
         .signupLoginModal .left-section.webheader,.bookAppointment .calendar-container .webheader{background-color:#fff !important}.signupLogin .signupLoginModal .logo-section .shortNameContainer .store-initial-color{color:#fff !important}.signupLogin 
         .signupLoginModal .logo-text-section .logo-heading.store-name-color,.signupLogin .signupLoginModal .logo-text-section .logo-txt.store-name-color{color:#bf2f2f !important}body.IPad .social-icon:hover{color:#333 !important}.header-btn{color:#333 !important}.header-btn:hover{text-decoration:underline 
         !important}.header-icon{color:#333 !important}.partition-color{border-top:1px solid !important}.store-bg-color{background-color:#9e1515 !important}.header-block .store-bg-color{border-color:#bb131a !important}.header-block .userAccount-wrapper 
         .my-account-pop-up .list-item:hover{background:#bb131a !important;color:#fff !important}.header-block .userAccount-wrapper 
         .my-account-pop-up .list-item:hover .myAccountText{color:#fff !important}.header-block .userAccount-wrapper 
         .my-account-pop-up.popover.bottom>.arrow:after{border-bottom-color:#fff !important}.header-block .userAccount-wrapper 
         .my-account-pop-up,.header-block .userAccount-wrapper .my-account-pop-up .list-item{background:#fff !important}.header-block 
         .userAccount-wrapper .my-account-pop-up .list-item .myAccountText{color:#bb131a !important}.store-initial-color{color:#fff !important}.search-bg-color{border:1px solid 
         !important}.search-icon-color{}.search-icon-color:hover{}.search-bg-color:hover .search-icon-color{}.search-button .srch-btn-text{}.search-button:hover .srch-btn-text{}.webheader.header-content .header-block:not(.coverImageHeader) 
         .header-custom-template{background-color:rgba(255,255,255,0)}.webheader.logo-canvas{background-color:rgba(255,255,255,0) !important;background-color:#fff !important}.leaflet-map-pane 
         .leaflet-popup .leaflet-popup-content-wrapper,.getdirections.store-bg-color,.signupLogin .signupLoginModal 
         .logo-section .shortNameContainer.store-bg-color{background:#9e1515 !important}.leaflet-map-pane 
         .leaflet-popup .leaflet-popup-content-wrapper .leaflet-outlet-name,.leaflet-map-pane .leaflet-popup 
         .leaflet-popup-content-wrapper .leaflet-outlet-area,.getdirections.store-initial-color{color:#fff !important}.web-theme-background 
         .webheader.header-content.no-cover-part .first-second-block{background-image:none;background-color:#fff}.home 
         .webheader.header-content .first-second-block{background-image:linear-gradient(-180deg, rgba(255,255,255,0) 14%, rgba(0,0,0,0) 94%) !important}.webheader.header-content:not(.header-sticky):not(.no-cover-part) .coverImageHeader .first-second-block{background-color:rgba(255,255,255,0) !important;
         background-image:none !important}.header-content.header-sticky .coverImageHeader 
         .first-second-block{background-image:none !important;background-color:#fff !important}.header-top-color{background-color:rgba(191,47,47,0) !important}.webheader.header-content:not(.no-cover-part) 
         .header-block.coverImageHeader .header-custom-template{background-color:rgba(0,0,0,0) !important}.header-middle-color{background-color:rgba(255,255,255,0) !important}.header-block.machinery3 
         .third-block{background-color:rgba(255,255,255,0) !important}.search-bg-color:hover{border:1px solid !important}.cart-brder-color{border:1px solid !important}.cart-txt-icon{}.cart-cnt-bg{}.cart-bttn-bg{cursor:pointer}.cart-bttn-bg:hover{cursor:pointer}.cart-bttn-bg:hover .header-icon.cart-btn-icon{}.cart-bttn-bg:hover 
         .cart-txt-pos.cart-txt-icon{}.webheader .cart-btn-icon,.webheader .cart-icon{}.cart-btn-icon:hover{}.cart-txt-icon:hover{}.cart-brder-color.cart-bttn-bg:hover .dta.search-scroll-bg.search-scroll-icon.cart-cnt-bg{}.cart-count-val{}.cart-brder-color.cart-bttn-bg:hover .cart-count-val{}.cart-brder-color:hover{border:1px solid !important}.category-header-color{color:#3c4144 !important}.sub-category-hover:hover,.sub-category-hover:active{color:#ab62ef !important}.header-block.header-block.machinery3 .third-block .burger-menu-wrapper.setHoverBackground,#content_wrapper 
         .leftnavOverlay #leftNavMenuRevamp{background-color:#fff !important}.user-submenu-icon{color:#bb131a !important}.header-block .userAccount-wrapper .my-account-pop-up .list-item:hover .icon-style,.user-submenu-icon:hover{color:#fff9f9 !important}.header-block:not(.grocery):not(.machinery3) .burger-menu-wrapper:hover .menuIconBar.whiteBack,.header-block:not(.grocery):not(.machinery3) .burger-menu-wrapper:hover .transparent-div,.header-block:not(.grocery):not(.machinery3) .burger-menu-wrapper.setHoverBackground .menuIconBar.whiteBack,.header-block:not(.grocery):not(.machinery3) 
         .burger-menu-wrapper.setHoverBackground .transparent-div{background-color:#fff !important}#leftNavMenuRevamp .leftNavWrapperRevamp .leftNavigationLeftContainer ul li.navlink:hover{background-color:#bb131a !important}.menuLink-color{color:#333 !important}.menuLink-color:hover{color:#bf2f2f !important}.header-block.grocery .menulink-with-popover.popoverOpen{}.menulink-with-popover.popoverOpen .menuLink-color,.menuLink-color:hover>a,.menuLink-color:hover>i{color:#bf2f2f !important;text-decoration:none}.menuLink-color:hover ~ i{color:#bf2f2f !important;text-decoration:none}.border-separator{}.user-icon-color{color:#333 !important}.searchBar-border:focus{}.searchBar-border{}.searchBar-text,.searchBar-text:focus{}.searchBar-cross{}.searchBar-bg{}.searchBar-bg:focus{}.category-burger-menu{color:#333 !important}@media (min-width: 768px){.category-burger-menu:hover,.menuIconBar.whiteBack .category-burger-menu{color:#bf2f2f !important}}.burger-menu-wrapper{color:#333 !important;}.header-block.grocery .burger-menu-wrapper:hover,.burger-menu-wrapper .menuIconBar:hover,.burger-menu-wrapper.setHoverBackground{color:#bf2f2f !important;}.burger-menu-wrapper.setHoverBackground .webheader-color.category-burger-menu{color:#bf2f2f !important}.burger-menu-wrapper .cat-text,.burger-menu-wrapper .category-burger-menu{color:inherit !important}.default-text-color{color:#333 !important}.header-content .header-block.machinery3 .first-block .right-sec .default-text-color:hover,.default-text-color:hover,.contactUs:hover .default-text-color,.default-text-color:hover .default-text-color{color:#bf2f2f !important}.header-content .header-block.machinery3 .first-block .right-sec .default-icon-color:hover,.default-text-color:hover .default-icon-color,.contactUs:hover .default-icon-color,.default-icon-color:hover{color:#bf2f2f !important}.default-text-color:hover .links-text{text-decoration:None !important}.header-block .signup-login-btn-div:hover .sign-up-login-btn,.header-block .my-account-holder:hover .welcome-text-span{text-decoration:None !important}.header-block .pageLink .track-order.menuLink-color:hover:not(#moreMenuLink),.header-block .pageLink:hover .track-order.menuLink-color:not(#moreMenuLink),.header-block .pageLink .track-order.menuLink-color:hover .header-more-txt:not(.icon-pagination-down),.header-block .pageLink:hover .track-order.menuLink-color .header-more-txt:not(.icon-pagination-down){text-decoration:None !important}.default-icon-color{color:#333 !important}.category-menu:hover{color:#fff !important}.cart-border-line{border-color:rgba(191,47,47,0) !important}.menuLink-background{}.child-menuLink-background{background-color:#fff !important}.child-menuLink-background .arrow:after{border-bottom-color:#fff !important}.child-menuLink-hover:hover{background-color:#bb131a !important}.child-menuLink-hover:hover>a,.child-menuLink-hover:hover>i,.child-menuLink-hover:hover>.icon-wrapper{color:#fff !important}.child-menuLink-color{color:#4d4d4d !important}.child-menuLink-color:hover{color:#fff !important}.login-signup-color{color:#333 !important}.my-account-div:hover .login-signup-color,.login-signup-color:hover{color:#bf2f2f !important}.login-signup-separator:hover,.login-signup-separator{color:#333 !important}.fake-login-signup-divider{color:#333 !important}.header-block .search-text-box::-webkit-input-placeholder,.header-block input.dummy-input{font-weight:300}.navlink.see-all-cat .menuLinks .catText,.navlink.see-all-cat .menuLinks i{color:#3d3d3d !important}.navlink.see-all-cat .menuLinks:hover .catText,.navlink.see-all-cat .menuLinks:hover i{color:#fff !important}.navlink .menuLinks .catText{color:#3d3d3d !important}.navlink .menuLinks:hover .catText{color:#fff !important}.header-sticky .header-block.grocery .burger-menu-wrapper .menuIconBar.whiteBack .icon-menu{}.header-block.grcocery .list-item:hover{color:#fff !important}.header-block.grocery .userAccount-wrapper .signup-login-btn-div .default-text-color:hover{color:#fff !important}.header-block.grocery .menuDropdown .menuLink-color:hover{background-color:transparent !important}.header-block.grocery .list-item:hover{color:#fff !important}.header-block.grocery .menuLink-color:hover{}.header-block.grocery .cart-btn-wrapper.cart-border-line{}.header-block.furniture .list-item:hover{color:#fff !important}.header-block.furniture .userAccount-wrapper .signup-login-btn-div .default-text-color:hover{color:#fff !important}.header-block.furniture .menuLink-color:hover{border-color:#bf2f2f !important}.header-block.furniture .menuLink-color.parent-menulink:hover{border-color:#bf2f2f !important}.header-block.apparel .list-item:hover{color:#fff !important}.header-block.apparel .userAccount-wrapper .signup-login-btn-div .default-text-color:hover{color:#fff !important}.wap-header-bg-color,body.wap .omni-header.webheader,body.wap .omni-header.webheader .custom-template.mobile-header,.wap .omni-left-panel-container .section-login-signup .shortNamePosition,.wap .signUpModal .user-initials-wrapper{background-color:rgba(255,255,255,0) !important}.mobileheader{background-color:rgba(255,255,255,0) !important;background-color:#fff !important}.wap .social .category-tags{background-color:#fff !important}.social .all-caught-up .icon-style{color:#fff !important}.wap .social .category-tag .category-name{color:#333 !important}.wap .social .category-tag.active .category-name{color:#fff !important}.wap .social .category-tags .background-div{background-color:#333 !important}.wap .menu-link-modal-header,.section-user-options .edit-menu-btn-holder{background-color:#fff !important}body.wap .omni-header.webheader.homepage-hdr .coverImageHeader .custom-template.mobile-header,body.wap .omni-header.webheader .coverImageHeader .omni-header.webheader{background-color:rgba(0,0,0,0) !important}body.wap .omni-header.webheader.homepage-hdr .coverImageHeader .main-outer{background-image:none !important;background-color:rgba(255,255,255,0) !important}html.desktop body:not(.home) .webheader.homepage-hdr .header-block.coverImageHeader,html.desktop .webheader:not(.homepage-hdr) .header-block.coverImageHeader{background-color:#fff}body.wap .omni-header.webheader:not(.homepage-hdr) .coverImageHeader .custom-template.mobile-header,.wap.omniBasics .omni-header.webheader .coverImageHeader .custom-template.mobile-header,body.wap.sticky-omniheader .omni-header.webheader .coverImageHeader .main-outer,body.wap.fixed-omniheader .omni-header.webheader .coverImageHeader .main-outer{background-image:none !important;background-color:#fff !important}body.wap.delivery-address .omni-header.webheader .sub-header-text{color:#333 !important}body.wap .order-summary #calendarDateTimeModal .modal-header{background:#fff;color:#333;opacity:1}body.wap .order-summary #calendarDateTimeModal .modal-header .back,body.wap .order-summary #calendarDateTimeModal .modal-header .modal-title,body.wap .order-summary #calendarDateTimeModal .modal-header .modal-subtitle{color:#333}.header-block.mobile .userAccount-wrapper{}.header-block.machinery2 .header-top-color{background-color:rgba(255,255,255,0) !important}.webheader .header-block.machinery2{border-top-color:rgba(191,47,47,0);border-bottom-color:rgba(191,47,47,0)}.child-menuLink-background:hover ~ .moreLink.menuLink-color a{color:#bf2f2f !important;text-decoration:none}.header-block.machinery2 .menulist-container .menuLink-color:hover::before{border-color:#bf2f2f !important}.header-block.machinery2 
         .menulist-container .moreLink.menuLink-color #moreTextId:before{border-bottom:2px solid #bf2f2f !important}.header-content .header-block.machinery3 .first-block .right-sec.location-holder .default-text-color,.header-block.machinery3 .first-block .right-sec .default-text-color{}.header-content .header-block.machinery3 .first-block .right-sec.location-holder .default-icon-color,.header-block.machinery3 .first-block .right-sec .default-icon-color{}.header-content .header-block.machinery3 .first-block .right-sec.location-holder .default-text-color:hover,.header-block.machinery3 .first-block .right-sec .default-text-color:hover{}.header-content .header-block.machinery3 .first-block .right-sec.location-holder .default-icon-color:hover,.header-block.machinery3 .first-block .right-sec .default-icon-color:hover{}.header-block.machinery3 .second-block .account-info-sec .default-text-color{}.header-block.machinery3 .second-block .account-info-sec .default-text-color:hover{}.header-block.machinery3 .second-block .account-info-sec .default-icon-color{}.header-block.machinery3 .second-block .account-info-sec .default-icon-color:hover{}.header-block.machinery2 .header-center .menu-list-holder{border:none}.header-block:not(.coverImageHeader) .header-center .menu-list-holder,.header-block.machinery3 .third-block .header-center .leftLink-outerDiv,.header-block.machinery3 .third-block .header-center .rightLink-outerDiv{border-bottom:1px solid !important}.header-block.machinery3 .third-block .header-center .leftLink-outerDiv,.header-block.machinery3 .third-block .header-center .rightLink-outerDiv{border-bottom:1px solid !important;border-top:1px solid !important}.header-block.machinery3 .user-icon-color{}.phone-icon-color{color:#333 !important}.customise-header .preview .user-icon-color{color:#333 !important}.wap-header-icon-color,.wap .main-outer .cart-icon,.wap .main-outer .category-burger-menu i,.wap .main-outer .back-btn i,.wap .main-outer .omni-burger i,.wap .main-outer .cross-icon i,.wap .main-outer .omni-control-search i,.wap .omni-left-panel-container .section-login-signup .my-account,.wap .omni-left-panel-container .user-login-link,.wap .menu-link-modal-header .heading,.wap .menu-link-modal-header .icon-close-thin,.section-user-options .selection-btn,.omni-left-panel .section-login-signup,.wap .omni-left-panel-container .section-login-signup .right-arrow-fonts,.wap .slider-icon{color:#333 !important}.background-phone-icon-color{background-color:#333 !important}.coverImageHeader .mobile-header .user-initials-wrapper{background-color:#fff !important}.mobile-header .user-initials-wrapper{color:#333 !important;background-color:#fff !important}.section-user-options .selection-btn,.wap .omni-left-panel-container .section-login-signup .shortNamePosition{border-color:#333 !important}.wap .main-outer .content-text,.wap .signUpModal .user-initials-wrapper{color:#bf2f2f !important}.header-block .profile-icon{}.my-account-div:hover .my-account-popup .profile-icon,.signup-login-btn-div:hover .login-icon-holder .profile-icon{}body.wap .verify-mobile .mob-no .warning-btn.disabled,body.wap .order-summary .cnfrmwp .cnfrmbtn.disabled,body.wap .mdyadrs .cnfrmwp .cnfrmbtn.disabled{background-color:#cfcfcf;color:#FFF;cursor:default;opacity:1}.omni-header .header-block .custom-template .srchbarwp input::-webkit-input-placeholder,.omni-header .header-block .custom-template .srchbarwp input::placeholder,.omni-header .header-block .custom-template .srchbarwp input.dummy-input,.omni-header .header-block .custom-template .srchbarwp .search-bar .srchicnwp.icons-block .search-icon{color:#788288 !important}.omni-header .header-block .custom-template .srchbarwp .search-bar{border-color:#EAEAEA !important;background-color:#fff !important}.omni-header .header-block .custom-template .srchbarwp .search-bar .icons-block .icon-barcode,.omni-header .header-block .custom-template .srchbarwp .search-bar .icons-block .icon-microphone,.omni-header .header-block .custom-template .srchbarwp .search-bar .icons-block .icon-GlList{color:#747474 !important}.header-block .defaultLink-wrapper .store-Outlet:hover .iconLocation{color:#bf2f2f}.header-block .defaultLink-wrapper .store-Outlet:hover .store-name-color{color:#bf2f2f}.omni-left-panel .section-login-signup,.omni-left-panel .section-login-signup:active{background-color:#fff !important}.second-partition-solid{background-color:#fff !important}.footer-background{background:#fff !important}.footer-basics .more-popover{background-color:#fff !important}.shop-footer .text-color{color:#BF2F2F !important}.shop-footer .divider{border-bottom:1px solid #fff !important}.shop-footer .store-bg-color{background:#BF2F2F !important}.shop-footer .store-initial-color{color:#fff !important}.shop-footer .store-name-color{color:#BF2F2F !important}.footer-main .b2b-lessmore a,.footer-main .footer-sec .sh-more-useful-links a,.footer-main .footer-sec .social-sec a:hover,.footer-basics .icon-pagination-down:focus,.footer-basics a:focus,.footer-basics a:focus,.footer-basics .expand-links:hover span{color:#F95252 !important}.footer-links .parent-menulink a:hover ~ i{color:#F95252 !important}.footer-links .parent-menulink:hover>a,.footer-links .parent-menulink:hover>i{color:#F95252 !important}.footer-options .parent-menulink a:hover ~ i,.footer-options a:hover{color:#F95252 !important}.footer-options.parent-menulink .popover a:hover{color:#F95252 !important}.footer-basics .menuDropdown li:hover>a,.footer-basics .menuDropdown li:hover>i{color:#F95252 !important}.footer-basics .menuDropdown li a{color:#BF2F2F !important}.wap .footer-basics .footer-options-cnt .footer-options{border-right:1px solid #fff}.shop-footer .social-sec.wrap-icons .sprite_new{color:#BF2F2F !important}.shop-footer .social-sec.wrap-icons .sprite_new:hover{color:#F95252 !important}.footer-child-menu-background{background-color:#fff !important}.shop-footer .more-popover{background-color:#fff !important}.footer-child-menu-background.top .arrow:after,.more-popover.top .arrow:after{border-top-color:#fff !important}.footer-child-menu-background.right .arrow:after{border-right-color:#fff !important}.footer-child-menu-color{color:#BF2F2F !important}.footer-child-menu-color:hover{color:#F95252 !important}.footer-basics .menuDropdown li:hover{background-color:#fff !important}.footer-child-background-hover:hover{background-color:#fff !important}.footer-child-background-hover:hover>a{color:#F95252 !important}.footer-language-section{background-color:#BF2F2F !important}.shop-footer .lang-change{color:#fff}.shop-footer .language-div .change-lang{color:#fff !important}.shop-footer .language-div .lang-change.selected-lang{color:#fff !important}#topcontrol{background-color:#BF2F2F !important}.wap #JDvoice_search .mic-icon-holder-inner svg g rect{fill:#fff}.product-name-price-details .enquire-tab.active,.product-name-price-details .buy-online-tab.active{border-top-color:#bb131a !important;color:#bb131a !important}.product-name-price-details .enquire-tab:not(.active),.product-name-price-details .buy-online-tab:not(.active){border-bottom-color:#bb131a !important}.product-name-price-details .buy-online-tab{border-right-color:#bb131a !important}.primary-btn-color-non-imp{background-color:#bb131a}.primary-btn-color-imp{background-color:#bb131a !important}.notification-container .primary-btn-color-non-imp{background-color:#bb131a}.primary-btn-psuedo-with-brd::after{background-color:#bb131a;border-color:#bb131a}.primary-btn-brd::after{border-color:#bb131a}.primary-btn-color,.primary-btn-color-opaque,.btn.primary-btn-color,body.wap .btn.primary-btn-color,.send_enquiry_btn.primary-btn-color,.enquiryForm .send-enquiry.primary-btn-color,.wap .listing-outerDiv .add-to-cart.primary-btn-color{background-color:#bb131a;color:#fff;outline-color:transparent;transition:0.3s}.primary-btn-color:focus,.btn.primary-btn-color:focus{color:#fff}.primary-color-border,.product-btn .primary-color-border{border-color:#bb131a}.custom-template .primary-btn-color{border-style:solid;border-color:#bb131a}.primary-btn-color .loading-span{border-color:#fff;border-top-color:transparent}.button-component .loader-svg-holder .circle,.full-width-button circle{stroke:#fff !important}.tertiary-btn-color .loading-span{border-color:#bb131a;border-top-color:transparent}.secondary-btn-color .loading-span{border-color:#fff;border-top-color:transparent}.wap .quantity-change-div{border-color:#bb131a}.quantity-change-div .loading-span,.qty-up-down .loading-span{border-color:#bb131a;border-top-color:transparent}.primary-btn-color-opaque{background-color:#bb131a}.social .category-section .category-name-color{color:#ca2121}.secondary-btn-color,.btn.secondary-btn-color{background-color:#bb131a;color:#fff;border-color:#bb131a;outline-color:transparent;transition:0.3s}.template-main-container .secondary-btn-color,.template-main-container .btn.secondary-btn-color{font-family:Gilroy;font-style:normal;text-decoration:none;font-size:14px;border-width:1px;line-height:normal;letter-spacing:normal}.floatCartButton .cart-txt-icon,.floatCartButton:hover .cart-btn-icon,.webheader .floatCartButton .cart-btn-icon,.webheader .floatCartButton .cart-icon{color:#fff !important}.floatCartButton .cart-cnt-bg.cart-count-val{background-color:#fff !important}.floatCartButton .cart-cnt-bg .cart-count-val{color:#bb131a !important}.emptycart .cart-emptyBx .cont-shop button.tertiary-btn-color,.desktop .prod-detail-section .view-all-tab.tertiary-btn-color,.listing-outerDiv .enquiry-mobile.tertiary-btn-color,.template-main-container .cms-add-action-button.tertiary-btn-color,.emptycart .cart-emptyBx .cont-shop button.tertiary-btn-color,#bookAppointment .submit-btn.tertiary-btn-color,.tertiary-btn-color,.wishlist-outerDiv .wishlist-body .wishlist-products .tertiary-btn-color,.btn.tertiary-btn-color,body.wap .btn.tertiary-btn-color,.product-details-page .range-default-style.selected,.btn.tertiary-btn-color:focus{background-color:#fff;color:#bb131a;border-color:#bb131a;outline-color:transparent;transition:0.3s}.template-main-container .cms-add-action-button.tertiary-btn-color{border-radius:30px}.primary-icon-btn-color,.qty-up-down .primary-icon-btn-color,.adbutton2.primary-icon-btn-color{background-color:transparent;color:#bb131a;border-color:transparent;outline-color:transparent;transition:0.3s}.primary-icon-btn-color .background-icon{background-color:#fff}.myAccount .my-account .myaccount-area .save-info-btn .btn{background-color:#bb131a;color:#fff;border-color:#bb131a;outline-color:transparent}.button-design-modal .default-primary-btn{background-color:#bb131a;color:#fff;border-color:#bb131a;outline-color:transparent;transition:0.3s;font-family:Gilroy;font-style:normal;text-decoration:none;border-radius:30px;font-size:14px;border-width:1px;line-height:inherit;letter-spacing:normal}.button-design-modal .default-primary-btn:focus{color:#fff !important;font-family:Gilroy;font-style:normal;text-decoration:none;border-radius:30px;font-size:14px;border-width:1px;line-height:inherit;letter-spacing:normal}.button-design-modal .default-secondary-btn{background-color:#bb131a;color:#fff;border-color:#bb131a;outline-color:transparent;transition:0.3s;font-family:Gilroy;font-style:normal;text-decoration:none;border-radius:30px;font-size:14px;border-width:1px;line-height:inherit;letter-spacing:normal}.button-design-modal .default-tertiary-btn,.button-design-modal .default-tertiary-btn:focus{background-color:#fff;color:#bb131a;border-color:#bb131a;outline-color:transparent;transition:0.3s;font-family:Gilroy;font-style:normal;text-decoration:none;border-radius:30px;font-size:14px;border-width:1px;line-height:inherit;letter-spacing:normal}.product-info-sec .ranges.selected,body.wap .product-variants .product-variant-keys .variant.active,body.wap .product-variants .variant-selected-style,.product-info-sec .variants .variant-selected-style{color:#bb131a !important;border-color:#bb131a !important}.floatCartButton,.enquiryForm .submit-btn.primary-btn-color,#calendarDateTimeModal .react-datepicker .react-datepicker__day--highlighted,.couponCodeSection .coupon-input-box .input-group-btn .primary-btn-color,#bookAppointment .submit-btn.primary-btn-color,.wishlist-outerDiv .wishlist-body .wishlist-products .primary-btn-color,.gymain .save-cont-wrp .svCont,:not(.button-design-modal).template-main-container .btn:not(.toolbar-action),.coverImageHeader.template-main-container .custom-template .editable-button-container .btn,.delivery-slot-container .date-card-container .date-card.selected,.delivery-slot-container .time-slot-container .time-slot.selected,.wap .deliverySlot .delivery-slot-container .react-datepicker .react-datepicker__day.react-datepicker__day--selected,.wap .deliverySlot .delivery-slot-container .date-section .date-card-container .date-card.selected,.wap .deliverySlot .delivery-slot-container .slots-wrapper .time-slot-container .time-slot.selected{background-color:#bb131a;color:#fff;border-color:#bb131a;outline-color:transparent;transition:0.3s}.coverImageHeader.template-main-container .custom-template .editable-button-container .btn,.template-main-container .btn,.template-main-container .primary-btn-color{border-radius:30px;font-family:Gilroy;font-style:normal;text-decoration:none;font-size:14px;border-width:1px;line-height:normal;letter-spacing:normal}.addBx.autoAdButon .adbutton1.primary-btn-color,.auto-rfqBtnWrp .rfqBtn.primary-btn-color{border:1px solid #bb131a;background-color:#bb131a;color:#fff;line-height:25px}.wap.preview .zoomImageDiv .belowSlider .sliderElement .sliderList.border-blue{border-color:#bb131a !important}@media (hover: hover) and (pointer: fine){.primary-btn-color:not(.no-hover):hover,.btn.primary-btn-color:not(.no-hover):hover,body.wap .btn.primary-btn-color:not(.no-hover):hover,.enquiryForm .send-enquiry.primary-btn-color:not(.no-hover):hover,.wap .listing-outerDiv .add-to-cart.primary-btn-color:not(.no-hover):hover{background-color:#ca2121;color:#fff;border-color:#ca2121;outline-color:transparent}.secondary-btn-color:not(.no-hover):hover,.btn.secondary-btn-color:not(.no-hover):hover{background-color:#ca2121;color:#fff;border-color:#ca2121;outline-color:transparent;text-decoration:none}.floatCartButton:hover{background-color:#ca2121;color:#fff;border-color:#ca2121;outline-color:transparent;transition:0.3s}.floatCartButton:hover .cart-txt-icon,.floatCartButton .cart-txt-icon:hover,.floatCartButton:hover .cart-btn-icon,.floatCartButton .cart-btn-icon:hover{color:#fff !important}.floatCartButton .cart-cnt-bg:hover,.floatCartButton:hover .cart-cnt-bg.cart-count-val{background-color:#fff !important}.floatCartButton:hover .cart-cnt-bg .cart-count-val,.floatCartButton .cart-cnt-bg .cart-count-val:hover,.floatCartButton:hover .cart-cnt-bg:hover .cart-count-val{color:#ca2121 !important}.button-design-modal .default-primary-btn:not(.no-hover):hover{background-color:#ca2121 !important;color:#fff !important;border-color:#ca2121 !important;outline-color:transparent;text-decoration:none}.button-design-modal .default-secondary-btn:not(.no-hover):hover{background-color:#ca2121 !important;color:#fff !important;border-color:#ca2121 !important;outline-color:transparent;text-decoration:none}.button-design-modal .default-tertiary-btn:not(.no-hover):hover{background-color:#ca2121 !important;color:#fff !important;border-color:#ca2121 !important;outline-color:transparent;text-decoration:none}.emptycart .cart-emptyBx .cont-shop button.tertiary-btn-color:hover,.desktop .prod-detail-section .view-all-tab.tertiary-btn-color:hover,.listing-outerDiv .enquiry-mobile.tertiary-btn-color:hover,.template-main-container .cms-add-action-button.tertiary-btn-color:hover,.emptycart .cart-emptyBx .cont-shop button.tertiary-btn-color:hover,#bookAppointment .submit-btn.tertiary-btn-color:hover,.wishlist-outerDiv .wishlist-body .wishlist-products .tertiary-btn-color:hover,.tertiary-btn-color:not(.no-hover):hover,.btn.tertiary-btn-color:not(.no-hover):hover,body.wap .btn.tertiary-btn-color:not(.no-hover):hover{background-color:#ca2121;color:#fff;border-color:#ca2121;outline-color:transparent;text-decoration:none}.myAccount .my-account .myaccount-area .save-info-btn .btn:hover{background-color:#ca2121;color:#fff;border-color:#ca2121;outline-color:transparent;text-decoration:none}.desktop .enquiryForm .submit-btn.primary-btn-color:hover,.desktop #calendarDateTimeModal .react-datepicker__day:hover,.desktop #calendarDateTimeModal .react-datepicker .react-datepicker__day:not(.react-datepicker__day--disabled):hover,.desktop .couponCodeSection .coupon-input-box .jd-btn-primary.primary-btn-color:hover,.desktop #cartTable .itmdt .green_btn.primary-btn-color:hover,.desktop #calendarDateTimeModal .react-datepicker .react-datepicker__day--highlighted:hover,.desktop .couponCodeSection .coupon-input-box .input-group-btn .primary-btn-color:hover,.desktop #bookAppointment .submit-btn.primary-btn-color:hover,.desktop .addBx.autoAdButon .adbutton1.primary-btn-color:hover,.desktop .auto-rfqBtnWrp .rfqBtn.primary-btn-color:hover,.desktop .wishlist-outerDiv .wishlist-body .wishlist-products .primary-btn-color:hover,.desktop .gymain .grcChktBtm .svCont:hover,.desktop .gymain .save-cont-wrp .svCont:hover,.desktop #outletChangeModal.trk-ordrPop .strtShopbtWrp .strtShopBt-act:hover,.desktop .static-templates .template-main-container .custom-template .btn:not(.toolbar-action):hover,.desktop :not(.button-design-modal).template-main-container .custom-template .editable-content-holder .link-button.btn:hover,.desktop .static-templates .template-main-container .custom-template .editable-button-container .btn:hover,.desktop .coverImageHeader.template-main-container .custom-template .editable-button-container .btn:hover{background-color:#ca2121;color:#fff;border-color:#ca2121;outline-color:transparent;text-decoration:none}}
    </style>
<link data-chunk="webstore" rel="stylesheet" href="https://static1.jdomni.in/mpstatic/webstore/css/22579.4e242d3b.css">
<link data-chunk="css-fonts-WebStore-style-css" rel="stylesheet" href="https://static1.jdomni.in/mpstatic/webstore/css/25926.491aa1f8.css">
<link data-chunk="css-header-coverImageMiddleHeader-scss" rel="stylesheet" href="https://static1.jdomni.in/mpstatic/webstore/css/32874.1a8aa7b7.css">
<link data-chunk="not-found" rel="stylesheet" href="https://static1.jdomni.in/mpstatic/webstore/css/57942.32373673.css">
<style
>@font-face{font-family:Cabin;font-style:normal;font-weight:400;font-display:swap;src:local("Cabin"),local("Cabin-Regular"),url(https://fonts.gstatic.com/s/cabin/v12/u-4x0qWljRw-Pd8w__1ImSRu.woff2) format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Cabin;font-style:normal;font-weight:500;font-display:swap;src:local("Cabin Medium"),local("Cabin-Medium"),url(https://fonts.gstatic.com/s/cabin/v12/u-480qWljRw-PdfD3OhluylEeQ5J.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Cabin;font-style:normal;font-weight:700;font-display:swap;src:local("Cabin Bold"),local("Cabin-Bold"),url(https://fonts.gstatic.com/s/cabin/v12/u-480qWljRw-PdeL2uhluylEeQ5J.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Abril Fatface;font-style:normal;font-weight:400;font-display:swap;src:local("Abril Fatface"),local("AbrilFatface-Regular"),url(https://fonts.gstatic.com/s/abrilfatface/v9/zOL64pLDlL1D99S8g8PtiKchq-dmjQ.woff2) format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Roboto;font-style:normal;font-weight:100;font-display:swap;src:local("Roboto Thin"),local("Roboto-Thin"),url(https://fonts.gstatic.com/s/roboto/v18/KFOkCnqEu92Fr1MmgVxIIzI.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Roboto;font-style:normal;font-weight:300;font-display:swap;src:local("Roboto Light"),local("Roboto-Light"),url(https://fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmSU5fBBc4.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Roboto;font-style:normal;font-weight:400;font-display:swap;src:local("Roboto"),local("Roboto-Regular"),url(https://fonts.gstatic.com/s/roboto/v18/KFOmCnqEu92Fr1Mu4mxK.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Roboto;font-style:normal;font-weight:500;font-display:swap;src:local("Roboto Medium"),local("Roboto-Medium"),url(https://fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmEU9fBBc4.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Roboto;font-style:normal;font-weight:700;font-display:swap;src:local("Roboto Bold"),local("Roboto-Bold"),url(https://fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmWUlfBBc4.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}@font-face{font-family:Roboto;font-style:normal;font-weight:900;font-display:swap;src:local("Roboto Black"),local("Roboto-Black"),url(https://fonts.gstatic.com/s/roboto/v18/KFOlCnqEu92Fr1MmYUtfBBc4.woff2) 
format("woff2");unicode-range:U+00??,U+0131,U+0152-0153,U+02bb-02bc,U+02c6,U+02da,U+02dc,U+2000-206f,U+2074,U+20ac,U+2122,U+2191,U+2193,U+2212,U+2215,U+feff,U+fffd}</style><style class="pre-script-ele" id="pre-script-ele"></style><style class="post-script-ele" id="post-script-ele">
</style>
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/91384.fdf2b0bf.css">
<link rel="stylesheet" href="https://static3.jdomni.in/mpstatic/webstore/contentblock.css?q=services,static-layouts/template2,gallery/gallery,static-layouts/template1,video/jd-dynamic-video,testimonial/topQuoteTestimonial,static-layouts/template108,static-layouts/template22,static-layouts/notification&amp;themeVersion=1623735865000&amp;ver=e67e77391c352b029ada" type="text/css">
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/74611.d44e930c.css">
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/12479.f7dd9f63.css">
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/6030.5aa0d675.css">
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/37885.2dcbdac3.css">
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/88349.cfc6a482.css">
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/1775.43608e83.css">
<link rel="stylesheet" type="text/css" href="https://static1.jdomni.in/mpstatic/webstore/css/35922.3ec85576.css">
</head>
<body class="preview overlay-scroll jd-webp web-theme-background"><div id="top"></div>
    <div id="app">
        <div class="coverImageMiddleHeader">
                    <div class="mobile-loader initial-cms-loader hide">
                        <div class="svg-wrapper">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px">
                                <circle cx="12px" cy="12px" r="9px" class="circle"></circle>
                            </svg>
                        </div>
                    </div>
                    <div class="react-slider-holder" id="react-slider-holder"></div>
                    <div class=" qVvA_success _2ypN_toast-container  undefined " style="bottom:-72px">
                        <div class="OLtM_toast-msg-container"></div>
                        <div class="_3MXO_ripple JPxw_close-icon _3ebv_has-close cxpu_btn-animate-hover">
                            <i class="icon-HDRcross"></i>
                            <div class="n2_N_rippleContainer"></div>
                        </div>
                    </div>
                    <div class="mobile-loader " id="filterLoader" style="display:none">
                        <div class="svg-wrapper">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px">
                                <circle cx="12px" cy="12px" r="9px" class="circle"></circle>
                            </svg>
                        </div>
                    </div>
                    <div class="btmblk webheader header-content outer-parent coverImageMiddleHeader all-sections header-sticky sticky" id="staticHeader">
                        <style>
                            .header-block .hoverStyle24960:hover{border-color:rgba(202, 33, 33, 1) !important;background-color:rgba(202, 33, 33, 1) !important;}
                        </style>
                        <div class="header-block coverImageHeader template-main-container coverImageMiddleHeader   " style="border-color: rgb(84, 84, 84); border-style: none; border-width: 0px; background-image: url(&quot;https://image1.jdomni.in/banner/06122019/B1/D7/A4/83FC0CB970464EF593A566C4BD_1575626626760.jpg?output-format=webp&quot;); background-size: cover;" data-header-type="coverImageHeader" data-web-bg-img="https://image1.jdomni.in/banner/06122019/B1/D7/A4/83FC0CB970464EF593A566C4BD_1575626626760.jpg?output-format=webp" data-mob-bg-img="https://image1.jdomni.in/banner/06122019/30/65/89/13EA5D262ECFA743A8178C5460_1575632997252.jpg">
                            <div class="bootstrap-iso header-custom-template custom-template">
                                <div class="fake-coverImageHeader-div" style="height: 140px;"></div>
                                <div class="coverImage-gradient-Block first-second-block" style="top: -40px;">
                                    <div class="first-block innercont header-editable-contentHolder editable-content-holder cmsheader header-top-color block-list" id="header-first-block">
                                        <div class="headerBlock-editContent editable-content">
                                            <div class="header-center">
                                                <div class="display-flex">
                                                    <div class="account-social-wrapper">
                                                        <div class="social-wrapper pos-rel">
                                                            <div class="editable-content-holder icon-holder social-wrapper pos-rel ">
                                                                <div class="editable-content iconEdit">
                                                                    <i><a target="_blank" href="mailto:contact@mysites.com" class="social-icon icon-message_2 event-disabled"></a></i>
                                                                    <i><a target="_blank" href="http://www.facebook.com" class="social-icon icon-fb event-disabled"></a></i>
                                                                    <i><a target="_blank" href="http://www.linkedin.com" class="social-icon icon-in event-disabled"></a></i>
                                                                    <i><a target="_blank" href="http://www.instagram.com" class="social-icon icon-insta event-disabled"></a></i>
                                                                    <i><a target="_blank" href="http://www.twitter.com" class="social-icon icon-Twiter event-disabled"></a></i>
                                                                    <i><a target="_blank" href="https://www.justdial.com" class="social-icon icon-jdLogo event-disabled"></a></i>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="defaultLink-wrapper display-flex">
                                                        <div class="contact-wrapper">
                                                            <div class="account-info-sec">
                                                                <div class="header-links contactEmail-link editable-content-holder  ">
                                                                    <a href="mailto:contact@mysites.com" class="default-text-color go-link-source event-disabled link-content">
                                                                        <div class="contact-link email  editable-content" style="font-family: Cabin;">
                                                                            <i class="contact-icon default-icon-color ico icon-message_2"></i>
                                                                            <span class="links-text">lifeshare.com</span>
                                                                        </div>
                                                                    </a>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="right-sec">
                                                    <div class="editable-content-holder store-Outlet header-links  single-Outlet ">
                                                        <span class="display-flex change-outlet default-text-color event-disabled not-editable editable-content " style="font-family: Cabin;">
                                                            <i class="head-edit icon-locationNew default-icon-color iconLocation notranslate"></i>
                                                            <span class="truncate-text default-text-color go-link-source area-loc store-name-color">
                                                                <a class="edit-outlet-btn default-text-color noUnderline">
                                                                    <span class="links-text">Dum Dum, North Kolkata, West Bengal</span>
                                                                </a>
                                                            </span>
                                                        </span>
                                                    </div>
                                                    <div class="userAccount-wrapper">
                                                        <div class="editable-content-holder userAccount-wrpr ">
                                                            <div class="signup-login-btn-div default-text-color event-disabled not-editable editable-content " style="font-family: Cabin;">
                                                                <div class="login-icon-holder">
                                                                    <span class="header-icon-customer user-icon-color profile-icon icon-hdrUser"> </span>
                                                                </div>
                                                                <div class="login-signup-text">
                                                                    <span class="sign-up-login-btn go-link-source login-signup-color cursor-pointer login-link">Log In</span>
                                                                    <span class="dash-separator login-signup-separator"> | </span>
                                                                    <span class="sign-up-login-btn go-link-source login-signup-color cursor-pointer signup-link"> Sign Up </span>
                                                                </div>
                                                            </div>
                                                            <div class="signup-login-btn-div default-text-color event-disabled not-editable editable-content  dn" id="my-account-div" style="font-family: Cabin;">
                                                                <div class="my-account-holder">
                                                                    <div class="login-icon-holder my-account-popup go-link-source">
                                                                        <span class="header-icon-customer profile-icon user-icon-color icon-hdrUser"></span>
                                                                    </div>
                                                                    <div class="login-signup-text login-signup-color">
                                                                        <span class="welcome-txt my-account-popup" style="cursor: pointer;">
                                                                            <span class="welcome-text-span">Hi  </span>
                                                                            <span class="icon-pagination-down login-signup-color"></span>
                                                                        </span>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="second-block cmsheader block-list header-noscroll editable-content-holder header-editable-contentHolder " id="header-second-block">
                                        <div class="header-center">
                                            <div class="leftLink-outerDiv">
                                                <div class="leftLink-wrapper menuLink-wrapper noBurgerMenu full-width" style="width: 327px;">
                                                    <div class="editable-content-holder menu-list-holder right-head header-content  header-menu-links ">
                                                        <div class="editable-content menulist-container event-disabled display-flex  align-center" id="menuList" style="font-family: Cabin;">
                                                            <div class="leftMenu menu-list link-pos display-flex" id="leftLinkName">
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093666">
                                                                    <a href="index.py" class="track-order menuLink-color" title="Home">Home</a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093667">
                                                                    <a class="track-order menuLink-color" href="#survice" title="Services">Services</a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093667">
                                                                    <a class="track-order menuLink-color" href="#post" title="Services">Post</a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093668">
                                                                    <a class="track-order menuLink-color" href="#about" title="About Us">About Us</a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093669">
                                                                    <a class="track-order menuLink-color" href="#gallery" title="Gallery">Gallery</a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093669">
                                                                    <a class="track-order menuLink-color" href="#fact" title="Gallery">Fact</a>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="logo-wrapper editable-content-holder web-logo-wrapper  ">
                                                <div class="strlogo pos-rel editable-content logo-container ">
                                                    <a class="vendor-logo-bx logo-in event-disabled" href="index.py">
                                                        <span class="logo-edit-style">
                                                            <img src="img/logo.png" style="max-width:195px;max-height:66px" alt="" title="">
                                                        </span>
                                                    </a>
                                                </div>
                                            </div>
                                            <div class="rightLink-outerDiv">
                                                <div class="rightLink-wrapper menuLink-wrapper  full-width" style="width: 222px;">
                                                    <div class="editable-content-holder menu-list-holder right-head header-content  header-menu-links ">
                                                        <div class="editable-content menulist-container event-disabled display-flex  align-center" id="menuList" style="font-family: Cabin;">
                                                            <div class="rightMenu menu-list link-pos display-flex" id="rightLinkName">
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093669">
                                                                    <a class="track-order menuLink-color" href="#donet" title="Why donate blood">Why donate blood</a>
                                                                </div>
                                                                
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093669">
                                                                    <a class="track-order menuLink-color" href="#videos" title="Gallery">Videos</a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093669">
                                                                    <a class="track-order menuLink-color" href="#contact" title="Gallery">Contact Us</a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093669">
                                                                    <a class="track-order menuLink-color" title="Gallery"></a>
                                                                </div>
                                                                <div class="pageLink menuLink-color no-dropdown display-flex " data-link-id="385093669">
                                                                    <a class="track-order menuLink-color" title="Gallery"></a>
                                                                </div>
                                                                
                                                                <div class="login-signup-text">
                                                                    <a href="paitentlogin.py"><span class="sign-up-login-btn go-link-source login-signup-color cursor-pointer login-link">Patient</span></a>
                                                                    <span class="dash-separator login-signup-separator"> | </span>
                                                                    <a href="hospitallogin.py"><span class="sign-up-login-btn go-link-source login-signup-color cursor-pointer signup-link">Hospital</span></a>
                                                                </div>
                                                                
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="third-block cmsheader cover-static-block" id="header-third-block">
                                    <div class=" container-fluid position-holder positionCenterRight">
                                        <div class=" row">
                                            <div class="">
                                                <div class=" editable-text editable-content-holder  ">
                                                    <div class=" main-header align-center font-size-36 editable-content" style="color: rgb(44, 44, 44); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1; letter-spacing: 0.7px;">
                                                        <div>Prompt and Economical&nbsp;</div>
                                                    </div>
                                                </div>
                                                <div class=" editable-text editable-content-holder  ">
                                                    <div class="para-1 align-center font-size-30 editable-content" style="color: rgb(179, 35, 32); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1.4; border-color: rgb(44, 44, 44); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Blood Bank Management System</div>
                                                </div>
                                                <div class=" editable-text editable-content-holder  ">
                                                    <div class="para-1 align-center font-size-30 editable-content" style="color: rgb(7, 50, 170); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1.4; border-color: rgb(44, 44, 44); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">We Are All Come Together To Extend A Helping Hand To Everyone In This Society</div>
                                                </div>
                                                <div class="editable-button-container  alignment-container paddingLR0 three-btns align-center">
                                                    <div class="editable-content-holder editable-button align-center ">
                                                        
                                                    </div>
                                                    <div class=" header-buttons-container"></div><div id="survice"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="normal-menu child-menuLink-background  right hide-menu-popover">
                        <div class="normal-menulinks-wrapper"></div>
                    </div>
                    <div class="background-container" style="min-height: calc(100vh - 887px);">
                        <div class="theme-bg-color">
                            <div class="home-page">
                                <div class="clearfix ">
                                    <div id="contentBlock579793427" class="edit-content  contentBlock579793427 firstContent jd-services" data-content-block-template="service1" data-block-id="309280801">
                                        <div class="template-main-container  services " data-transparency_value=" 1" data-web-bg-img="" data-mob-bg-img="" alt="" title="" style="border-color: rgb(66, 66, 66); border-style: none; border-width: 0px;">
                                            <div class="custom-template bootstrap-iso clearfix" style="background-color: rgb(255, 255, 255);">
                                                <div class="container-fluid">
                                                    <div class="row">
                                                        <div class="header-subheader jd-font-roboto">
                                                            <div class=" editable-content-holder  ">
                                                                <a href="javascript:void(0)" class="link-content">
                                                                    <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Services</div>
                                                                </a>
                                                            </div>
                                                        </div>
                                                        <div class="col-md-12 col-xs-12 align-center">
                                                            <div class="services-block-slider marginT5" style="display: flex; flex-wrap: wrap; justify-content: center; margin-top: 10px;">
                                                                <div class="services-block-container marginB20" data-index="0" style="width: 25%;">
                                                                    <div class="col-md-12 services-column">
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="editable-image-holder  editable-image-holder services-image dynamic-block-image">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class="editable-content   align-center not-editable marginB15  ">
                                                                                        <img src="https://image3.jdomni.in/banner/07122017/ED/84/C6/DDE82C7BAE38A9BCC0A9E0B6D1_1512657582508.jpg?output-format=webp" alt="" class="services-image-tag img-loaded" style="width: 100%; height: auto; max-width: 250px; max-height: 250px; border-radius: 15px;">
                                                                                    </div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="marginT10 clearfix">
                                                                                <div class="content para-1 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" not-editable para-1 font-size-22 align-center not-editable para-1 editable-content" contenteditable="false" style="color: rgb(158, 21, 21); font-family: Cabin; line-height: 1.5; letter-spacing: 0.7px;">Blood Storage</div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="clearfix services-desc">
                                                                            <div class="content para-2 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" align-center not-editable para-2 font-size-18 not-editable para-2 editable-content" contenteditable="false" style="color: rgba(58, 58, 58, 0.85); font-family: Cabin; line-height: 1.4; letter-spacing: 0.5px;">We store the safest blood of all blood groups which you can use for any kind of treatments or in an emergency.</div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        
                                                                    </div>
                                                                </div>
                                                                <div class="services-block-container marginB20" data-index="1" style="width: 25%;">
                                                                    <div class="col-md-12 services-column">
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="editable-image-holder  editable-image-holder services-image dynamic-block-image">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class="editable-content   align-center not-editable marginB15  ">
                                                                                        <img src="https://image3.jdomni.in/banner/07122017/1B/CF/8A/2CD62AE3CDD610A93640861E19_1512657611065.jpg?output-format=webp" alt="" class="services-image-tag img-loaded" style="width: 100%; height: auto; max-width: 250px; max-height: 250px; border-radius: 15px;">
                                                                                    </div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="content para-1 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" not-editable para-1 font-size-22 align-center not-editable para-1 editable-content" contenteditable="false" style="color: rgb(158, 21, 21); font-family: Cabin; line-height: 1.5; letter-spacing: 0.7px;">Blood Donation</div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="clearfix services-desc">
                                                                            <div class="content para-2 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" align-center not-editable para-2 font-size-18 not-editable para-2 editable-content" contenteditable="false" style="color: rgba(58, 58, 58, 0.85); font-family: Cabin; line-height: 1.4; letter-spacing: 0.5px;">Donation of blood is an selfless service that we do for mankind! We allow you to save a life by donating blood to the ones who need it.</div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        
                                                                    </div>
                                                                </div>
                                                                <div class="services-block-container marginB20" data-index="2" style="width: 25%;">
                                                                    <div class="col-md-12 services-column">
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="editable-image-holder  editable-image-holder services-image dynamic-block-image">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class="editable-content   align-center not-editable marginB15  ">
                                                                                        <img src="img/Hospital-HITN.jpg" alt="" class="services-image-tag img-loaded" style="width: 100%; height: auto; max-width: 250px; max-height: 250px; border-radius: 15px;">
                                                                                    </div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="content para-1 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" not-editable para-1 font-size-22 align-center not-editable para-1 editable-content" contenteditable="false" style="color: rgb(158, 21, 21); font-family: Cabin; line-height: 1.5; letter-spacing: 0.7px;">Help From Hospitals</div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="clearfix services-desc">
                                                                            <div class="content para-2 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" align-center not-editable para-2 font-size-18 not-editable para-2 editable-content" contenteditable="false" style="color: rgba(58, 58, 58, 0.85); font-family: Cabin; line-height: 1.4; letter-spacing: 0.5px;">The hospital responsible for management of the hospital's blood stock, includes maintining an inventory for each blood group.</div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        
                                                                    </div>
                                                                </div>
                                                                <div class="services-block-container marginB20" data-index="3" style="width: 25%;">
                                                                    <div class="col-md-12 services-column">
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="editable-image-holder  editable-image-holder services-image dynamic-block-image">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class="editable-content   align-center not-editable marginB15  ">
                                                                                        <img src="img/POSTpost.jpg" alt="" class="services-image-tag img-loaded" style="width: 100%; height: auto; max-width: 250px; max-height: 250px; border-radius: 15px;">
                                                                                    </div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="content para-1 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" not-editable para-1 font-size-22 align-center not-editable para-1 editable-content" contenteditable="false" style="color: rgb(158, 21, 21); font-family: Cabin; line-height: 1.5; letter-spacing: 0.7px;">Make A Post</div>
                                                                                </a>
                                                                            </div>  
                                                                        </div>
                                                                        <div class="clearfix services-desc">
                                                                            <div class="content para-2 editable-content-holder  ">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class=" align-center not-editable para-2 font-size-18 not-editable para-2 editable-content" contenteditable="false" style="color: rgba(58, 58, 58, 0.85); font-family: Cabin; line-height: 1.4; letter-spacing: 0.5px;">Platelets play an important role in blocking the blood flow at the times of injuries. We also provide platelets to maintain its count in your blood.</div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        
                                                                    </div>
                                                                </div>
                                                            </div><div id="post"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
</div>''')
src="SELECT p.*, u.mob FROM post p INNER JOIN registration u ON p.pid=u.pid WHERE p.status=1"
cursor=config.db8.cursor()
cursor.execute(src)
rs=cursor.fetchall()
if rs:
    print('''<div id="contentBlock579793427" class="edit-content  contentBlock579793427 firstContent jd-services" data-content-block-template="service1" data-block-id="309280801">
                                        <div class="template-main-container  services " data-transparency_value=" 1" data-web-bg-img="" data-mob-bg-img="" alt="" title="" style="border-color: rgb(66, 66, 66); border-style: none; border-width: 0px;">
                                            <div class="custom-template bootstrap-iso clearfix" style="background-color: rgb(255, 255, 255);">
                                                <div class="container-fluid">
                                                    <div class="row">
                                                        <div class="header-subheader jd-font-roboto">
                                                            <div class=" editable-content-holder  ">
                                                                <a href="javascript:void(0)" class="link-content">
                                                                    <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Post</div>
                                                                </a>
                                                            </div>
                                                        </div>
                                                        <div class="col-md-12 col-xs-12 align-center">
                                                        <div class="services-block-slider marginT5" style="display: flex; flex-wrap: wrap; justify-content: center; margin-top: 10px;">''')
    for rec in rs:
        print('''                                           
                                                                <div class="services-block-container marginB20" data-index="3" style="width: 25%;">
                                                                    <div class="col-md-12 services-column">
                                                                        <div class="marginT10 clearfix">
                                                                            <div class="editable-image-holder  editable-image-holder services-image dynamic-block-image">
                                                                                <a href="javascript:void(0)" class="link-content">
                                                                                    <div class="editable-content   align-center not-editable marginB15  ">
                                                                                        <textarea name="post" placeholder="" style="text-align:center; width: 250px; height: 250px; font-size:35px; font-family: {}; background: {}; border: none; color:{}; transition: 0.25s; outline: none;" readonly>{}</textarea>
                                                                                    </div>
                                                                                </a>
                                                                            </div>
                                                                        </div>
                                                                        <div class="col-md-12 col-xs-12 paddingLR0">
                                                                            <div class="editable-content-holder editable-button align-center ">
                                                                                <div class="editable-content">
                                                                                    <a class="phoneNo-link" href="tel:+91{}"><button class="btn button contact_submit primary-btn-color  align-left btn-md btn-rounded  hoverStyle42319" style="color: rgb(255, 255, 255); overflow: hidden; position: relative; min-height: auto; border-color: rgb(191, 47, 47); background-color: rgb(191, 47, 47);">Contact</button></a>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>'''.format(rec[2],rec[3],rec[4],rec[1],rec[7]))
    print('''
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>''')
else:
    print('Sorry no post found')
print('''
                                    <div id="contentBlock579793428" class="edit-content  contentBlock579793428 static-templates" data-content-block-template="template2" data-block-id="309280813"><div id="about"></div>
                                        <div class="template-main-container   " data-transparency_value=" 0.8" data-web-bg-img="https://image3.jdomni.in/banner/06122019/43/8A/D8/AB4ABBD11FDBF090955A41B7AD_1575628644998.jpg" data-mob-bg-img="https://image2.jdomni.in/banner/06122019/FB/BA/6F/820D37C03E2C2BC9D27054373A_1575628650562.jpg" style="background-image: url(&quot;https://image3.jdomni.in/banner/06122019/43/8A/D8/AB4ABBD11FDBF090955A41B7AD_1575628644998.jpg?output-format=webp&quot;);">
                                            <div class="custom-template  clearfix bootstrap-iso template-2 global-block-padding" style="background-color: rgba(255, 255, 255, 0.8);">
                                                <div class=" container-fluid">
                                                    <div class=" row responsive-row">
                                                        <div class=" col-md-6 main-image image-left responsive-image">
                                                            <div class="editable-image-holder  " data-cropperid="1812487">
                                                                <div class="editable-content    ">
                                                                    <img src="https://image3.jdomni.in/banner/06122019/C7/24/F3/B4014C78EB037B6BC135E26404_1575628997819.jpg?output-format=webp" alt="" class=" img-loaded" style="border-radius: 15px;">
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class=" col-md-6 responsive-content">
                                                            <div class=" editable-content-holder  ">
                                                                <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">About Us</div>
                                                            </div>
                                                            <div class=" block-t-space">
                                                                <div class=" editable-content-holder  ">
                                                                    <div class="para-1 align-center   font-size-18 editable-content jd-cms-tag jd-cms-tag-company-description" style="color: rgba(58, 58, 58, 0.85); min-height: auto; font-family: Cabin; line-height: 2; border-color: rgba(58, 58, 58, 0.85); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.5px; background-color: rgba(0, 0, 0, 0);">We, Life Share Blood Banks at Dum Dum, North Kolkata, West Bengal, aim to provide prompt, economical and reliable services of the safest blood and all blood Conecters like Donor, Near Hospital stock etc. Offering the industry-leading, advanced technology and well-equipped inventory, we make all types of blood available for the patients and many hospitals. We contribute in saving many lives in the time of need or in an emergency.</div>
                                                                </div>
                                                            </div>
                                                            <div class="editable-button-container  paddingLR0 alignment-container"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div id="contentBlock579793429" class="edit-content  contentBlock579793429" data-content-block-template="gallery1" data-block-id="309280803"><div id="gallery"></div>
                                        <div class="template-main-container  editGalleryTemplate  " data-transparency_value=" 1" data-web-bg-img="" data-mob-bg-img="" style="color: rgb(51, 51, 51); font-family: Roboto; border-color: rgb(66, 66, 66); border-style: none; border-width: 0px; border-radius: 0px;">
                                            <div class="custom-template bootstrap-iso clearfix " style="background-color: rgb(255, 255, 255);">
                                                <div class="container-fluid">
                                                    <div class="row">
                                                        <div class="header-subheader jd-font-roboto">
                                                            <div class=" editable-content-holder  ">
                                                                <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Gallery</div>
                                                            </div>
                                                        </div>
                                                        <div class="col-xs-12 clearfix gallery-overflow paddingLR0">
                                                            <div class="slick-slider gallery-block slick-initialized">
                                                                <div class="slick-list">
                                                                    <div class="slick-track" style="width: 994px; opacity: 1; transform: translate3d(0px, 0px, 0px);">
                                                                        <div data-index="0" class="slick-slide slick-active slick-current" tabindex="-1" aria-hidden="false" style="outline: none; width: 994px;">
                                                                            <div>
                                                                                <div tabindex="-1" style="width: 100%; display: inline-block;">
                                                                                    <div class=" imgRow ">
                                                                                        <div class="" style="width: 33.3%; display: inline-block; padding: 30px 15px 0px;">
                                                                                            <div class="editable-image-holder  editable-gallery">
                                                                                                <div class="editable-content  gallery-img-container   " style="height: inherit; overflow: hidden; border-style: none; border-width: 0px; border-radius: 15px;">
                                                                                                    <img src="img/donordonor.jpg" alt="" class=" img-loaded" draggable="false">
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                        <div class="" style="width: 33.3%; display: inline-block; padding: 30px 15px 0px;">
                                                                                            <div class="editable-image-holder  editable-gallery">
                                                                                                <div class="editable-content  gallery-img-container   " style="height: inherit; overflow: hidden; border-style: none; border-width: 0px; border-radius: 15px;">
                                                                                                    <img src="img/paitent.jpg" alt="" class=" img-loaded" draggable="false">
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                        <div class="" style="width: 33.3%; display: inline-block; padding: 30px 15px 0px;">
                                                                                            <div class="editable-image-holder  editable-gallery">
                                                                                                <div class="editable-content  gallery-img-container   " style="height: inherit; overflow: hidden; border-style: none; border-width: 0px; border-radius: 15px;">
                                                                                                    <img src="img/hospitalhospital.jpg" alt="" class=" img-loaded" draggable="false">
                                                                                                </div>
                                                                                            </div>
                                                                                        </div>
                                                                                        
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div id="contentBlock579793431" class="edit-content  contentBlock579793431 dynamic-video-block video-block" data-content-block-template="jd-dynamic-video" data-block-id="578417086"><div id="fact"></div>
                                        <div class="template-main-container   " data-transparency_value="1" data-web-bg-img="" data-mob-bg-img="">
                                            <div class="custom-template bootstrap-iso clearfix jd-dynamic-video global-block-padding" style="background-color: rgb(255, 255, 255);">
                                                <div class="container-fluid">
                                                    <div class="header-subheader jd-font-roboto">
                                                        <div class=" editable-content-holder  ">
                                                            <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Facts</div>
                                                        </div>
                                                    </div>
                                                    <div class="video-row">
                                                        <img src="img/life.gif" alt="" class=" img-loaded" draggable="false">
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div id="contentBlock579793430" class="edit-content  contentBlock579793430 static-templates" data-content-block-template="template1" data-block-id="309280815"><div id="donet"></div>
                                        <div class="template-main-container    " data-transparency_value=" 0.8" data-web-bg-img="https://image3.jdomni.in/banner/06122019/04/71/BC/E10BA4CCA493762CB932C76CEC_1575629047934.jpg" data-mob-bg-img="https://image3.jdomni.in/banner/06122019/4A/45/3B/93EBE7B923C24E8B91D8992FFE_1575629055613.jpg" style="color: rgb(51, 51, 51); font-family: Roboto; border-color: rgb(51, 51, 51); border-style: none; border-width: 0px; border-radius: 0px; background-image: url(&quot;https://image3.jdomni.in/banner/06122019/04/71/BC/E10BA4CCA493762CB932C76CEC_1575629047934.jpg?output-format=webp&quot;);">
                                            <div class="custom-template clearfix bootstrap-iso template-1 global-block-padding " style="background-color: rgba(255, 255, 255, 0.8);">
                                                <div class=" container-fluid">
                                                    <div class=" row">
                                                        <div class=" col-md-6 main-image">
                                                            <div class="editable-image-holder  " data-cropperid="1813639">
                                                                <div class="editable-content    " style="">
                                                                    <img src="https://image3.jdomni.in/banner/06122019/1A/FD/53/8DCEC6FF0B18691E6994E1A83A_1575638920190.jpg?output-format=webp" alt="" class=" img-loaded" style="border-radius: 15px;">
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class=" col-md-6 content-1">
                                                            <div class=" editable-content-holder  ">
                                                                <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Why donate blood?</div>
                                                            </div>
                                                            <div class=" block-t-space">
                                                                <div class=" editable-content-holder  ">
                                                                    <div class="para-1 align-center font-size-18 editable-content" style="color: rgba(58, 58, 58, 0.85); min-height: auto; font-family: Cabin; line-height: 2; border-color: rgba(58, 58, 58, 0.85); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.5px; background-color: rgba(0, 0, 0, 0);">Everyday, there are many emergency cases or other treatments that require blood. But unfortunately, the requirement of blood is exponentially more than its supply. This, at times, leads to loss of life. An act of kindness and a selfless service of donating blood can make a big difference and save and prolong someone's life.</div>
                                                                </div>
                                                            </div>
                                                            <div class="editable-button-container  paddingLR0 alignment-container align"></div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div id="contentBlock579793431" class="edit-content  contentBlock579793431 dynamic-video-block video-block" data-content-block-template="jd-dynamic-video" data-block-id="578417086"><div id="videos"></div>
                                        <div class="template-main-container   " data-transparency_value="1" data-web-bg-img="" data-mob-bg-img="">
                                            <div class="custom-template bootstrap-iso clearfix jd-dynamic-video global-block-padding" style="background-color: rgb(255, 255, 255);">
                                                <div class="container-fluid">
                                                    <div class="header-subheader jd-font-roboto">
                                                        <div class=" editable-content-holder  ">
                                                            <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Videos</div>
                                                        </div>
                                                    </div>
                                                    <div class="video-row">
                                                        <div class="col-md-6 col-xs-12 video-desc-holder">
                                                            <div class="col-md-12 paddingLR0  editable-video-holder tint-applied" data-block-id="5797934310" data-video-id="video_5797934310_1623742114255_0">
                                                                <div class="video-player-holder" data-src="https://www.youtube.com/embed/FvG7MyDsEjg?enablejsapi=1" data-youtubeurl="" data-poster="https://i.ytimg.com/vi/FvG7MyDsEjg/hqdefault.jpg" data-video-uploaded="false" data-video-type="youtube" style="background: none; height: 100%;">
                                                                    <video width="600" height="350" controls >
                                                                        <source src="img/vid1.mp4" type="video/mp4">
                                                                    </video>
                                                                </div>
                                                            </div>
                                                            <div class="col-md-12 editable-title paddingLR0 editable-content-holder  ">
                                                                <div class="not-editable  font-size-22 align-center editable-content" contenteditable="false">The Benefits of Donating Blood</div>
                                                            </div>
                                                        </div>
                                                        <div class="col-md-6 col-xs-12 video-desc-holder">
                                                            <div class="col-md-12 paddingLR0  editable-video-holder tint-applied" data-block-id="5797934311" data-video-id="video_5797934311_1623742114261_0">
                                                                <div class="video-player-holder" data-src="https://www.youtube.com/embed/i-65bghkskI?enablejsapi=1" data-youtubeurl="" data-poster="https://i.ytimg.com/vi/i-65bghkskI/hqdefault.jpg" data-video-uploaded="false" data-video-type="youtube" style="background: none; height: 100%;">
                                                                    <video width="600" height="350" controls >
                                                                        <source src="img/vid2.mp4" type="video/mp4">
                                                                    </video>
                                                                </div>
                                                            </div>
                                                            <div class="col-md-12 editable-title paddingLR0 editable-content-holder  ">
                                                                <div class="not-editable  font-size-22 align-center editable-content" contenteditable="false">Why Should You Donate Blood?</div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    
                                    <div id="contentBlock579793433" class="edit-content  contentBlock579793433 static-templates" data-content-block-template="template108" data-block-id="309280809"><div id="contact"></div>
                                        <style>.contentBlock579793433 .hoverStyle42319:hover{border-color:rgba(202, 33, 33, 1) !important;background-color:rgba(202, 33, 33, 1) !important;}</style>
                                        <div class="template-main-container   " data-transparency_value="1" data-web-bg-img="" data-mob-bg-img="">
                                            <div class="custom-template  template-108 bootstrap-iso btn-md global-block-padding" style="background-color: rgb(255, 255, 255);">
                                                <div class=" container-fluid paddingLR0">
                                                    <div class=" clearfix">
                                                        <div class="header-subheader jd-font-roboto">
                                                            <div class=" editable-content-holder  ">
                                                                <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Contact Us</div>
                                                            </div>
                                                        </div>
                                                        <div class=" col-md-12 col-xs-12 paddingLR0 desc">
                                                            <div class=" col-md-6 col-xs-12 paddingLR0 store-info">
                                                                <div class="change-color-holder  not-multiple add-image ">
                                                                    <div class="change-color  change-color clearfix" style="background-color: rgb(255, 255, 255);">
                                                                        <div class=" col-md-12 col-xs-12">
                                                                            <div class=" col-md-1 col-xs-2 paddingLR0">
                                                                                <div class="editable-image-holder  ">
                                                                                    <div class="editable-content    ">
                                                                                        <div style="padding-bottom: 100%; background: rgb(255, 255, 255);">
                                                                                            <img src="https://image3.jdomni.in/banner/31072018/C6/B6/58/CB2B8B8105D35734E79C433288_1533036144752.png?output-format=webp" alt="" class=" img-loaded">
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                            <div class=" col-md-8 col-xs-12">
                                                                                <div class=" content para-1 editable-content-holder  ">
                                                                                    <div class=" font-size-20 semi-bold editable-content" style="color: rgb(158, 21, 21); min-height: auto; font-family: Cabin;">Our Office Address</div>
                                                                                </div>
                                                                                <div class=" content para-2 editable-content-holder  ">
                                                                                    <div class="   font-size-16 editable-content jd-cms-tag jd-cms-tag-company-address" style="color: rgba(58, 58, 58, 0.8); min-height: auto; font-family: Cabin;">
                                                                                        <div>Dum Dum, South Kolkata, West Bengal</div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div> 
                                                                        <div class=" col-md-12 col-xs-12">
                                                                            <div class=" col-md-1 col-xs-2 paddingLR0">
                                                                                <div class="editable-image-holder  ">
                                                                                    <div class="editable-content    ">
                                                                                        <div style="padding-bottom: 100%; background: rgb(255, 255, 255);"><img src="https://image3.jdomni.in/banner/31072018/F2/84/A6/3FD8B02CBDD85061B1C7E1DB05_1533036188916.png?output-format=webp" alt="" class=" img-loaded"></div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                            <div class=" col-md-8 col-xs-12">
                                                                                <div class=" content para-1 editable-content-holder  ">
                                                                                    <div class=" font-size-20 semi-bold editable-content" style="color: rgb(158, 21, 21); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(158, 21, 21, 0.95); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">General Enquiries</div>
                                                                                </div>
                                                                                <div class=" content para-2 editable-content-holder  ">
                                                                                    <div class="  font-size-16 editable-content jd-cms-tag jd-cms-tag-email" style="color: rgba(58, 58, 58, 0.8); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(58, 58, 58, 0.8); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">
                                                                                        <div><a href="mailto:someone@example.com">lifeshare.com</a></div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class=" col-md-12 col-xs-12">
                                                                            <div class=" col-md-1 col-xs-2 paddingLR0">
                                                                                <div class="editable-image-holder  ">
                                                                                    <div class="editable-content    ">
                                                                                        <div style="padding-bottom: 100%; background: rgb(255, 255, 255);"><img src="https://image2.jdomni.in/banner/31072018/3A/80/00/7190FC83BB56F81485EE7A68AC_1533036156489.png?output-format=webp" alt="" class=" img-loaded"></div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                            <div class=" col-md-8 col-xs-12">
                                                                                <div class=" content para-1 editable-content-holder  ">
                                                                                    <div class=" font-size-20 semi-bold editable-content" style="color: rgb(158, 21, 21); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(158, 21, 21, 0.95); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">Call Us</div>
                                                                                </div>
                                                                                <div class=" content para-2 editable-content-holder  ">
                                                                                    <div class="  font-size-16 editable-content jd-cms-tag jd-cms-tag-contact-no" style="color: rgba(58, 58, 58, 0.8); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(58, 58, 58, 0.8); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">
                                                                                        <div><a class="phoneNo-link" href="tel:+7900000009">+91-7900000009</a></div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                        <div class=" col-md-12 col-xs-12">
                                                                            <div class=" col-md-1 col-xs-2 paddingLR0">
                                                                                <div class="editable-image-holder  ">
                                                                                    <div class="editable-content    ">
                                                                                        <div style="padding-bottom: 100%; background: rgb(255, 255, 255);"><img src="https://image3.jdomni.in/banner/31072018/71/DB/A6/47BB14FD118737E11C0B583487_1533036243777.png?output-format=webp" alt="" class=" img-loaded"></div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                            <div class=" col-md-8 col-xs-12">
                                                                                <div class=" content para-1 editable-content-holder  ">
                                                                                    <div class=" font-size-20 semi-bold editable-content" style="color: rgb(158, 21, 21); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(158, 21, 21, 0.95); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">Our Timing</div>
                                                                                </div>
                                                                                <div class=" content para-2 editable-content-holder  ">
                                                                                    <div class="clearfix   font-size-16 editable-content jd-cms-tag jd-cms-tag-working-hours" style="color: rgba(58, 58, 58, 0.8); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(58, 58, 58, 0.8); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">
                                                                                        <div>
                                                                                            <span class="contact-day-holder">Mon - Sun :&nbsp;</span>
                                                                                            <span class="contact-timing-holder">24 Hours Available</span>
                                                                                        </div>
                                                                                    </div>
                                                                                </div>
                                                                            </div>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div class=" col-md-6 col-xs-12 paddingLR0 enquiry-form">
                                                                <div class="change-color-holder  not-multiple add-image ">
                                                                    <div class="change-color  change-color clearfix" style="background-color: rgb(255, 255, 255);">
                                                                        <form name=frm method=post >
                                                                        <div class="editable-content-holder col-md-10 col-xs-12 input-content ">
                                                                            <div class="editable-content edit-input  border-curved" style="min-height: auto;">
                                                                                <input type="text" class="form-control " placeholder="YOUR NAME" maxlength="50" seleniumid="sel_srcBox" name="name">
                                                                            </div>
                                                                        </div>
                                                                        <div class="editable-content-holder col-md-10 col-xs-12 input-content ">
                                                                            <div class="editable-content edit-input  border-curved" style="min-height: auto;">
                                                                                <input type="text" class="form-control " placeholder="YOUR EMAIL" seleniumid="sel_srcBox" name="email">
                                                                            </div>
                                                                        </div>
                                                                        <div class="editable-content-holder col-md-10 col-xs-12 input-content ">
                                                                            <div class="editable-content edit-input  border-curved" style="min-height: auto;">
                                                                                <input type="text" class="form-control " placeholder="YOUR CONTACT NO." maxlength="10" seleniumid="sel_srcBox" name="cnct">
                                                                            </div>
                                                                        </div>
                                                                        <div class="editable-content-holder col-md-10 col-xs-12 input-content ">
                                                                            <div class="editable-content edit-input  border-curved" style="min-height: auto;">
                                                                                <textarea rows="1" class="form-control " name="addr" placeholder="YOUR MESSAGE" seleniumid="sel_srcBox"></textarea>
                                                                            </div>
                                                                        </div>
                                                                        <div class="col-md-10 col-xs-12 paddingLR0">
                                                                            <div class="editable-content-holder editable-button align-center ">
                                                                                <div class="editable-content">
                                                                                    <input value="Submit" class="btn button contact_submit primary-btn-color  align-left btn-md btn-rounded  hoverStyle42319" style="color: rgb(255, 255, 255); overflow: hidden; position: relative; min-height: auto; border-color: rgb(191, 47, 47); background-color: rgb(191, 47, 47);" name="ok" type="submit">
                                                                                </div>
                                                                            </div>
                                                                        </div></form>''')
frm=cgi.FieldStorage()
if frm.getvalue('ok'):
    post=frm.getvalue('name')
    font=frm.getvalue('email')
    back=frm.getvalue('cnct')
    text=frm.getvalue('addr')
    try:
        cursor = config.db8.cursor()
        sql = "INSERT INTO msg(name,email,cnct,addr) VALUES ('{}','{}','{}','{}')".format(post,font,back,text)
        cursor.execute(sql)
        config.db8.commit()
        config.db8.close()
        print('''<h1 style="color:green; text-align:left; ">Uplode Successfull</h1>''')
    except Exception as e:
        print(e)
print('''
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div id="contentBlock579793435" class="edit-content  contentBlock579793435 static-templates notification-card notification notification1" data-content-block-template="notification1" data-block-id="309280811">
                                        <div class="template-main-container   notification notification1 content-align-right  " data-transparency_value=" " data-web-bg-img="" data-mob-bg-img="">
                                            <div class="custom-template  clearfix bootstrap-iso notification1 padding0">
                                                <div>
                                                    <div class=" col-md-12 notification-container" style="border-radius: 8px;">
                                                        <div class="change-color-holder  col-md-4 img-holder primary-btn-color-non-imp " style="border-radius: 8px 0px 0px 8px;">
                                                            <div class="change-color  change-color clearfix">
                                                                <div class="">
                                                                    <div class="editable-image-holder  ">
                                                                        <div class="editable-content    " style="">
                                                                            <img src="https://image3.jdomni.in/jdomni_email/headphones_1.png?output-format=webp" alt="" class=" img-loaded">
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                        <div class="change-color-holder  col-md-8 clearfix contact-holder add-image " style="border-radius: 0px 8px 8px 0px;">
                                                            <div class="change-color  change-color content-1 paddingLR0" style="background-color: rgb(255, 255, 255);">
                                                                <div class=" editable-content-holder  ">
                                                                    <div class=" font-size-22 align-left editable-content" style="color: rgb(158, 21, 21); min-height: auto; font-family: Cabin; line-height: 1.5; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Contact Us</div>
                                                                </div>
                                                                <div class=" editable-content-holder  ">
                                                                    <div class="para-1 contact-mob font-size-16 editable-content jd-cms-tag jd-cms-tag-contact-no" style="color: rgba(58, 58, 58, 0.8); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(58, 58, 58, 0.8); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">
                                                                        <div>
                                                                            <a class="phoneNo-link" href="tel:+918888888888">+91-7900000009</a>
                                                                        </div>
                                                                    </div>
                                                                </div>
                                                                <div class=" editable-content-holder  ">
                                                                    <div class=" font-size-22 align-left editable-content" style="color: rgb(158, 21, 21); min-height: auto; font-family: Cabin; line-height: 1.5; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Mail Us</div>
                                                                </div>
                                                                <div class=" editable-content-holder  ">
                                                                    <div class="para-1 contact-mail font-size-16 editable-content jd-cms-tag jd-cms-tag-email" style="color: rgba(58, 58, 58, 0.8); min-height: auto; font-family: Cabin; line-height: 1.4; border-color: rgba(58, 58, 58, 0.8); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0px; background-color: rgba(0, 0, 0, 0);">
                                                                        <div><a href="mailto:someone@example.com">lifeshare.com</a></div>
                                                                    </div>
                                                                </div>
                                                                <div class=" editable-content-holder  ">
                                                                    <div class=" font-size-22 align-left editable-content" style="color: rgb(158, 21, 21); min-height: auto; font-family: Cabin; line-height: 1.5; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);"><a href="fdbk.py"><img src="img/fdbk.png" >Feedback US</a></div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="header-subheader jd-font-roboto">
                        <div class=" editable-content-holder  ">
                            <a href="javascript:void(0)" class="link-content">
                                <div class="main-header align-center font-size-34 editable-content" style="color: rgb(191, 47, 47); min-height: auto; font-family: &quot;Abril Fatface&quot;; line-height: 1.8; border-color: rgb(158, 21, 21); border-style: none; border-width: 0px; border-radius: 0px; letter-spacing: 0.7px; background-color: rgba(0, 0, 0, 0);">Our Connections</div>
                            </a>
                        </div>
                    </div>
                    <div>
                        <iframe src="https://www.google.com/maps/d/embed?mid=179E6svgkmMm-562H789UHczgoc7yl1om" width="1900" height="480" frameborder="0"></iframe>                               
                    </div>
                    
                    <div class="footer-container footer-wrapper">
                        <section class="footer-basics shop-footer footer-background footer-doctors doctors  ">
                            <div class="footer-distributed bootstrap-iso">
                                <div class="clearfix sections bootstrap-iso">
                                    <div class="col-md-12 menu-social-links-sec">
                                        <div class="col-md-6 col-xs-12 paddingLR0 inlineBlock footer-options-cnt menu-links doctors">
                                            <div class="footer-options-cnt admin-edit-border menuLink-wrapper">
                                                <div class="footer-options " data-link-id="385093666">
                                                    <a href="https://safelifebloodbanksmumbai501.justdial.com/" class="text-color" title="Home">Home</a>
                                                </div>
                                                <div class="footer-options " data-link-id="385093667">
                                                    <a class="text-color" title="Services">SERVICES</a>
                                                </div>
                                                <div class="footer-options " data-link-id="385093668">
                                                    <a class="text-color" title="About Us">ABOUT</a>
                                                </div>
                                                <div class="footer-options " data-link-id="385093669">
                                                    <a class="text-color" title="Gallery">GALLERY</a>
                                                </div>
                                                <div class="footer-options " data-link-id="385093667">
                                                    <a class="text-color" title="Services">FACT</a>
                                                </div>
                                                <div class="footer-options " data-link-id="385093668">
                                                    <a class="text-color" title="About Us">WHY DONATE BLOOD</a>
                                                </div>
                                                <div class="footer-options " data-link-id="385093669">
                                                    <a class="text-color" title="Gallery">VIDEOS</a>
                                                    
                                                </div>
                                                <div class="footer-options " data-link-id="385093668">
                                                    <a class="text-color" title="About Us">CONTACT US</a>
                                                </div>
                                                
                                            </div>
                                        </div>
                                        <div class="col-md-6 col-xs-12 footer-options-cnt">
                                            <div class="edit-social-pos col-xs-12 col-md-12 paddingLR0 admin-edit-border account-social-wrapper">
                                                <div class="col-md-12 paddingLR0 social-icon-sec">
                                                    <div class="social-sec wrap-icons">
                                                        <a target="_blank" data-externallink="http://www.facebook.com" title="Facebook" href="http://www.facebook.com" class="sprite-fbCircle icon-fbCircle sprite_new paddingR5"></a>
                                                        <a target="_blank" data-externallink="http://www.linkedin.com" title="LinkedIn" href="http://www.linkedin.com" class="sprite-inCircle icon-inCircle sprite_new paddingR5"></a>
                                                        <a target="_blank" data-externallink="http://www.instagram.com" title="Instagram" href="http://www.instagram.com" class="sprite-instaCircle icon-instaCircle sprite_new paddingR5"></a>
                                                        <a target="_blank" data-externallink="http://www.twitter.com" title="Twitter" href="http://www.twitter.com" class="sprite-TwiterCircle icon-TwiterCircle sprite_new paddingR5"></a>
                                                        <a target="_blank" data-externallink="https://www.justdial.com" title="Justdial" href="https://www.justdial.com" class="sprite-jdNew icon-jdNew sprite_new paddingR5"></a>
                                                    </div>
                                                </div>
                                            </div>
                                            
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="divider"></div>
                            <div class="clearfix sections bootstrap-iso">
                                <div class="col-md-12 paddingLR0 padding15 copyright-applinks-section">
                                    <div class="col-md-6 col-xs-12 paddingLR0 app-img-cnt">
                                        <div class="rating-download-section">
                                            <div>
                                                <div class="footer-app footer-app-download"></div>
                                            </div>
                                            <div id="jdRating" class="jdRating "></div>
                                        </div>
                                    </div>
                                    <div class="col-md-6 col-xs-12 paddingLR0 text-right copyright-text">
                                        <div class="footer-company-name col-sm-12 paddingLR0 margin0 padding0">
                                            <div class="text-color copyright-container editable-content-holder  ">
                                                <div class="  editable-content" style="color:rgba(191, 47, 47, 1)">
                                                    Life Share Blood Banks. Team Members : Nandini Srijita Subhojit Atanu Harsh</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="footer-language-section">
                                <div class="clearfix sections bootstrap-iso">
                                    <div class="col-md-12 footer-bottom">
                                        <div class="hidden-lang-text hide" id="hiddenLangText">English </div>
                                        <div class="language-div notranslate event-disabled ">
                                            <div class="change-lang text-color"><span class="colon-sign"></span></div>
                                            <div class="lagauges">
                                                <div class="lang-change text-center selected-lang" data-lang-key="/en/en"></div>
                                                
                                                <div class="lang-change text-center" data-lang-key="/en/ta">Life Share Blood Bank</div>
                                                
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
                        <a href="https://api.whatsapp.com/send?phone=918013530481&amp;forceIntent=true&amp;load=loadInIOSExternalSafari" target="_blank">
                            <div class="whatsappWidget widgetPosition-Bottom-Right">
                                <img src="https://image1.jdomni.in/jdomni_email/whatsapp_popup_2011271203.png?output-format=webp" class="whatsappIcon">
                            </div>
                        </a>

                    </div>
                    <section id="ToastMessage" class="hide toast-message">
                        <div class="backdrop">
                            <div class="toast-text"></div>
                        </div>
                    </section>
                    <div class="modal search-form" tabindex="-1" role="dialog" id="searchForm">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content"></div>
                        </div>
                    </div>
                    <div id="google_translate_element"></div>
                    <div class="custom-modal  modal fade  " tabindex="-1" role="dialog">
                        <div class="modal-dialog ">
                            <div class="modal-content">
                                <div class="custom-modal-header"></div>
                                <div class="custom-modal-body">
                                    <div class="text-center"></div>
                                </div>
                                <div class="custom-modal-footer padding0"></div>
                            </div>
                        </div>
                    </div>
                    <div class="custom-modal-backdrop"></div>
        </div>
    </div>
    <span class="footer-customcode-holder"></span>
        
        <div class="raf-scroll-helper" style="position:absolute;z-index:-1;width:0px;height:0px"></div>
        <span></span>
        
        <div id="topcontrol" title="Scroll Back to Top" style="position: fixed; bottom: 136px; right: 16px; opacity: 1; cursor: pointer; z-index: 101;">
            <a href="#top"><i class="icon-pagination-up up-icon"></i></a>
        </div>
        
        
        
    </body>
</html>''')

