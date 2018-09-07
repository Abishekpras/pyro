"""
The :mod:`pyro.contrib.glmm` module provides models and guides for
generalised linear mixed models (GLMM). It also includes the
Normal-inverse-gamma family.

To create a classical Bayesian linear model, use::

    from pyro.contrib.glmm import known_covariance_linear_model

    # Note: coef is a p-vector, observation_sd is a scalar
    # Here, p=1 (one feature)
    model = known_covariance_linear_model(coef_mean=torch.tensor([0.]),
                                          coef_sd=torch.tensor([10.]),
                                          observation_sd=torch.tensor(2.))

    # An n x p design tensor
    # Here, n=2 (two observations)
    design = torch.tensor(torch.tensor([[1.], [-1.]]))

    model(design)

use a non-linear link function, such as::

    from pyro.contrib.glmm import logistic_regression_model

    # No observation_sd is needed for logistic models
    model = logistic_regression_model(coef_mean=torch.tensor([0.]),
                                      coef_sd=torch.tensor([10.]))

Random effects may be incorporated as regular Bayesian regression coefficients.
For random effects with a shared covariance matrix, see `pyro.contrib.glmm.lmer_model`.
"""

from pyro.contrib.glmm.glmm import *  # noqa: F403, F401
from pyro.contrib.glmm import guides  # noqa: F401
