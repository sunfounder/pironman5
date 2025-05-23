function changeLanguage() {

    let supportLangs = {
        'en': ['This documentation is also available in', 'English', 'Never show again'],
        'de': ['Diese Dokumentation ist auch in', 'Deutsch', 'Nie wieder anzeigen'],
        'ja': ['このドキュメントは', '日本語', '今後表示しない'],
        'fr': ['Cette documentation est également disponible en', 'Français', 'Ne plus afficher'],
        'es': ['Esta documentación también está disponible en', 'español', 'No mostrar de nuevo'],
        'it': ['Questa documentazione è disponibile anche in', 'Italiano', 'Non mostrare più'],
    };

    let svgIcon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="40" height="40"><defs><style>.cls-1{fill:#6fabe6}.cls-2{fill:#dad7e5}.cls-3{fill:#edebf2}.cls-4{fill:#7c7d7d}</style></defs><g id="Global_language" data-name="Global language"><path class="cls-1" d="M21 44.78V31a2 2 0 0 0-2-2H3.6A21 21 0 0 1 26.08 3.1c.31 0 .61.06.92.11V17a2 2 0 0 0 2 2h15.4C48 33.82 35.18 47.07 21 44.78z"/><rect class="cls-2" x="27" y="1" width="20" height="18" rx="2"/><path class="cls-3" d="M47 3v14C36.07 17 30 9 30 1h15a2 2 0 0 1 2 2z"/><rect class="cls-2" x="1" y="29" width="20" height="18" rx="2"/><path class="cls-3" d="M21 31v14C10.07 45 4 37 4 29h15a2 2 0 0 1 2 2z"/><path class="cls-4" d="M41.93 14.63C37.59 3.79 37.93 4 37 4s-.55-.32-4.93 10.63a1 1 0 0 0 1.86.74C35 12.61 34.83 13 35 13h4.11c.84 2.1 1 3 1.89 3a1 1 0 0 0 .93-1.37zM35.68 11 37 7.69 38.32 11zM15 34h-3v-1a1 1 0 0 0-2 0v1H7a1 1 0 0 0 0 2h5.89A7.22 7.22 0 0 1 11 39.46a9.42 9.42 0 0 1-.84-1 1 1 0 0 0-1.64 1.14 11.28 11.28 0 0 0 1 1.24 14.16 14.16 0 0 1-2 1.3 1 1 0 0 0 .9 1.78A15.21 15.21 0 0 0 11 42.2a15 15 0 0 0 2.55 1.69 1 1 0 0 0 .9-1.78 14.16 14.16 0 0 1-2-1.29A9 9 0 0 0 14.93 36a1 1 0 1 0 .07-2z"/><path d="M37 40.47a20.87 20.87 0 0 1-16 1.66V31a2 2 0 0 0-2-2H7.2a21 21 0 0 1 6.69-23.41 21.14 21.14 0 0 1 9-2.57 23.35 23.35 0 0 1 3.17.09C27 3.11 25 3.16 25 5v14a2 2 0 0 0 2 2h16a2 2 0 0 0 1.64-.85A20.91 20.91 0 0 1 37 40.47z" style="fill:#82bcf4"/><path class="cls-1" d="M34 25a35.63 35.63 0 0 1-2.34 11.84 16.93 16.93 0 0 1 5 3.79c.07.1.19 0-.74.67-.28.19-.56.38-.85.55a15.27 15.27 0 0 0-4.18-3.16 36.1 36.1 0 0 1-3.43 6c-4.59.51-1.84.82 1.58-6.83a14.7 14.7 0 0 0-7.83-.62c-.27 0-.19.31-.19-2a16.57 16.57 0 0 1 8.78.76A33.82 33.82 0 0 0 32 25H16a34.57 34.57 0 0 0 .32 4h-2a32.87 32.87 0 0 1-.32-4H3v-2h11a35.63 35.63 0 0 1 2.34-11.84 16.6 16.6 0 0 1-5.04-3.87A18.11 18.11 0 0 1 13 6.15a15.27 15.27 0 0 0 4.18 3.16 36.1 36.1 0 0 1 3.43-6c4.58-.51 1.84-.83-1.58 6.83a14.51 14.51 0 0 0 8 .6v2a16.57 16.57 0 0 1-8.81-.74A33.82 33.82 0 0 0 16 23h16a30.3 30.3 0 0 0-.31-3.85c0-.21-.25-.15 2-.15a32.87 32.87 0 0 1 .31 4h11v2z"/></g></svg>';

    let pathname = window.location.pathname;
    let pageLang = "";
    if (pathname.split('/').length >= 4) {
        pageLang = pathname.split('/')[3];
    }
    let browserLang = navigator.language || navigator.userLanguage;
    browserLang = browserLang.substr(0, 2);

    // Check if the current language is the same as the browser language
    if (pageLang !== browserLang) {
        // Check if the current language is supported
        if (Object.keys(supportLangs).indexOf(browserLang) !== -1) {
            // Check if the current page is the default page, if so, redirect to the browser language
            if (pageLang === "") {
                newLink = window.location.protocol + '//' + window.location.host + pathname + browserLang + '/latest';
                window.location.href = newLink;
            } else {
                if (localStorage.getItem('neverShowAgain') === 'true') {
                    return;
                }
                // Create link
                var link = window.location.protocol + '//' + window.location.host + pathname.replace('/' + pageLang + '/', '/' + browserLang + '/');

                // Create notification
                var notification = document.createElement('div');
                notification.id = 'notification';
                notification.style.cssText = `
                    position: fixed;
                    top: 4px;
                    right: 4px;
                    width: 300px;
                    border-radius: 10px;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
                    z-index: 9999;
                    padding: 12px;
                    font-size: 14px;
                    line-height: 1.5;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    color: #333;
                    display: flex;
                    align-items: center;
                `;

                let svgContainer = document.createElement('div');
                svgContainer.innerHTML = svgIcon;
                svgContainer.style.cssText = 'display: inline-block; vertical-align: middle;';

                var text = document.createElement('p');
                text.style.cssText = 'margin: 0; display: inline-block; vertical-align: middle;';

                text.innerHTML = supportLangs[browserLang][0] + ' <a href="' + link + '">' + supportLangs[browserLang][1] + '</a>';

                var textAndButtonContainer = document.createElement('div');
                textAndButtonContainer.style.cssText = `
                    display: inline-block;
                    vertical-align: middle;
                    width: calc(100% - 40px);
                    padding-left: 10px;
                `;

                var closeButton = document.createElement('button');
                closeButton.style.cssText = `
                    position: absolute;
                    top: 4px;
                    right: 4px;
                    width: 16px;
                    height: 16px;
                    background-color: transparent;
                    border: 0;
                    font-size: 16px;
                    line-height: 1;
                    color: #999;
                    cursor: pointer;
                `;
                closeButton.innerHTML = '×';
                closeButton.onclick = function () {
                    document.body.removeChild(notification);
                };

                // Create never-show button
                var neverShowButton = document.createElement('button');
                neverShowButton.style.cssText = `
                    width: 100%;
                    text-align: end;
                    background-color: transparent;
                    border: 0;
                    font-size: 12px;
                    line-height: 1;
                    color: #999;
                    cursor: pointer;
                `;
                neverShowButton.innerHTML = supportLangs[browserLang][2];
                neverShowButton.onclick = function () {
                    localStorage.setItem('neverShowAgain', 'true');
                    document.body.removeChild(notification);
                };

                textAndButtonContainer.appendChild(text);
                textAndButtonContainer.appendChild(neverShowButton);

                notification.appendChild(svgContainer);
                notification.appendChild(textAndButtonContainer);
                notification.appendChild(closeButton);

                document.body.appendChild(notification);
            }
        }
    }
}

window.addEventListener('load', changeLanguage);
