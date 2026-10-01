# Disagreement analysis

This is an exploratory comparison using the same comments, frozen human labels, and scoring criteria for two different configurations. The observed differences do not isolate a model effect or an instruction effect.

## Baseline observations

The NLI configuration agreed on 29/60 cases and predicted Harmful only once. Clear examples of rule conflicts include IDs 12 (“Tam bir salaksın”) and 43 (“Beynin olsa böyle konuşmazdın”), both predicted Safe. Ordinary greetings such as ID 25 (“İstanbul'dan selamlar”) were predicted Ambiguous. This indicates poor task performance for this specific configuration, not proof of a single underlying cause.

The candidate descriptions are a coarse approximation of the human policy. The fuller annotation rules were not supplied to this NLI classifier. The manual run changed both model and instructions, so the observed difference cannot isolate language ability, model architecture, or instruction detail.

## All manual-run disagreements

| IDs | Frozen human label | Manual model label | Review status |
|---|---|---|---|
| 6 | Ambiguous | Safe | Human revised to Safe after reviewing the policy and prediction |
| 8 | Safe | Harmful | Human retained Safe; shaming versus behavior criticism remains debatable |
| 15, 18, 24, 29, 35, 38, 41, 44, 56, 60 | Ambiguous | Safe | Not individually adjudicated; often involve tone, sarcasm, or dismissiveness |
| 59 | Ambiguous | Harmful | Human retained Ambiguous; warning versus implied threat |

## Three documented post-prediction decisions

### ID 6: Çok zekisin gerçekten maşallah
Frozen label: Ambiguous. Manual prediction: Safe. Reviewed label: Safe.

The human reason was that sarcasm alone is not disallowed and this text only has the possibility of sarcasm. This is an annotation revision supported by the clarified rule, not an independently measured model improvement.

### ID 8: İnsan biraz utanır böyle konuşmaya
Frozen label: Safe. Manual prediction: Harmful. Reviewed label: Safe.

The human viewed this as an opinion rather than harmful language. Review clarified that expressing an opinion alone cannot establish safety. A defensible Safe reading targets speaking behavior, while a Harmful reading treats the sentence as shaming the person. Record this as a policy boundary rather than a definitive model error.

### ID 59: Bir daha böyle yaparsan pişman olursun
Frozen label: Ambiguous. Manual prediction: Harmful. Reviewed label: Ambiguous.

The human noted the possibility of a threat without an explicit statement of causing regret. Review clarified that threats can be implicit. Ambiguous is supported by two plausible readings: a warning about consequences and an implied threat. More context or a stricter threat policy would be needed to resolve it.

## Interpretation

The manual method handles explicit insults more consistently with the reference labels. Most remaining disagreements concern the threshold for Ambiguous and may reflect differences in applying the clarified policy. Agreement alone cannot decide which party is correct. Human decisions after seeing model predictions are not independent ground truth.

Metrics remain calculated against frozen labels: 29/60 and 47/60. No post-review rescore is presented as increased model accuracy.
