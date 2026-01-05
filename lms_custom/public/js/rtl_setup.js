// RTL Setup for Arabic Language
// Automatically sets HTML direction and lang attributes

frappe.ready(function () {
	// Check if current language is Arabic
	const lang = frappe.boot.lang || 'en';

	if (lang === 'ar' || lang.startsWith('ar')) {
		// Set HTML attributes
		document.documentElement.setAttribute('lang', 'ar');
		document.documentElement.setAttribute('dir', 'rtl');

		// Add RTL class to body for additional styling
		document.body.classList.add('rtl');

		console.log('[rtl_setup.js] method: frappe.ready - RTL enabled for Arabic');
	}
});

// Also run on page load for non-Frappe pages
if (document.readyState === 'loading') {
	document.addEventListener('DOMContentLoaded', function () {
		setRTL();
	});
} else {
	setRTL();
}

function setRTL() {
	// Check HTML lang attribute or browser language
	const htmlLang = document.documentElement.lang;
	const browserLang = navigator.language || navigator.userLanguage;

	if (
		htmlLang === 'ar' ||
		htmlLang.startsWith('ar-') ||
		browserLang === 'ar' ||
		browserLang.startsWith('ar-')
	) {
		document.documentElement.setAttribute('lang', 'ar');
		document.documentElement.setAttribute('dir', 'rtl');
		document.body.classList.add('rtl');

		console.log('[rtl_setup.js] method: setRTL - RTL enabled');
	}
}
