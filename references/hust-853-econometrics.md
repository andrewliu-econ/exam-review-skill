# HUST 853 Econometrics Review Profile

Use this as a topic checklist when the course is HUST 853 Econometrics or a closely equivalent exam. It contains no past-paper text and must not be used as evidence that a particular question appeared.

## Core topic map

1. **Regression foundations:** variables, parameters, error term versus residual, OLS objective, assumptions, fitted values, goodness of fit.
2. **Simple and multiple regression:** interpretation of coefficients, standard errors, t tests, confidence intervals, joint F tests, matrix form.
3. **Functional form and dummy variables:** log models, quadratic terms, interactions, intercept and slope shifts, dummy-variable trap.
4. **Classical assumptions and estimator properties:** unbiasedness, variance, efficiency, consistency, Gauss-Markov theorem.
5. **Multicollinearity:** perfect versus imperfect collinearity, consequences, detection, remedies.
6. **Heteroskedasticity:** consequences, White and related tests, robust standard errors, WLS/FGLS.
7. **Autocorrelation:** causes, consequences, Durbin-Watson and related tests, Newey-West or GLS remedies.
8. **Model specification:** omitted and irrelevant variables, RESET, nested and non-nested comparisons, information criteria.
9. **Endogeneity and simultaneous equations:** sources, identification, instrumental variables, 2SLS, overidentification and weak instruments.
10. **Time series:** stationarity, white noise, AR/MA models, unit roots, spurious regression, cointegration, error-correction models.
11. **Panel data:** pooled OLS, fixed effects, random effects, Hausman test, clustered inference.
12. **Binary or limited dependent variables:** linear probability model, logit/probit interpretation when included in the syllabus.

## High-yield answer chains

### OLS under a violated assumption

State the assumption, whether unbiasedness or consistency fails, whether the usual variance formula fails, the effect on tests, then the robust estimator or test.

### Hypothesis test

Write H0 and H1, choose the statistic, state its distribution under H0, compute or compare, then interpret in the model's language.

### Time-series diagnosis

Distinguish trend, unit root, deterministic nonstationarity, structural break, and serial correlation. Do not recommend differencing before checking what kind of nonstationarity is present.

### Panel model choice

Connect the choice to the correlation between the individual effect and regressors. Use fixed effects when that correlation is allowed; use random effects when the effect is uncorrelated with regressors and the required assumptions hold. State the Hausman null hypothesis correctly.

## Formula and notation checks

- Define every symbol: sample size, regressors, coefficients, disturbance, fitted value, residual.
- Keep hats for estimates distinct from population parameters.
- Check whether a variance formula assumes homoskedasticity or no serial correlation.
- For asymptotic results, state the limiting argument and required regularity conditions.
- Preserve the distinction between `Var`, `Cov`, `plim`, and conditional expectation.

## Exam-writing checklist

- Name the economic question before writing algebra.
- Interpret the sign, magnitude, units, and significance of coefficients.
- State the null and alternative before a test.
- Tie every remedy to the diagnosed failure.
- End with a one-sentence conclusion that answers the actual prompt.