import { useState, useEffect } from 'react'
import { SHELLS, MAPS } from '../api/client'
import './EditRunModal.css'

export default function EditRunModal({ run, onSave, onClose }) {
  const [form, setForm] = useState({})
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    if (run) setForm({ ...run })
  }, [run])

  if (!run) return null

  function handleChange(e) {
    const { name, value, type, checked } = e.target
    setForm(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : type === 'number' ? Number(value) : value,
    }))
  }

  async function handleSubmit(e) {
    e.preventDefault()
    setError(null)
    setSubmitting(true)
    try {
      await onSave(run.id, form)
      onClose()
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <div className="modal-header">
          <span>// EDIT RUN #{run.id}</span>
          <button className="modal-close" onClick={onClose}>[ X ]</button>
        </div>

        {error && <p className="form-error">[ERR] {error}</p>}

        <form onSubmit={handleSubmit}>
          <div className="form-grid">
            <div className="form-field">
              <label>SHELL</label>
              <select name="shell" value={form.shell || ''} onChange={handleChange}>
                {SHELLS.map(s => <option key={s} value={s}>{s.toUpperCase()}</option>)}
              </select>
            </div>

            <div className="form-field">
              <label>MAP</label>
              <select name="map_name" value={form.map_name || ''} onChange={handleChange}>
                {MAPS.map(m => <option key={m} value={m}>{m.toUpperCase()}</option>)}
              </select>
            </div>

            <div className="form-field">
              <label>RUNNER DOWNS</label>
              <input type="number" name="runner_downs" min="0"
                value={form.runner_downs ?? 0} onChange={handleChange} />
            </div>

            <div className="form-field">
              <label>UESC ELIMS</label>
              <input type="number" name="uesc_elims" min="0"
                value={form.uesc_elims ?? 0} onChange={handleChange} />
            </div>

            <div className="form-field">
              <label>TEAM MATES REZZED</label>
              <input type="number" name="team_mates_rezzed" min="0"
                value={form.team_mates_rezzed ?? 0} onChange={handleChange} />
            </div>

            <div className="form-field">
              <label>EXFIL AMOUNT</label>
              <input type="number" name="exfil_amount" min="0"
                value={form.exfil_amount ?? 0} onChange={handleChange} />
            </div>

            <div className="form-field form-field--check">
              <label>
                <input type="checkbox" name="exfiled"
                  checked={form.exfiled ?? false} onChange={handleChange} />
                EXFILED
              </label>
            </div>

            <div className="form-field form-field--check">
              <label>
                <input type="checkbox" name="rook_friends"
                  checked={form.rook_friends ?? false} onChange={handleChange} />
                ROOK FRIENDS
              </label>
            </div>
          </div>

          <div className="modal-actions">
            <button type="button" className="btn btn--small" onClick={onClose}>CANCEL</button>
            <button type="submit" className="btn btn--primary btn--small" disabled={submitting}>
              {submitting ? 'SAVING...' : '[ SAVE CHANGES ]'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
