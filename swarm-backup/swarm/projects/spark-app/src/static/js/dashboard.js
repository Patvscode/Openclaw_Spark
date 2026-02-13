// dashboard.js
// Vanilla JS dashboard for Spark App
// Loads agent status, task queue, and recent findings.
// Auto-refreshes every 30 seconds.
// Provides a createTask function to POST a new task.

// Utility to create an element with optional classes and innerHTML
function createEl(tag, options = {}) {
  const el = document.createElement(tag);
  if (options.classes) el.className = options.classes;
  if (options.html) el.innerHTML = options.html;
  if (options.text) el.textContent = options.text;
  if (options.attrs) {
    for (const [k, v] of Object.entries(options.attrs)) el.setAttribute(k, v);
  }
  return el;
}

// Render agent status cards
function loadStatus() {
  const container = document.getElementById('status-cards');
  if (!container) return;
  container.innerHTML = '<p>Loading agent status...</p>';
  fetch('/api/status')
    .then(res => res.json())
    .then(data => {
      container.innerHTML = '';
      if (!Array.isArray(data) || data.length === 0) {
        container.textContent = 'No agent status available.';
        return;
      }
      data.forEach(agent => {
        const card = createEl('div', {classes: 'agent-card'});
        card.appendChild(createEl('h3', {text: agent.name || 'Unnamed'}));
        card.appendChild(createEl('p', {text: `Status: ${agent.status || 'unknown'}`}));
        if (agent.lastUpdated) {
          card.appendChild(createEl('p', {text: `Last Updated: ${new Date(agent.lastUpdated).toLocaleString()}`}));
        }
        container.appendChild(card);
      });
    })
    .catch(err => {
      console.error('Error loading agent status:', err);
      container.textContent = 'Error loading agent status.';
    });
}

// Render task queue
function loadTasks() {
  const container = document.getElementById('task-queue');
  if (!container) return;
  container.innerHTML = '<p>Loading task queue...</p>';
  fetch('/api/tasks')
    .then(res => res.json())
    .then(data => {
      container.innerHTML = '';
      if (!Array.isArray(data) || data.length === 0) {
        container.textContent = 'No tasks in queue.';
        return;
      }
      const list = createEl('ul');
      data.forEach(task => {
        const item = createEl('li');
        item.textContent = `[#${task.id}] ${task.type || 'Unknown'} - ${task.status || 'pending'}`;
        if (task.queuedAt) {
          item.appendChild(createEl('span', {text: ` (Queued: ${new Date(task.queuedAt).toLocaleTimeString()})`}));
        }
        list.appendChild(item);
      });
      container.appendChild(list);
    })
    .catch(err => {
      console.error('Error loading tasks:', err);
      container.textContent = 'Error loading task queue.';
    });
}

// Render recent findings
function loadFindings() {
  const container = document.getElementById('recent-findings');
  if (!container) return;
  container.innerHTML = '<p>Loading recent findings...</p>';
  fetch('/api/findings')
    .then(res => res.json())
    .then(data => {
      container.innerHTML = '';
      if (!Array.isArray(data) || data.length === 0) {
        container.textContent = 'No recent findings.';
        return;
      }
      const table = createEl('table', {classes: 'findings-table'});
      const header = createEl('tr');
      header.appendChild(createEl('th', {text: 'ID'}));
      header.appendChild(createEl('th', {text: 'Title'}));
      header.appendChild(createEl('th', {text: 'Severity'}));
      header.appendChild(createEl('th', {text: 'Date'}));
      table.appendChild(header);
      data.forEach(fnd => {
        const row = createEl('tr');
        row.appendChild(createEl('td', {text: fnd.id}));
        row.appendChild(createEl('td', {text: fnd.title || ''}));
        row.appendChild(createEl('td', {text: fnd.severity || ''}));
        row.appendChild(createEl('td', {text: fnd.date ? new Date(fnd.date).toLocaleDateString() : ''}));
        table.appendChild(row);
      });
      container.appendChild(table);
    })
    .catch(err => {
      console.error('Error loading findings:', err);
      container.textContent = 'Error loading recent findings.';
    });
}

// Auto-refresh every 30 seconds
function startAutoRefresh() {
  setInterval(() => {
    loadStatus();
    loadTasks();
    loadFindings();
  }, 30000);
}

// Create a new task via POST
function createTask(taskData) {
  return fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(taskData),
  })
    .then(res => {
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json();
    })
    .then(created => {
      console.log('Task created:', created);
      loadTasks();
      return created;
    })
    .catch(err => {
      console.error('Error creating task:', err);
      throw err;
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  loadStatus();
  loadTasks();
  loadFindings();
  startAutoRefresh();
});
