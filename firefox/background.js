browser.contextMenus.create({
  id: 'shpeak',
  title: 'Speak selection',
  contexts: ["selection"]
});

browser.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId !== 'shpeak') return;
  fetch('http://localhost:9253/say', {
    method: 'POST',
    headers: new Headers({'content-type': 'application/json'}),
    body: JSON.stringify({ to_say: info.selectionText || 'Please select some text for me to read' }),
  })
});
