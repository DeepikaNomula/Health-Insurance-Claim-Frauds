#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
importos
import sys

defmain():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'identifying_health_insurance_claim_frauds.settings')
    try:
        fromdjango.core.managementimportexecute_from_command_line
    exceptImportErrorasexc:
        raiseImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) fromexc
    execute_from_command_line(sys.argv)

if__name__=='__main__':
    main()
