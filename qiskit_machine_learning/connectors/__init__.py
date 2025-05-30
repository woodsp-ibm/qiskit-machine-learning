# This code is part of a Qiskit project.
#
# (C) Copyright IBM 2021, 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Connectors (:mod:`qiskit_machine_learning.connectors`)
======================================================

"Connector" tools to couple Qiskit Machine Learning to other frameworks.

.. currentmodule:: qiskit_machine_learning.connectors

Connectors
----------------------

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   TorchConnector

"""

from .torch_connector import TorchConnector


__all__ = ["TorchConnector"]
