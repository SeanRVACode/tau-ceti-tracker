import { useState, useEffect, useCallback } from 'react'
import { api } from './api/client'
import Header from './components/Header'
import StatsPanel from './components/StatsPanel'
import AddRunForm from './components/AddRunForm'
import RunsTable from './components/RunsTable'
import EditRunModal from './components/EditRunModal'
import './App.css'

export default function App() {
  const [stats, setStats]       = useState(null)
  const [runs, setRuns]         = useState([])
  const [loading, setLoading]   = useState(true)
  const [statsErr, setStatsErr] = useState(null)
  const [runsErr, setRunsErr]   = useState(null)
  const [editRun, setEditRun]   = useState(null)

  const fetchAll = useCallback(async () => {
    setLoading(true)
    setStatsErr(null)
    setRunsErr(null)

    const [statsRes, runsRes] = await Promise.allSettled([
      api.getStats(),
      api.getAllRuns(),
    ])

    if (statsRes.status === 'fulfilled') setStats(statsRes.value)
    else setStatsErr(statsRes.reason.message)

    if (runsRes.status === 'fulfilled') setRuns(runsRes.value)
    else setRunsErr(runsRes.reason.message)

    setLoading(false)
  }, [])

  useEffect(() => { fetchAll() }, [fetchAll])

  async function handleCreateRun(data) {
    await api.createRun(data)
    await fetchAll()
  }

  async function handleEditRun(id, data) {
    await api.editRun(id, data)
    await fetchAll()
  }

  async function handleDeleteRun(id) {
    await api.deleteRun(id)
    await fetchAll()
  }

  return (
    <>
      <Header />
      <main className="main">
        <StatsPanel stats={stats} loading={loading} error={statsErr} />
        <AddRunForm onRunAdded={handleCreateRun} />
        <RunsTable
          runs={runs}
          loading={loading}
          error={runsErr}
          onEdit={setEditRun}
          onDelete={handleDeleteRun}
        />
      </main>
      <footer className="footer">
        <span>TAU CETI FIELD OPS // CLASSIFIED</span>
        <span>SYS v0.1.0</span>
      </footer>

      <EditRunModal
        run={editRun}
        onSave={handleEditRun}
        onClose={() => setEditRun(null)}
      />
    </>
  )
}
