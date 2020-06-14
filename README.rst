=======================
Terraforming Mars Stats
=======================

.. contents::
    :depth: 2

❓ What's this even about?
--------------------------

The most addictive board game and people who are addicted to stats.

🔨 Any cool tools?
------------------

Will have to disappoint - pretty basic.

:Deployment: Not sure yet, though helped by ``docker``
:Backend: - Django 3
          - Django REST / Swagger UI (in plans)
          - Postgres 12

:Frontend: - VueJS, SPA-ish
           - Webpack interface
           - *Probably* D3.js for visualisations


🚀 Boring. Let's see
--------------------

.. code:: bash

    npm ci
    npm run build
    make install
    make up

* ``npm run build`` builds ``js`` files once
* ``npm run watch`` builds automatically on changes

Navigate to ``localhost:8000`` or ``DOCKER_MACHINE_IP:8000`` if you use ``docker-machine``

``make down`` to stop the containers


Initial data import
~~~~~~~~~~~~~~~~~~~

Not a big fan of what's below, let's rather make it ``python manage.py <not_hardcoded_file_name.csv>``

* Make sure you have ``terra-mars-initial-data.csv`` in the ``terra_mars/games/initial_import`` folder
* Run ``make import-initial-data``

