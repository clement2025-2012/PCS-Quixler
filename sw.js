/**
 * ==============================================================================
 * PCS QUIXLER - MASTER SERVICE WORKER v40.0
 * Combines Adsterra Push Notifications with PWA Offline Caching Capabilities.
 * Optimized for Render.com deployment.
 * ==============================================================================
 */

// ------------------------------------------------------------------------------
// 1. ADSTERRA PUSH NOTIFICATIONS PROVIDER
// ------------------------------------------------------------------------------
self.options = {
    "domain": "5gvci.com",
    "zoneId": 10717792
};
self.lary = "";

// Import Adsterra's service worker logic safely. 
// If an adblocker blocks it, it fails silently instead of crashing your site.
try {
    importScripts('https://5gvci.com/act/files/service-worker.min.js?r=sw');
    console.log('[PCS ServiceWorker] Adsterra Push Provider Loaded Successfully.');
} catch (e) {
    console.log('[PCS ServiceWorker] Adsterra Push Provider blocked by client environment.');
}

// ------------------------------------------------------------------------------
// 2. PCS QUIXLER PWA CACHING & OFFLINE ENGINE
// ------------------------------------------------------------------------------
const CACHE_NAME = 'pcs-quixler-cache-v40';

const CORE_ASSETS = [
    './',
    './index.html',
    './style.css',
    './app.js',
    './manifest.json',
    './PCS-Seal.jpg' // Caching the logo so it appears offline
];

self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            console.log('[PCS ServiceWorker] Caching Core Assets for Offline Mode');
            return cache.addAll(CORE_ASSETS);
        })
    );
    self.skipWaiting(); // Force the waiting service worker to become the active service worker
});

self.addEventListener('activate', function(event) {
    event.waitUntil(
        caches.keys().then(function(cacheNames) {
            return Promise.all(
                cacheNames.map(function(cacheName) {
                    if (cacheName !== CACHE_NAME) {
                        console.log('[PCS ServiceWorker] Clearing Old Cache Payload:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

self.addEventListener('fetch', function(event) {
    // 🛑 CRITICAL STABILITY FIX: 
    // Only cache our own app files. Ignore Adsterra, AdSense, and external APIs.
    // If we try to cache Adsterra, the browser throws a CORS error and breaks the app.
    if (event.request.method !== 'GET' || !event.request.url.startsWith(self.location.origin)) {
        return; 
    }

    event.respondWith(
        caches.match(event.request).then(function(cachedResponse) {
            if (cachedResponse) {
                return cachedResponse; // Serve instantly from Cache
            }
            return fetch(event.request).then(function(networkResponse) {
                // Ensure response is valid before caching
                if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
                    return networkResponse;
                }
                const responseClone = networkResponse.clone();
                caches.open(CACHE_NAME).then(function(cache) {
                    cache.put(event.request, responseClone);
                });
                return networkResponse;
            }).catch(function() {
                console.log('[PCS ServiceWorker] Network Offline. User is playing from Cache.');
            });
        })
    );
});