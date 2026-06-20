// =========================
// GLOBAL TRANSLATIONS
// =========================

const translations = {

    en: {

        dashboard: 'Dashboard',
        prediction: 'Prediction',
        analytics: 'Analytics',
        reports: 'Reports',
        settings: 'Settings',

        endopredict: 'EndoPredict AI',

        system_overview:
            'System overview and key metrics',

        system_performance:
            'System Performance',

        model_status:
            'Model Status',

        last_updated:
            'Last Updated',

        precision_score:
            'Precision Score',

        recall_score:
            'Recall Score',

        api_status:
            'API Status',

        active_running:
            '✅ Active & Running',

        operational:
            '✅ Operational',

        patient_information:
            'Patient Information',

        age: 'Age',

        menstrual_irregularity:
            'Menstrual Irregularity',

        chronic_pain:
            'Chronic Pain Level',

        hormone_abnormality:
            'Hormone Level Abnormality',

        infertility:
            'Infertility',

        bmi: 'BMI',

        height: 'Height',

        weight: 'Weight',

        blood_pressure_systolic:
            'Blood Pressure Systolic',

        blood_pressure_diastolic:
            'Blood Pressure Diastolic',

        estrogen_level:
            'Estrogen Level',

        progesterone_level:
            'Progesterone Level',

        upload_scan:
            'Upload Scan Image',

        predict_disease:
            'Predict Disease',

        accuracy:
            'Accuracy',

        precision:
            'Precision',

        recall:
            'Recall',

        f1_score:
            'F1-Score',

        success_rate:
            'Success Rate',

        yes: 'Yes',
        no: 'No',

        high: 'High',
        moderate: 'Moderate',
        low: 'Low',

        data_driven:
            'Data-driven insights and performance metrics',

        accuracy_trend:
            'Accuracy Trend Over Time',

        precision_vs_recall:
            'Precision vs Recall Performance',

        f1_performance:
            'F1-Score Performance',

        patient_predictions:
            'Patient predictions and diagnostic reports',

        download_all:
            'Download All Reports',

        no_reports:
            'No reports available. Make a prediction to generate reports.',

        report_id:
            'Report ID',

        confidence:
            'Confidence',

        risk_level:
            'Risk Level',

        date:
            'Date',

        status:
            'Status',

        completed:
            '✓ Completed',

        dark_mode:
            'Dark Mode',

        system_info:
            'System Information',

        backend_status:
            'Backend Status',

        ai_accuracy:
            'AI Accuracy',

        model_version:
            'Model Version',

        language:
            'Language',

        select_language:
            'Select Language',

        save_settings:
            'Save Settings',

        light_mode:
            'Light Mode'
    },

    te: {

        dashboard: 'డ్యాష్‌బోర్డ్',
        prediction: 'ఊహ',
        analytics: 'విశ్లేషణ',
        reports: 'నివేదికలు',
        settings: 'సెట్టింగ్‌లు',

        endopredict:
            'ఎండోప్రెడిక్ట్ AI',

        language:
            'భాష',

        select_language:
            'భాష ఎంచుకోండి',

        dark_mode:
            'డార్క్ మోడ్',

        system_info:
            'సిస్టమ్ సమాచారం',

        save_settings:
            'సెట్టింగ్‌లను సేవ్ చేయండి'
    },

    hi: {

        dashboard: 'डैशबोर्ड',
        prediction: 'पूर्वानुमान',
        analytics: 'विश्लेषण',
        reports: 'रिपोर्ट',
        settings: 'सेटिंग्स',

        endopredict:
            'एंडोप्रेडिक्ट एआई',

        language:
            'भाषा',

        select_language:
            'भाषा चुनें',

        dark_mode:
            'डार्क मोड',

        system_info:
            'सिस्टम जानकारी',

        save_settings:
            'सेटिंग्स सहेजें'
    }
};


// =========================
// INITIALIZE SETTINGS
// =========================

function initializeGlobalSettings() {

    // REMOVE OLD THEME STORAGE

    localStorage.removeItem('themeColor');

    // REMOVE OLD THEME CLASSES

    document.body.classList.remove(
        'theme-blue',
        'theme-purple',
        'theme-green',
        'theme-red'
    );

    // LOAD SAVED LANGUAGE

    const savedLanguage =

        localStorage.getItem(
            'preferredLanguage'
        ) || 'en';

    // APPLY LANGUAGE

    translatePage(savedLanguage);
}


// =========================
// TRANSLATE PAGE
// =========================

function translatePage(lang) {

    const trans = translations[lang];

    if (!trans) return;

    document
        .querySelectorAll('[data-i18n]')
        .forEach(element => {

            const key =
                element.getAttribute(
                    'data-i18n'
                );

            if (trans[key]) {

                element.innerText =
                    trans[key];
            }
        });
}


// =========================
// CHANGE LANGUAGE
// =========================

function changeLanguage(lang) {

    localStorage.setItem(
        'preferredLanguage',
        lang
    );

    translatePage(lang);
}


// =========================
// INITIALIZE AUTOMATICALLY
// =========================

document.addEventListener(

    'DOMContentLoaded',

    initializeGlobalSettings
);