import { useState } from 'react'
import { SHELLS, MAPS } from '../api/client'
import './AddRunForm.css'

const defaultForm = {
  shell: '',
  map_name: '',
  exfiled: false,
  exfil_amount: 0,
  uesc_elims: 0,
  rook_friends: false,
  team_mates_rezzed: 0,
  runner_downs: 0,
}

export default function AddRunForm({ onRunAdded }) {
  const [form, setForm] = useState(defaultForm)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState(null)
  const [open, setOpen] = useState(false)

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
    if (!form.shell || !form.map_name) {
      setError('Shell and map are required.')
      return
    }
    setSubmitting(true)
    try {
      await onRunAdded(form)
      setForm(defaultForm)
      setOpen(false)
    } catch (err) {
      setError(err.message)
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div className="add-run-wrapper">
      <button className="btn btn--primary" onClick={() => setOpen(o => !o)}>
        {open ? '[ CANCEL ]' : '[ + LOG NEW RUN ]'}
      </button>

      {open && (
        <form className="add-run-form" onSubmit={handleSubmit}>
          <div className="form-header">// FIELD RUN LOG ENTRY</div>

          {error && <p className="form-error">[ERR] {error}</p>}

          <div className="form-grid">
            <div className="form-field">
              <label>SHELL</label>
              <select name="shell" value={form.shell} onChange={handleChange}>
                <option value="">-- select --</option>
                {SHELLS.map(s => <option key={s} value={s}>{s.toUpperCase()}</option>)}
              </select>
            </div>

            <div className="form-field">
              <label>MAP</label>
              <select name="map_name" value={form.map_name} onChange={handleChange}>
                <option value="">-- select --</option>
                {MAPS.map(m => <option key={m} value={m}>{m.toUpperCase()}</option>)}
              </select>
            </div>

            <div className="form-field">
              <label>RUNNER DOWNS</label>
              <input type="number" name="runner_downs" min="0"
                value={form.runner_downs} onChange={handleChange} />
            </div>

            <div className="form-field">
              <label>UESC ELIMS</label>
              <input type="number" name="uesc_elims" min="0"
                value={form.uesc_elims} onChange={handleChange} />
            </div>

            <div className="form-field">
              <label>TEAM MATES REZZED</label>
              <input type="number" name="team_mates_rezzed" min="0"
                value={form.team_mates_rezzed} onChange={handleChange} />
            </div>

            <div className="form-field">
              <label>EXFIL AMOUNT</label>
              <input type="number" name="exfil_amount" min="0"
                value={form.exfil_amount} onChange={handleChange} />
            </div>

            <div className="form-field form-field--check">
              <label>
                <input type="checkbox" name="exfiled"
                  checked={form.exfiled} onChange={handleChange} />
                EXFILED
              </label>
            </div>

            <div className="form-field form-field--check">
              <label>
                <input type="checkbox" name="rook_friends"
                  checked={form.rook_friends} onChange={handleChange} />
                ROOK FRIENDS
              </label>
            </div>
          </div>

          <button className="btn btn--primary btn--submit" type="submit" disabled={submitting}>
            {submitting ? '[ TRANSMITTING... ]' : '[ CONFIRM ENTRY ]'}
          </button>
        </form>
      )}
    </div>
  )
}
