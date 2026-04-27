const BASE = '/api'

async function request(path, options = {}) {
  const res = await fetch(`${BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    credentials: 'include',
    ...options,
  })
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: res.statusText }))
    throw new Error(err.detail || 'Request failed')
  }
  return res.json()
}

export const api = {
  checkAuth:  ()        => request('/auth/me'),
  logout:     ()        => request('/auth/logout'),
  getStats:   ()        => request('/stats'),
  getAllRuns:  ()        => request('/all_runs'),
  createRun:  (data)    => request('/run', { method: 'POST', body: JSON.stringify(data) }),
  editRun:    (id, data)=> request(`/run_edit/${id}`, { method: 'PATCH', body: JSON.stringify(data) }),
  deleteRun:  (id)      => request(`/delete_run/${id}`, { method: 'DELETE' }),
}

export const SHELLS = ['assassin', 'destroyer', 'triage', 'vandal', 'thief', 'rook', 'recon']
export const MAPS   = ['perimeter', 'dire marsh', 'outpost', 'cryo archive']
