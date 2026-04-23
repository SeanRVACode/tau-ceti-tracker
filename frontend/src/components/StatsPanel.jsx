import './StatsPanel.css'

function StatCard({ label, value, accent }) {
  return (
    <div className={`stat-card ${accent ? 'stat-card--accent' : ''}`}>
      <div className="stat-label">{label}</div>
      <div className="stat-value">{value ?? '---'}</div>
    </div>
  )
}

export default function StatsPanel({ stats, loading, error }) {
  return (
    <section className="stats-panel">
      <div className="panel-header">
        <span className="panel-tag">// AGGREGATE STATS</span>
      </div>

      {error && <p className="stats-error">[ERR] {error}</p>}

      <div className="stats-grid">
        <StatCard label="TOTAL RUNS"    value={loading ? '...' : stats?.total_runs} />
        <StatCard label="EXFIL RATE"    value={loading ? '...' : stats?.exfil_rate} accent />
        <StatCard label="TOTAL ELIMS"   value={loading ? '...' : stats?.total_elims} />
        <StatCard label="K/D RATIO"     value={loading ? '...' : stats?.kd_ratio} accent />
      </div>
    </section>
  )
}
