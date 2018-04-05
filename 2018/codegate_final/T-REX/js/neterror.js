// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

function toggleHelpBox() {
  var helpBoxOuter = document.getElementById('details');
  helpBoxOuter.classList.toggle(HIDDEN_CLASS);
  var detailsButton = document.getElementById('details-button');
  if (helpBoxOuter.classList.contains(HIDDEN_CLASS))
    detailsButton.innerText = detailsButton.detailsText;
  else
    detailsButton.innerText = detailsButton.hideDetailsText;

  // Details appears over the main content on small screens.
  if (mobileNav) {
    document.getElementById('main-content').classList.toggle(HIDDEN_CLASS);
    var runnerContainer = document.querySelector('.runner-container');
    if (runnerContainer) {
      runnerContainer.classList.toggle(HIDDEN_CLASS);
    }
  }
}

function diagnoseErrors() {
// <if expr="not chromeos">
    if (window.errorPageController)
      errorPageController.diagnoseErrorsButtonClick();
// </if>
// <if expr="chromeos">
  var extensionId = 'idddmepepmjcgiedknnmlbadcokidhoa';
  var diagnoseFrame = document.getElementById('diagnose-frame');
  diagnoseFrame.innerHTML =
      '<iframe src="chrome-extension://' + extensionId +
      '/index.html"></iframe>';
// </if>
}

// Subframes use a different layout but the same html file.  This is to make it
// easier to support platforms that load the error page via different
// mechanisms (Currently just iOS).
if (window.top.location != window.location)
  document.documentElement.setAttribute('subframe', '');

// Re-renders the error page using |strings| as the dictionary of values.
// Used by NetErrorTabHelper to update DNS error pages with probe results.
function updateForDnsProbe(strings) {
  var context = new JsEvalContext(strings);
  jstProcess(context, document.getElementById('t'));
}

// Given the classList property of an element, adds an icon class to the list
// and removes the previously-
function updateIconClass(classList, newClass) {
  var oldClass;

  if (classList.hasOwnProperty('last_icon_class')) {
    oldClass = classList['last_icon_class'];
    if (oldClass == newClass)
      return;
  }

  classList.add(newClass);
  if (oldClass !== undefined)
    classList.remove(oldClass);

  classList['last_icon_class'] = newClass;

  if (newClass == 'icon-offline') {
    document.body.classList.add('offline');
    new Runner('.interstitial-wrapper');
  } else {
    document.body.classList.add('neterror');
  }
}

// Does a search using |baseSearchUrl| and the text in the search box.
function search(baseSearchUrl) {
  var searchTextNode = document.getElementById('search-box');
  document.location = baseSearchUrl + searchTextNode.value;
  return false;
}

// Use to track clicks on elements generated by the navigation correction
// service.  If |trackingId| is negative, the element does not come from the
// correction service.
function trackClick(trackingId) {
  // This can't be done with XHRs because XHRs are cancelled on navigation
  // start, and because these are cross-site requests.
  if (trackingId >= 0 && errorPageController)
    errorPageController.trackClick(trackingId);
}

// Called when an <a> tag generated by the navigation correction service is
// clicked.  Separate function from trackClick so the resources don't have to
// be updated if new data is added to jstdata.
function linkClicked(jstdata) {
  trackClick(jstdata.trackingId);
}

// Implements button clicks.  This function is needed during the transition
// between implementing these in trunk chromium and implementing them in
// iOS.
function reloadButtonClick(url) {
  if (window.errorPageController) {
    errorPageController.reloadButtonClick();
  } else {
    location = url;
  }
}

function showSavedCopyButtonClick() {
  if (window.errorPageController) {
    errorPageController.showSavedCopyButtonClick();
  }
}

function downloadButtonClick() {
  if (window.errorPageController) {
    errorPageController.downloadButtonClick();
    var downloadButton = document.getElementById('download-button');
    downloadButton.disabled = true;
    downloadButton.textContent = downloadButton.disabledText;
  }
}

function detailsButtonClick() {
  if (window.errorPageController)
    errorPageController.detailsButtonClick();
}

/**
 * Replace the reload button with the Google cached copy suggestion.
 */
function setUpCachedButton(buttonStrings) {
  var reloadButton = document.getElementById('reload-button');

  reloadButton.textContent = buttonStrings.msg;
  var url = buttonStrings.cacheUrl;
  var trackingId = buttonStrings.trackingId;
  reloadButton.onclick = function(e) {
    e.preventDefault();
    trackClick(trackingId);
    if (window.errorPageController) {
      errorPageController.trackCachedCopyButtonClick();
    }
    location = url;
  };
  reloadButton.style.display = '';
  document.getElementById('control-buttons').hidden = false;
}

var primaryControlOnLeft = true;
// <if expr="is_macosx or is_ios or is_linux or is_android">
primaryControlOnLeft = false;
// </if>

function onDocumentLoad() {
  var controlButtonDiv = document.getElementById('control-buttons');
  var reloadButton = document.getElementById('reload-button');
  var detailsButton = document.getElementById('details-button');
  var showSavedCopyButton = document.getElementById('show-saved-copy-button');
  var downloadButton = document.getElementById('download-button');

  /* var reloadButtonVisible = loadTimeData.valueExists('reloadButton') &&
      loadTimeData.getValue('reloadButton').msg;
  var showSavedCopyButtonVisible =
      loadTimeData.valueExists('showSavedCopyButton') &&
      loadTimeData.getValue('showSavedCopyButton').msg;
  var downloadButtonVisible =
      loadTimeData.valueExists('downloadButton') &&
      loadTimeData.getValue('downloadButton').msg; */

  var primaryButton, secondaryButton;
  if (showSavedCopyButton.primary) {
    primaryButton = showSavedCopyButton;
    secondaryButton = reloadButton;
  } else {
    primaryButton = reloadButton;
    secondaryButton = showSavedCopyButton;
  }

  // Sets up the proper button layout for the current platform.
  if (primaryControlOnLeft) {
    buttons.classList.add('suggested-left');
    controlButtonDiv.insertBefore(secondaryButton, primaryButton);
  } else {
    buttons.classList.add('suggested-right');
    controlButtonDiv.insertBefore(primaryButton, secondaryButton);
  }

  // Check for Google cached copy suggestion.
  /* if (loadTimeData.valueExists('cacheButton')) {
    setUpCachedButton(loadTimeData.getValue('cacheButton'));
  } */ 

  if (reloadButton.style.display == 'none' &&
      showSavedCopyButton.style.display == 'none' &&
      downloadButton.style.display == 'none') {
    detailsButton.classList.add('singular');
  }

  // Show control buttons.
  /* if (reloadButtonVisible || showSavedCopyButtonVisible ||
      downloadButtonVisible) {
    controlButtonDiv.hidden = false;

    // Set the secondary button state in the cases of two call to actions.
    if ((reloadButtonVisible || downloadButtonVisible) &&
        showSavedCopyButtonVisible) {
      secondaryButton.classList.add('secondary-button');
    }
  } */
  new Runner('.interstitial-wrapper');
}

document.addEventListener('DOMContentLoaded', onDocumentLoad);
