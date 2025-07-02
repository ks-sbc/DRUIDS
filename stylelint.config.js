module.exports = {
  extends: ['stylelint-config-standard'],
  plugins: ['stylelint-order'],
  rules: {
    'no-duplicate-selectors': true,
    'declaration-block-no-duplicate-properties': true,
    'declaration-block-no-duplicate-custom-properties': true,
    'font-family-no-duplicate-names': true,
    'keyframe-block-no-duplicate-selectors': true,
    'no-duplicate-at-import-rules': true,
    'color-hex-length': 'short',
    'color-named': 'never',
    'selector-max-specificity': '0,4,2', // Allow for complex Material theme selectors
    'max-nesting-depth': 4,
    'declaration-no-important': null, // Allow !important for theme overrides
    'selector-class-pattern': null, // Allow Material theme class names
    'order/properties-alphabetical-order': true,
    'unit-allowed-list': ['px', 'rem', 'em', '%', 'vh', 'vw', 'deg', 'ms', 's', 'fr'],
    'declaration-property-value-allowed-list': {
      '/^border/': ['none', '0', /px/, 'solid', 'dashed', 'dotted'],
      '/^padding|^gap/': [/rem/, /px/, '0']
    },
    'property-no-vendor-prefix': true,
    'value-no-vendor-prefix': true,
    'selector-no-vendor-prefix': true,
    'media-feature-name-no-vendor-prefix': true,
    'at-rule-no-vendor-prefix': true,
    'length-zero-no-unit': true,
    'font-weight-notation': 'numeric',
    'function-url-quotes': 'always',
    'comment-empty-line-before': null,
    'custom-property-pattern': '^(qm|cyber|dark-pride|druids)-[a-z0-9-]+$',
    'at-rule-no-unknown': [true, {
      'ignoreAtRules': ['apply', 'layer', 'tailwind', 'screen']
    }],
    'selector-pseudo-class-no-unknown': [true, {
      'ignorePseudoClasses': ['global']
    }]
  },
  ignoreFiles: [
    'docs/assets/css/extra.css', // Temporarily ignore the large file
    '**/node_modules/**'
  ]
};