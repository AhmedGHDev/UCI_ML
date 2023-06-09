import pandas as pd


#Step 00: Loading data
#FROM URL
"""
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/audiology/audiology.standardized.data", names=['age_gt_60', 'air()', 'airBoneGap', 'ar_c()', 'ar_u()', 'bone()', 'boneAbnormal', 'bser()', 'history_buzzing', 'history_dizziness', 'history_fluctuating', 'history_fullness', 'history_heredity', 'history_nausea', 'history_noise', 'history_recruitment', 'history_ringing', 'history_roaring', 'history_vomiting', 'late_wave_poor', 'm_at_2k', 'm_cond_lt_1k', 'm_gt_1k', 'm_m_gt_2k', 'm_m_sn', 'm_m_sn_gt_1k', 'm_m_sn_gt_2k', 'm_m_sn_gt_500', 'm_p_sn_gt_2k', 'm_s_gt_500', 'm_s_sn', 'm_s_sn_gt_1k', 'm_s_sn_gt_2k', 'm_s_sn_gt_3k', 'm_s_sn_gt_4k', 'm_sn_2_3k', 'm_sn_gt_1k', 'm_sn_gt_2k', 'm_sn_gt_3k', 'm_sn_gt_4k', 'm_sn_gt_500', 'm_sn_gt_6k', 'm_sn_lt_1k', 'm_sn_lt_2k', 'm_sn_lt_3k', 'middle_wave_poor', 'mod_gt_4k', 'mod_mixed', 'mod_s_mixed', 'mod_s_sn_gt_500', 'mod_sn', 'mod_sn_gt_1k', 'mod_sn_gt_2k', 'mod_sn_gt_3k', 'mod_sn_gt_4k', 'mod_sn_gt_500', 'notch_4k', 'notch_at_4k', 'o_ar_c()', 'o_ar_u()', 's_sn_gt_1k', 's_sn_gt_2k', 's_sn_gt_4k', 'speech()', 'static_normal', 'tymp()', 'viith_nerve_signs', 'wave_V_delayed', 'waveform_ItoV_prolonged', 'class'])

print(df.info())
"""

#LOACL
import pandas
df = pd.read_csv("../ics.uci.edu/ml/machine-learning-databases/audiology/audiology.standardized.data", names=['age_gt_60', 'air()', 'airBoneGap', 'ar_c()', 'ar_u()', 'bone()', 'boneAbnormal', 'bser()', 'history_buzzing', 'history_dizziness', 'history_fluctuating', 'history_fullness', 'history_heredity', 'history_nausea', 'history_noise', 'history_recruitment', 'history_ringing', 'history_roaring', 'history_vomiting', 'late_wave_poor', 'm_at_2k', 'm_cond_lt_1k', 'm_gt_1k', 'm_m_gt_2k', 'm_m_sn', 'm_m_sn_gt_1k', 'm_m_sn_gt_2k', 'm_m_sn_gt_500', 'm_p_sn_gt_2k', 'm_s_gt_500', 'm_s_sn', 'm_s_sn_gt_1k', 'm_s_sn_gt_2k', 'm_s_sn_gt_3k', 'm_s_sn_gt_4k', 'm_sn_2_3k', 'm_sn_gt_1k', 'm_sn_gt_2k', 'm_sn_gt_3k', 'm_sn_gt_4k', 'm_sn_gt_500', 'm_sn_gt_6k', 'm_sn_lt_1k', 'm_sn_lt_2k', 'm_sn_lt_3k', 'middle_wave_poor', 'mod_gt_4k', 'mod_mixed', 'mod_s_mixed', 'mod_s_sn_gt_500', 'mod_sn', 'mod_sn_gt_1k', 'mod_sn_gt_2k', 'mod_sn_gt_3k', 'mod_sn_gt_4k', 'mod_sn_gt_500', 'notch_4k', 'notch_at_4k', 'o_ar_c()', 'o_ar_u()', 's_sn_gt_1k', 's_sn_gt_2k', 's_sn_gt_4k', 'speech()', 'static_normal', 'tymp()', 'viith_nerve_signs', 'wave_V_delayed', 'waveform_ItoV_prolonged', 'class'])

print(df.info())