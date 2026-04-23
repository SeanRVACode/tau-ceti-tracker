import './RunsTable.css'

function formatDate(iso) {
  if (!iso) return '---'
  const d = new Date(iso)
  return d.toLocaleDateString('en-US', { month: '2-digit', day: '2-digit', year: '2-digit' })
    + ' ' + d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: false })
}

function Bool({ val }) {
  return <span className={val ? 'bool-yes' : 'bool-no'}>{val ? 'YES' : 'NO'}</span>
}

export default function RunsTable({ runs, loading, error, onEdit, onDelete }) {
  return (
    <section className="runs-section">
      <div className="panel-header">
        <span className="panel-tag">// RUN LOG</span>
        <span className="panel-count">{runs.length} ENTR{runs.length === 1 ? 'Y' : 'IES'}</span>
      </div>

      {error && <p className="runs-error">[ERR] {error}</p>}

      {loading && <p className="runs-loading">[ FETCHING DATA... ]</p>}

      {!loading && runs.length === 0 && !error && (
        <p className="runs-empty">NO RUNS LOGGED. DEPLOY A RUNNER.</p>
      )}

      {runs.length > 0 && (
        <div className="table-wrap">
          <table className="runs-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>DATE</th>
                <th>SHELL</th>
                <th>MAP</th>
                <th>EXFILED</th>
                <th>EXFIL AMT</th>
                <th>RUNNER DOWNS</th>
                <th>UESC ELIMS</th>
                <th>REZZED</th>
                <th>ROOK FRIENDS</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {runs.map(run => (
                <tr key={run.id} className="run-row">
                  <td className="td-id">#{run.id}</td>
                  <td className="td-date">{formatDate(run.date)}</td>
                  <td className="td-shell">{run.shell.toUpperCase()}</td>
                  <td>{run.map_name.toUpperCase()}</td>
                  <td><Bool val={run.exfiled} /></td>
                  <td>{run.exfil_amount.toLocaleString()}</td>
                  <td>{run.runner_downs}</td>
                  <td>{run.uesc_elims}</td>
                  <td>{run.team_mates_rezzed}</td>
                  <td><Bool val={run.rook_friends} /></td>
                  <td className="td-actions">
                    <button className="btn btn--small" onClick={() => onEdit(run)}>EDIT</button>
                    <button className="btn btn--small btn--danger" onClick={() => onDelete(run.id)}>DEL</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  )
}
