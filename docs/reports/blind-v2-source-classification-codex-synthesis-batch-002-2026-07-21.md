<!-- zhtw:disable -->
# Blind-v2 Source Classification Synthesis 002 (2026-07-21)

Status: superseded by maintainer decision; all 100 cases use the Codex first pass

## Summary

- Packet cases: 100
- Exact Codex/Gemini classifications: 55
- Differing classifications: 45
- Low-risk differences recommended for Codex batch confirmation: 27
- Cases requiring explicit maintainer attention: 18
- No converter output, expected text, or competing reviewer conclusion was exposed to Gemini.

Codex recommends batch-confirming the 55 exact matches and 27 low-risk Codex
differences. The following 18 cases need explicit attention because they affect
eligibility or because the synthesis recommendation differs from the Codex
first pass.

Maintainer decision on 2026-07-21: adopt Codex for the complete batch. Gemini
and third-version suggestions below remain advisory history and were not used in
the final classification.

## Eligibility Decisions

### flores-200-zho-hans-v1/dev-0775

Input: `世界园艺博览会是展示花卉、植物园和与植物有关的一切。`

Recommendation: **Codex — exclude**. The predicate is malformed and lacks the
construction needed to form a complete definition.

### flores-200-zho-hans-v1/devtest-0480

Input: `事件发生的时代通常被称为欧洲史的中世纪盛时，即的 11、12 和 13世纪时期（公元 1000-1300 年）。`

Recommendation: **Codex — exclude**. The sequence `即的` is a source error that
breaks the sentence structure.

### ud-chinese-cfl-v1/CFL_A_1-6_ori

Input: `因为我人生第一次亲眼看见军队。`

Recommendation: **Codex — exclude**. It is a subordinate clause without a main
clause.

### ud-chinese-cfl-v1/CFL_D_2-7_ori

Input: `我因开车就睡着了。`

Recommendation: **Codex — exclude**. It is unclear whether the writer means
falling asleep while driving or because of driving.

### ud-chinese-cfl-v1/CFL_F_2-4_ori

Input: `所以我一有时间，就带着一把钱和一个行李箱去旅行。`

Recommendation: **third version — include**, `social_daily / baseline_guard`,
medium confidence, with `awkward_word_choice`. `一把钱` is unnatural but the
sentence remains independently understandable.

### ud-chinese-cfl-v1/CFL_I_1-12_ori

Input: `有一天，他给我介绍一个他的堂妹了，然后那个堂妹真的喜欢我了，所以她给家人告诉了我真的是一个真的好女孩儿。`

Recommendation: **Codex — exclude**. Multiple argument and clause-order errors
make the latter half unreliable without reconstructing the intended sentence.

### ud-chinese-cfl-v1/CFL_L_1-10_ori

Input: `时光很快快过两个月了。`

Recommendation: **third version — include**, `social_daily / baseline_guard`,
medium confidence, with `duplicated_word`. The duplicated `快` is a local typo
and does not obscure the intended meaning.

### ud-chinese-cfl-v1/CFL_L_1-15_ori

Input: `那时我的心情是这样的：“天池不是令我流了很多眼泪的那个池吗？`

Recommendation: **Codex — exclude**. The quotation is unterminated and the
referent-dependent wording is fragmentary.

### ud-chinese-cfl-v1/CFL_M_1-31_ori

Input: `辛亏我遇到她，否则我不会了解爱情的意义，我来中国学习汉语便很快忘记了她，可是我很怕以后爱上别的女孩子，因为分手的感觉很难过，我不想再来一次。`

Recommendation: **Codex — include**, `social_daily / baseline_guard`, medium
confidence, with `typo`. The typo `辛亏` does not prevent independent semantic
interpretation.

## Classification Overrides

### flores-200-zho-hans-v1/dev-0253

Input: `被称为“11 号宇航员”的列昂诺夫是苏联最早的宇航员团队中的一员。`

Recommendation: **Gemini**, `formal_news / candidate_gap`; `宇航员` has the
Taiwan usage candidate `太空人`.

### flores-200-zho-hans-v1/dev-0501

Input: `它是由约翰•史密斯 (John Smith) 在 20 世纪 70 年代研发的，用于帮助缺乏经验的折纸人或动手能力差的人。`

Recommendation: **Gemini**, `formal_news / over_conversion_guard`; the person
name is the primary risk and `研發` is already normal Taiwan usage.

### flores-200-zho-hans-v1/dev-0660

Input: `旧金山的经济与自身是世界级旅游胜地这一点有关，但旧金山的经济却是多元化的。`

Recommendation: **Gemini**, `formal_news / over_conversion_guard`; protect the
place name and do not invent a regional rewrite.

### flores-200-zho-hans-v1/dev-0672

Input: `因此，如果启程日期为 5 月，野地露营许可证将在 1 月 1 日发放。`

Recommendation: **third version**, `social_daily / baseline_guard`. This is
travel guidance, while `許可證` is standard Taiwan usage rather than a lexical
gap.

### flores-200-zho-hans-v1/dev-0893

Input: `雪被压实，缝隙也被填满，并用旗帜做了标记。只有专门的拖拉机以及拖着装有燃料和补给的雪橇才能通行。`

Recommendation: **third version**, `social_daily / candidate_gap`; retain the
travel-guide domain while testing the vehicle terminology.

### flores-200-zho-hans-v1/devtest-0637

Input: `哲学家亚里士多德提出一种理论，即任何事物都是由土、水、空气和火四种元素中的一种或多种组成的。`

Recommendation: **Gemini**, `formal_news / over_conversion_guard`; the proper
name is the dominant conversion risk.

### ud-chinese-cfl-v1/CFL_D_2-22_ori

Input: `那条公路沿海岸，所以途径中有海岛和很大的桥梁。`

Recommendation: **Gemini**, `social_daily / baseline_guard`; the wording is
awkward, but there is no clear PRC-to-Taiwan lexical candidate.

### ud-chinese-cfl-v1/CFL_L_1-1_ori

Input: `对我来说最难忘记的事就是有关天池和找对象的事情。`

Recommendation: **Gemini**, `social_daily / over_conversion_guard`; protect the
place name `天池`.

### ud-chinese-cfl-v1/CFL_P_1-6_ori

Input: `另外和我以前想象完全不一的是中国的饮食非常符合我的味口。`

Recommendation: **Gemini**, `social_daily / over_conversion_guard`, while
retaining the `味口` typo as source text; the place name is the main risk.
