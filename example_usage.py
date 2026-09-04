from client import CrossWindowPersistentNotesLedgerClient

def main():
    client = CrossWindowPersistentNotesLedgerClient()
    res = client.append_checkpoint_note('sess_01', 'REFACTOR_DATABASE', ['SCHEMA_DUMP'], ['APPLY_MIGRATION'])
    print('Persistent Notes Ledger: ' + res['ledger_id'] + ' (Goal: ' + res['goal_key'] + ')')
    print('Completed: ' + str(res['completed_count']) + ' | Lossless: ' + str(res['compression_lossless_guarantee']))
    print('Snapshot URL: ' + res['ledger_snapshot_url'])

if __name__ == '__main__':
    main()
