# uvarov-frontend/vanilla-calendar-pro@main

- Files included: 440
- Files skipped: 2
- Total size: 854.3 KB
- Estimated tokens: ~191,710

## Directory Structure

```
├── .github
│   ├── ISSUE_TEMPLATE
│   │   ├── -bug--bug-report.md
│   │   ├── -enhancement--feature-request.md
│   │   ├── -question--help-request.md
│   │   └── config.yml
│   ├── workflows
│   │   ├── main.yml
│   │   └── pull_request.yml
│   ├── dependabot.yml
│   └── FUNDING.yml
├── config
│   ├── assets.config.ts
│   ├── helpers.ts
│   ├── main.config.ts
│   └── utils.config.ts
├── cypress
│   ├── e2e
│   │   ├── a11y.cy.ts
│   │   ├── animation.cy.ts
│   │   ├── collapse.cy.ts
│   │   ├── default.cy.ts
│   │   ├── disableDatesGaps.cy.ts
│   │   ├── gestureOptions.cy.ts
│   │   ├── lifecycleGuards.cy.ts
│   │   ├── multiple.cy.ts
│   │   ├── popupsRange.cy.ts
│   │   ├── shadowDom.cy.ts
│   │   ├── swipe.cy.ts
│   │   ├── week.cy.ts
│   │   └── weekNumbers.cy.ts
│   └── support
│       ├── commands.ts
│       └── e2e.ts
├── demo
│   ├── pages
│   │   ├── a11y
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── animation
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── disable-dates-gaps
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── gestures
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── input
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── lang
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── lifecycle
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── multiple
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── popups-range
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── shadow-dom
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   ├── week
│   │   │   ├── index.html
│   │   │   └── main.ts
│   │   └── week-numbers
│   │       ├── index.html
│   │       └── main.ts
│   ├── favicon.svg
│   ├── index.css
│   ├── index.html
│   └── main.ts
├── docs
│   ├── en
│   │   ├── learn
│   │   │   ├── additional-features-animation.mdx
│   │   │   ├── additional-features-collapse.mdx
│   │   │   ├── additional-features-layouts.mdx
│   │   │   ├── additional-features-popups-and-tooltip.mdx
│   │   │   ├── additional-features-styles.mdx
│   │   │   ├── additional-features-swipe.mdx
│   │   │   ├── additional-features-themes.mdx
│   │   │   ├── components-for-libraries-angular.mdx
│   │   │   ├── components-for-libraries-react.mdx
│   │   │   ├── components-for-libraries-vue.mdx
│   │   │   ├── components-for-libraries-web-component.mdx
│   │   │   ├── date-management-date-min-and-max.mdx
│   │   │   ├── date-management-display-range-dates.mdx
│   │   │   ├── date-management-enable-or-disable-days.mdx
│   │   │   ├── date-management-enable-time-picker.mdx
│   │   │   ├── date-management-forbid-choice.mdx
│   │   │   ├── date-management-other-today.mdx
│   │   │   ├── date-management-selected-days-month-year.mdx
│   │   │   ├── handle-click-a-day.mdx
│   │   │   ├── handle-click-on-a-month-in-the-month-selection.mdx
│   │   │   ├── handle-click-on-the-arrows.mdx
│   │   │   ├── handle-click-on-the-year-in-the-year-selection.mdx
│   │   │   ├── handle-click-on-weekday-and-the-week-number.mdx
│   │   │   ├── handle-get-and-change-every-day.mdx
│   │   │   ├── handle-select-and-change-of-time.mdx
│   │   │   ├── installation-and-usage.mdx
│   │   │   ├── internationalization-locale.mdx
│   │   │   ├── internationalization-week-numbers.mdx
│   │   │   ├── internationalization-weekday-first-and-weekdays.mdx
│   │   │   ├── internationalization-weekends-and-holidays.mdx
│   │   │   ├── type-default.mdx
│   │   │   ├── type-month.mdx
│   │   │   ├── type-multiple.mdx
│   │   │   ├── type-week.mdx
│   │   │   └── type-year.mdx
│   │   ├── reference
│   │   │   ├── actions.mdx
│   │   │   ├── creating-an-instance.mdx
│   │   │   ├── labels.mdx
│   │   │   ├── layouts.mdx
│   │   │   ├── methods.mdx
│   │   │   ├── popups.mdx
│   │   │   ├── settings.mdx
│   │   │   ├── styles.mdx
│   │   │   └── utilities.mdx
│   │   ├── learn.mdx
│   │   └── reference.mdx
│   ├── ko
│   │   ├── learn
│   │   │   ├── additional-features-animation.mdx
│   │   │   ├── additional-features-collapse.mdx
│   │   │   ├── additional-features-layouts.mdx
│   │   │   ├── additional-features-popups-and-tooltip.mdx
│   │   │   ├── additional-features-styles.mdx
│   │   │   ├── additional-features-swipe.mdx
│   │   │   ├── additional-features-themes.mdx
│   │   │   ├── components-for-libraries-angular.mdx
│   │   │   ├── components-for-libraries-react.mdx
│   │   │   ├── components-for-libraries-vue.mdx
│   │   │   ├── components-for-libraries-web-component.mdx
│   │   │   ├── date-management-date-min-and-max.mdx
│   │   │   ├── date-management-display-range-dates.mdx
│   │   │   ├── date-management-enable-or-disable-days.mdx
│   │   │   ├── date-management-enable-time-picker.mdx
│   │   │   ├── date-management-forbid-choice.mdx
│   │   │   ├── date-management-other-today.mdx
│   │   │   ├── date-management-selected-days-month-year.mdx
│   │   │   ├── handle-click-a-day.mdx
│   │   │   ├── handle-click-on-a-month-in-the-month-selection.mdx
│   │   │   ├── handle-click-on-the-arrows.mdx
│   │   │   ├── handle-click-on-the-year-in-the-year-selection.mdx
│   │   │   ├── handle-click-on-weekday-and-the-week-number.mdx
│   │   │   ├── handle-get-and-change-every-day.mdx
│   │   │   ├── handle-select-and-change-of-time.mdx
│   │   │   ├── installation-and-usage.mdx
│   │   │   ├── internationalization-locale.mdx
│   │   │   ├── internationalization-week-numbers.mdx
│   │   │   ├── internationalization-weekday-first-and-weekdays.mdx
│   │   │   ├── internationalization-weekends-and-holidays.mdx
│   │   │   ├── type-default.mdx
│   │   │   ├── type-month.mdx
│   │   │   ├── type-multiple.mdx
│   │   │   ├── type-week.mdx
│   │   │   └── type-year.mdx
│   │   ├── reference
│   │   │   ├── actions.mdx
│   │   │   ├── creating-an-instance.mdx
│   │   │   ├── labels.mdx
│   │   │   ├── layouts.mdx
│   │   │   ├── methods.mdx
│   │   │   ├── popups.mdx
│   │   │   ├── settings.mdx
│   │   │   ├── styles.mdx
│   │   │   └── utilities.mdx
│   │   ├── learn.mdx
│   │   └── reference.mdx
│   ├── ru
│   │   ├── learn
│   │   │   ├── additional-features-animation.mdx
│   │   │   ├── additional-features-collapse.mdx
│   │   │   ├── additional-features-layouts.mdx
│   │   │   ├── additional-features-popups-and-tooltip.mdx
│   │   │   ├── additional-features-styles.mdx
│   │   │   ├── additional-features-swipe.mdx
│   │   │   ├── additional-features-themes.mdx
│   │   │   ├── components-for-libraries-angular.mdx
│   │   │   ├── components-for-libraries-react.mdx
│   │   │   ├── components-for-libraries-vue.mdx
│   │   │   ├── components-for-libraries-web-component.mdx
│   │   │   ├── date-management-date-min-and-max.mdx
│   │   │   ├── date-management-display-range-dates.mdx
│   │   │   ├── date-management-enable-or-disable-days.mdx
│   │   │   ├── date-management-enable-time-picker.mdx
│   │   │   ├── date-management-forbid-choice.mdx
│   │   │   ├── date-management-other-today.mdx
│   │   │   ├── date-management-selected-days-month-year.mdx
│   │   │   ├── handle-click-a-day.mdx
│   │   │   ├── handle-click-on-a-month-in-the-month-selection.mdx
│   │   │   ├── handle-click-on-the-arrows.mdx
│   │   │   ├── handle-click-on-the-year-in-the-year-selection.mdx
│   │   │   ├── handle-click-on-weekday-and-the-week-number.mdx
│   │   │   ├── handle-get-and-change-every-day.mdx
│   │   │   ├── handle-select-and-change-of-time.mdx
│   │   │   ├── installation-and-usage.mdx
│   │   │   ├── internationalization-locale.mdx
│   │   │   ├── internationalization-week-numbers.mdx
│   │   │   ├── internationalization-weekday-first-and-weekdays.mdx
│   │   │   ├── internationalization-weekends-and-holidays.mdx
│   │   │   ├── type-default.mdx
│   │   │   ├── type-month.mdx
│   │   │   ├── type-multiple.mdx
│   │   │   ├── type-week.mdx
│   │   │   └── type-year.mdx
│   │   ├── reference
│   │   │   ├── actions.mdx
│   │   │   ├── creating-an-instance.mdx
│   │   │   ├── labels.mdx
│   │   │   ├── layouts.mdx
│   │   │   ├── methods.mdx
│   │   │   ├── popups.mdx
│   │   │   ├── settings.mdx
│   │   │   ├── styles.mdx
│   │   │   └── utilities.mdx
│   │   ├── learn.mdx
│   │   └── reference.mdx
│   └── zh
│       ├── learn
│       │   ├── additional-features-animation.mdx
│       │   ├── additional-features-collapse.mdx
│       │   ├── additional-features-layouts.mdx
│       │   ├── additional-features-popups-and-tooltip.mdx
│       │   ├── additional-features-styles.mdx
│       │   ├── additional-features-swipe.mdx
│       │   ├── additional-features-themes.mdx
│       │   ├── components-for-libraries-angular.mdx
│       │   ├── components-for-libraries-react.mdx
│       │   ├── components-for-libraries-vue.mdx
│       │   ├── components-for-libraries-web-component.mdx
│       │   ├── date-management-date-min-and-max.mdx
│       │   ├── date-management-display-range-dates.mdx
│       │   ├── date-management-enable-or-disable-days.mdx
│       │   ├── date-management-enable-time-picker.mdx
│       │   ├── date-management-forbid-choice.mdx
│       │   ├── date-management-other-today.mdx
│       │   ├── date-management-selected-days-month-year.mdx
│       │   ├── handle-click-a-day.mdx
│       │   ├── handle-click-on-a-month-in-the-month-selection.mdx
│       │   ├── handle-click-on-the-arrows.mdx
│       │   ├── handle-click-on-the-year-in-the-year-selection.mdx
│       │   ├── handle-click-on-weekday-and-the-week-number.mdx
│       │   ├── handle-get-and-change-every-day.mdx
│       │   ├── handle-select-and-change-of-time.mdx
│       │   ├── installation-and-usage.mdx
│       │   ├── internationalization-locale.mdx
│       │   ├── internationalization-week-numbers.mdx
│       │   ├── internationalization-weekday-first-and-weekdays.mdx
│       │   ├── internationalization-weekends-and-holidays.mdx
│       │   ├── type-default.mdx
│       │   ├── type-month.mdx
│       │   ├── type-multiple.mdx
│       │   ├── type-week.mdx
│       │   └── type-year.mdx
│       ├── reference
│       │   ├── actions.mdx
│       │   ├── creating-an-instance.mdx
│       │   ├── labels.mdx
│       │   ├── layouts.mdx
│       │   ├── methods.mdx
│       │   ├── popups.mdx
│       │   ├── settings.mdx
│       │   ├── styles.mdx
│       │   └── utilities.mdx
│       ├── learn.mdx
│       └── reference.mdx
├── examples
│   ├── additional-features-animation-custom.ts
│   ├── additional-features-animation-shared.ts
│   ├── additional-features-animation.ts
│   ├── additional-features-collapse.ts
│   ├── additional-features-layouts-btn-close.ts
│   ├── additional-features-layouts.ts
│   ├── additional-features-popups.ts
│   ├── additional-features-styles.ts
│   ├── additional-features-swipe.ts
│   ├── additional-features-themes-dark.ts
│   ├── additional-features-themes-light.ts
│   ├── additional-features-themes-slate-light.ts
│   ├── additional-features-tooltips.ts
│   ├── date-management-date-min-and-max.ts
│   ├── date-management-disable-dates.ts
│   ├── date-management-display-range-dates.ts
│   ├── date-management-enable-dates.ts
│   ├── date-management-enable-time-picker-12.ts
│   ├── date-management-enable-time-picker-24.ts
│   ├── date-management-enable-time-picker-control.ts
│   ├── date-management-enable-time-picker-range.ts
│   ├── date-management-enable-time-picker-your-time.ts
│   ├── date-management-forbid-choice.ts
│   ├── date-management-other-today.ts
│   ├── date-management-selected-days-month-year.ts
│   ├── handle-click-a-day-ranged.ts
│   ├── handle-click-a-day.ts
│   ├── handle-click-on-a-month-in-the-month-selection.ts
│   ├── handle-click-on-the-arrows.ts
│   ├── handle-click-on-the-week-number.ts
│   ├── handle-click-on-the-year-in-the-year-selection.ts
│   ├── handle-click-on-weekday.ts
│   ├── handle-get-and-change-every-day.ts
│   ├── handle-select-and-change-of-time.ts
│   ├── installation-and-usage.ts
│   ├── internationalization-assign-manually.ts
│   ├── internationalization-locale.ts
│   ├── internationalization-week-numbers.ts
│   ├── internationalization-weekday-first-and-weekdays.ts
│   ├── internationalization-weekends-and-holidays.ts
│   ├── type-default-in-input.ts
│   ├── type-default.ts
│   ├── type-month.ts
│   ├── type-multiple-ranged.ts
│   ├── type-multiple.ts
│   ├── type-week-in-input.ts
│   ├── type-week.ts
│   └── type-year.ts
├── package
│   ├── public
│   │   ├── index.html
│   │   ├── LICENSE
│   │   ├── package.json
│   │   └── README.md
│   └── src
│       ├── scripts
│       │   ├── components
│       │   │   ├── ArrowNext.ts
│       │   │   ├── ArrowPrev.ts
│       │   │   ├── Collapse.ts
│       │   │   ├── ControlTime.ts
│       │   │   ├── DateRangeTooltip.ts
│       │   │   ├── Dates.ts
│       │   │   ├── index.ts
│       │   │   ├── Month.ts
│       │   │   ├── Months.ts
│       │   │   ├── TimeInput.ts
│       │   │   ├── TimeRange.ts
│       │   │   ├── Week.ts
│       │   │   ├── WeekNumbers.ts
│       │   │   ├── Year.ts
│       │   │   └── Years.ts
│       │   ├── creators
│       │   │   ├── createDates
│       │   │   │   ├── createDate.ts
│       │   │   │   ├── createDatePopup.ts
│       │   │   │   ├── createDateRangeTooltip.ts
│       │   │   │   ├── createDates.ts
│       │   │   │   ├── createDatesFromCurrentMonth.ts
│       │   │   │   ├── createDatesFromNextMonth.ts
│       │   │   │   ├── createDatesFromPrevMonth.ts
│       │   │   │   ├── createWeekDates.ts
│       │   │   │   ├── setDateModifier.ts
│       │   │   │   └── updateDateModifiers.ts
│       │   │   ├── create.ts
│       │   │   ├── createLayouts.ts
│       │   │   ├── createMonths.ts
│       │   │   ├── createTime.ts
│       │   │   ├── createToInput.ts
│       │   │   ├── createWeek.ts
│       │   │   ├── createWeekNumbers.ts
│       │   │   ├── createYears.ts
│       │   │   ├── setMonthOrYearModifier.ts
│       │   │   ├── visibilityArrows.ts
│       │   │   └── visibilityTitle.ts
│       │   ├── handles
│       │   │   ├── handleClick
│       │   │   │   ├── handleClick.ts
│       │   │   │   ├── handleClickArrow.ts
│       │   │   │   ├── handleClickCollapse.ts
│       │   │   │   ├── handleClickDate.ts
│       │   │   │   ├── handleClickMonthOrYear.ts
│       │   │   │   └── handleClickWeek.ts
│       │   │   ├── handleGestures
│       │   │   │   ├── collapseTransition.ts
│       │   │   │   ├── dragTracker.ts
│       │   │   │   ├── handleGestures.ts
│       │   │   │   ├── swipeTransition.ts
│       │   │   │   └── transition.ts
│       │   │   ├── handleSelectDateRange
│       │   │   │   ├── handleCancelSelectionDates.ts
│       │   │   │   ├── handleHoverDatesEvent.ts
│       │   │   │   ├── handleHoverSelectedDatesRangeEvent.ts
│       │   │   │   ├── handleMouseLeave.ts
│       │   │   │   ├── handleSelectDateRange.ts
│       │   │   │   ├── optimizedHandles.ts
│       │   │   │   ├── state.ts
│       │   │   │   ├── toggleHoverEffect.ts
│       │   │   │   └── updateDisabledDates.ts
│       │   │   ├── handleTime
│       │   │   │   ├── handleActions.ts
│       │   │   │   ├── handleClickKeepingTime.ts
│       │   │   │   ├── handleInput.ts
│       │   │   │   ├── handleRange.ts
│       │   │   │   └── handleTime.ts
│       │   │   ├── handleArrowKeys.ts
│       │   │   ├── handleInput.ts
│       │   │   ├── handleNavigate.ts
│       │   │   ├── handleSelectDate.ts
│       │   │   └── handleTheme.ts
│       │   ├── layouts
│       │   │   ├── default.ts
│       │   │   ├── month.ts
│       │   │   ├── multiple.ts
│       │   │   ├── week.ts
│       │   │   └── year.ts
│       │   ├── methods
│       │   │   ├── destroy.ts
│       │   │   ├── hide.ts
│       │   │   ├── index.ts
│       │   │   ├── init.ts
│       │   │   ├── reset.ts
│       │   │   ├── set.ts
│       │   │   ├── show.ts
│       │   │   └── update.ts
│       │   └── utils
│       │       ├── initVariables
│       │       │   ├── initAllVariables.ts
│       │       │   ├── initMonthsCount.ts
│       │       │   ├── initRange.ts
│       │       │   ├── initSelectedDates.ts
│       │       │   ├── initSelectedMonthYear.ts
│       │       │   ├── initTime.ts
│       │       │   └── initWeek.ts
│       │       ├── positions
│       │       │   ├── calculateAvailableSpace.ts
│       │       │   ├── findBestPickerPosition.ts
│       │       │   ├── getAvailablePosition.ts
│       │       │   ├── getOffset.ts
│       │       │   ├── getViewportDimensions.ts
│       │       │   ├── getWindowScrollPosition.ts
│       │       │   └── setPosition.ts
│       │       ├── animate.ts
│       │       ├── canOpenOnFocus.ts
│       │       ├── canToggleSelection.ts
│       │       ├── getColumnID.ts
│       │       ├── getDate.ts
│       │       ├── getDateString.ts
│       │       ├── getErrorMessages.ts
│       │       ├── getLocalDate.ts
│       │       ├── getLocale.ts
│       │       ├── getLocaleString.ts
│       │       ├── getRootNode.ts
│       │       ├── getWeekNumber.ts
│       │       ├── getWeekStart.ts
│       │       ├── observeHtmlElement.ts
│       │       ├── parseComponent.ts
│       │       ├── parseDates.ts
│       │       ├── replaceProperties.ts
│       │       ├── resolveDate.ts
│       │       ├── resolveToggle.ts
│       │       ├── rovingTabIndex.ts
│       │       ├── setContext.ts
│       │       ├── setWeekDate.ts
│       │       ├── skipOpenOnFocus.ts
│       │       ├── toggleTabbing.ts
│       │       ├── transformTime12.ts
│       │       ├── transformTime24.ts
│       │       └── updateNavigationA11y.ts
│       ├── styles
│       │   ├── themes
│       │   │   ├── dark.css
│       │   │   ├── light.css
│       │   │   └── slate-light.css
│       │   ├── index.css
│       │   └── layout.css
│       ├── utils
│       │   └── index.ts
│       ├── index.ts
│       ├── labels.ts
│       ├── options.ts
│       ├── styles.ts
│       └── types.ts
├── .dockerignore
├── .editorconfig
├── .gitignore
├── .htmlvalidate.json
├── .prettierignore
├── .prettierrc
├── cypress.config.ts
├── eslint.config.mjs
├── helpers.js
├── LICENSE
├── package.json
├── postcss.config.js
├── README.md
├── tailwind.config.js
├── tsconfig.json
├── tsconfig.main.json
├── tsconfig.utils.json
├── vite-env.d.ts
├── vite.config.ts
└── yarn.lock
```

## Code Digest

### `.dockerignore`

```dockerignore
.git
.gitignore
node_modules
next/node_modules
next/.next
build
*.log
.DS_Store

```

### `.editorconfig`

```editorconfig
root = true

[*]
end_of_line = lf
charset = utf-8
insert_final_newline = true
trim_trailing_whitespace = true
tab_width = 2
indent_size = 2
indent_style = space
max_line_length = 124

```

### `.github/dependabot.yml`

```yml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: monthly
    groups:
      github-actions:
        patterns:
          - "*"

```

### `.github/FUNDING.yml`

```yml
buy_me_a_coffee: uvarov

```

### `.github/ISSUE_TEMPLATE/-bug--bug-report.md`

```md
---
name: Bug report
about: Report a bug or issue in Vanilla Calendar Pro
title: "[BUG]"
labels: bug
assignees: ''
---

**⚠️ Important: Bug reports are accepted only for version 3.0.0 or above**
Before submitting a bug report, ensure that you are using at least version **3.0.0** of Vanilla Calendar Pro. Issues reported for earlier versions will not be addressed.

---

**Describe the bug**
Provide a clear and concise description of the issue related to Vanilla Calendar Pro.

**Steps to reproduce**
Please list the exact steps to reproduce the issue:
1. Include the version of Vanilla Calendar Pro you are using.
2. Describe the setup process or initialization of the calendar.
3. Detail the actions taken before encountering the bug.

**Expected behavior**
What was the expected outcome or behavior of Vanilla Calendar Pro?

**CodeSandbox example (REQUIRED)**
To help us debug efficiently, you **must** create a reproducible example of the issue in a sandbox environment.
Use [CodeSandbox](https://codesandbox.io/) or a similar tool to replicate the problem, and provide the link here:
> Example link: https://codesandbox.io/p/sandbox/eloquent-dubinsky-cfthqk

**Screenshots (optional)**
If applicable, attach screenshots or GIFs to illustrate the problem.

**Additional context**
Include any additional details, such as custom configurations, integrations, or any logs related to the issue.

```

### `.github/ISSUE_TEMPLATE/-enhancement--feature-request.md`

```md
---
name: Feature request
about: Suggest a new feature or improvement for Vanilla Calendar Pro
title: "[FEATURE]"
labels: enhancement
assignees: ''
---

**⚠️ Important: Check before submitting**
Before proposing a new feature, ensure:
1. The feature does not already exist in Vanilla Calendar Pro.
2. It cannot be implemented using the current settings or customization options.

---

**Feature description**
Describe the feature or enhancement you would like to see in Vanilla Calendar Pro. Be specific and concise.

**Use case**
Explain why this feature is important.
- What problem does it solve?
- How would it improve the user experience?

**Proposed solution**
If you have an idea of how this feature could be implemented, describe it here. This can include API suggestions, functionality details, or UI/UX considerations.

**Similar functionality in other calendars (optional)**
If you know of another calendar that has this feature, please share its name and describe how it works.

**Alternatives considered**
If you have explored other solutions, mention them and explain why they are insufficient for your needs.

**Additional context**
Add any additional information, related discussions, or references that might help us understand and prioritize your request.

```

### `.github/ISSUE_TEMPLATE/-question--help-request.md`

```md
---
name: Help request
about: Request assistance with using Vanilla Calendar Pro
title: "[HELP]"
labels: question, help wanted
assignees: ''
---

**⚠️ Important: Check the documentation first**
Before submitting a help request, make sure to:
1. Review the official [Vanilla Calendar Pro documentation](https://vanilla-calendar.pro/ru/docs/reference).
2. Search existing issues to ensure your question has not already been answered.

---

**Describe your question**
Provide a clear and concise description of your issue or question about Vanilla Calendar Pro.

**Steps to reproduce your issue (if applicable)**
If your question is related to unexpected behavior, please provide the steps to reproduce it:
1. Your setup or configuration (share relevant code snippets).
2. Actions you performed before encountering the issue.

**CodeSandbox example (optional)**
If applicable, provide a minimal example in a sandbox environment like [CodeSandbox](https://codesandbox.io/):
> Example link: https://codesandbox.io/p/sandbox/eloquent-dubinsky-cfthqk

**Additional context**
Add any additional information, links, or context that could help answer your question.

```

### `.github/ISSUE_TEMPLATE/config.yml`

```yml
blank_issues_enabled: false
contact_links:
  - name: "Feedback"
    url: "https://t.me/uvarov_frontend"
    about: "Use this form to contact me if the problem is not described in the templates."

```

### `.github/workflows/main.yml`

```yml
name: Testing and deploy

on:
  push:
    branches:
      - main

jobs:
  cypress:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7.0.1
      - name: Setup npm package
        run: npm install
      - name: Testing
        uses: cypress-io/github-action@v7.4.1
        with:
          start: npm run dev
  deploy:
    runs-on: ubuntu-latest
    needs: cypress
    steps:
      - uses: actions/checkout@v7.0.1

      - name: Copy repository contents via scp
        uses: appleboy/scp-action@v1.0.0
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          port: ${{ secrets.PORT }}
          key: ${{ secrets.KEY }}
          source: '.'
          target: ${{ secrets.TARGET }}

      - name: Build app
        uses: appleboy/ssh-action@v1.2.5
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USERNAME }}
          port: ${{ secrets.PORT }}
          key: ${{ secrets.KEY }}
          script: |
            cd ${{ secrets.TARGET }}
            yarn install --frozen-lockfile
            yarn package:build

```

### `.github/workflows/pull_request.yml`

```yml
name: Testing pull request

on:
  pull_request:
    types: [opened, edited, reopened]
    branches:
      - main

jobs:
  cypress:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7.0.1
      - name: Setup npm package
        run: npm install
      - name: Testing
        uses: cypress-io/github-action@v7.4.1
        with:
          start: npm run dev

```

### `.gitignore`

```gitignore
# Default
.idea
.vscode

# Node
node_modules

# Dist & test
demo/build
demo/dist
package/dist
next

# Tests
cypress/videos

# BD, logs
*.log

# Other
npm-debug.log*
yarn-debug.log*
yarn-error.log*
package-lock.json

# Special
Thumbs.db
Desktop.ini
.DS_Store*
ehthumbs.db
Icon?

```

### `.htmlvalidate.json`

```json
{
  "extends": ["html-validate:recommended"],
  "rules": {
    "doctype-style": ["error", { "style": "lowercase" }],
    "void-style": ["error", { "style": "selfclosing" }],
    "no-inline-style": "off"
  }
}

```

### `.prettierignore`

```prettierignore
**/.git
**/node_modules
**/next/**
**/demo/build/**
**/package/dist/**
**/package.json
**/package-lock.json
**/yarn.lock
**/README.md

```

### `.prettierrc`

```prettierrc
{
  "semi": true,
  "singleQuote": true,
  "arrowParens": "always",
  "bracketSpacing": true,
  "jsxSingleQuote": false,
  "printWidth": 160,
  "tabWidth": 2,
  "trailingComma": "all"
}

```

### `config/assets.config.ts`

```ts
import { resolve } from 'path';
import { defineConfig } from 'vite';

import { bannerPlugin, getInputFiles } from './helpers';

const outDir = './package/dist';
const input = getInputFiles(resolve(__dirname, '../package/src/styles'));

export default defineConfig({
  publicDir: './package/public',
  build: {
    target: 'ES6',
    assetsDir: '',
    outDir,
    cssCodeSplit: true,
    minify: false,
    emptyOutDir: true,
    rollupOptions: {
      output: {
        inlineDynamicImports: false,
        assetFileNames: (assetInfo) =>
          assetInfo.name && ['index.css', 'layout.css'].includes(assetInfo.name) ? 'styles/[name].[ext]' : 'styles/themes/[name].[ext]',
      },
      input,
    },
  },
  plugins: [bannerPlugin(outDir)],
});

```

### `config/helpers.ts`

```ts
import { readdirSync } from 'fs';
import { resolve } from 'path';
import banner from 'vite-plugin-banner';

import { version } from '../package/public/package.json';

export const bannerPlugin = (outDir: string) =>
  banner({ outDir, content: `name: vanilla-calendar-pro v${version} | url: https://github.com/uvarov-frontend/vanilla-calendar-pro` });

export const alias = {
  '@': resolve(__dirname, '../'),
  '@package': resolve(__dirname, '../package'),
  '@src': resolve(__dirname, '../package/src'),
  '@scripts': resolve(__dirname, '../package/src/scripts'),
};

export const getInputFiles = (dir: string): string[] => {
  const files: string[] = [];

  const readDir = (path: string): void => {
    readdirSync(path, { withFileTypes: true }).forEach((item) => {
      const itemPath = resolve(path, item.name);
      if (item.isDirectory()) {
        readDir(itemPath);
      } else if (!item.name.startsWith('.')) {
        files.push(itemPath);
      }
    });
  };

  readDir(dir);
  return files;
};

```

### `config/main.config.ts`

```ts
import { resolve } from 'path';
import { defineConfig } from 'vite';
import dts from 'vite-plugin-dts';
import eslint from 'vite-plugin-eslint';

import { alias, bannerPlugin } from './helpers';

const outDir = './package/dist';

export default defineConfig({
  build: {
    target: 'ES6',
    assetsDir: '',
    outDir,
    minify: false,
    emptyOutDir: false,
    lib: {
      name: 'VanillaCalendarPro',
      formats: ['es', 'umd'],
      fileName: (format) => `index.${format === 'es' ? 'mjs' : 'js'}`,
      entry: resolve(__dirname, '../package/src/index.ts'),
    },
  },
  resolve: { alias },
  plugins: [bannerPlugin(outDir), eslint(), dts({ tsconfigPath: './tsconfig.main.json', outDir })],
});

```

### `config/utils.config.ts`

```ts
import { resolve } from 'path';
import { defineConfig } from 'vite';
import dts from 'vite-plugin-dts';
import eslint from 'vite-plugin-eslint';

import { alias, bannerPlugin } from './helpers';

const outDir = './package/dist/utils';

export default defineConfig({
  build: {
    target: 'ES6',
    assetsDir: '',
    outDir,
    minify: false,
    emptyOutDir: false,
    lib: {
      name: 'VanillaCalendarProUtils',
      formats: ['es', 'umd'],
      fileName: (format) => `index.${format === 'es' ? 'mjs' : 'js'}`,
      entry: resolve(__dirname, '../package/src/utils/index.ts'),
    },
  },
  resolve: { alias },
  plugins: [bannerPlugin(outDir), eslint(), dts({ tsconfigPath: './tsconfig.utils.json', outDir: './package/dist' })],
});

```

### `cypress.config.ts`

```ts
import { defineConfig } from 'cypress';

export default defineConfig({
  e2e: {
    video: false,
    baseUrl: 'http://localhost:5173',
  },
});

```

### `cypress/e2e/a11y.cy.ts`

```ts
// color-contrast and the landmark/region rules are excluded on purpose: they are about the demo
// page's own styling and structure, not the calendar's markup, which is what this checks.
const axeOptions = {
  runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'] },
  rules: {
    'color-contrast': { enabled: false },
    'landmark-one-main': { enabled: false },
    region: { enabled: false },
  },
};

const checkA11y = (ctx?: string) => {
  cy.injectAxe();
  cy.checkA11y(ctx as never, axeOptions as never);
};

describe('Accessibility (axe-core)', () => {
  it('default calendar view has no ARIA violations', () => {
    cy.visit('/');
    checkA11y();
  });

  it('month picker view has no ARIA violations', () => {
    cy.visit('/');
    cy.get('.vc-month').click();
    checkA11y();
  });

  it('year picker view has no ARIA violations', () => {
    cy.visit('/');
    cy.get('.vc-year').click();
    checkA11y();
  });

  it('type: multiple calendar view has no ARIA violations', () => {
    cy.visit('/pages/multiple/index.html');
    checkA11y();
  });

  it('type: week calendar view has no ARIA violations', () => {
    cy.visit('/pages/week/');
    checkA11y('#calendar-week');
  });

  it('week numbers have no ARIA violations', () => {
    cy.visit('/pages/week-numbers/');
    checkA11y();
  });

  it('collapsed calendar view has no ARIA violations', () => {
    cy.visit('/pages/gestures/');
    cy.get('#calendar-bounded [data-vc="collapse"]').click();
    cy.get('#calendar-bounded').should('have.attr', 'data-vc-type', 'week');
    checkA11y('#calendar-bounded');
  });

  it('calendars inside a shadow root have no ARIA violations', () => {
    cy.visit('/pages/shadow-dom/');
    // the inputMode popup only exists once the field has been opened
    cy.get('#widget-4').shadow().find('[data-vc-shadow-input]').click();
    cy.get('#widget-4').shadow().find('[data-vc="calendar"]').should('not.have.attr', 'data-vc-calendar-hidden');
    checkA11y();
  });

  it('every option combination carrying its own ARIA markup has no violations', () => {
    cy.visit('/pages/a11y/');
    checkA11y();
  });

  it('inputMode popup has no ARIA violations, open or closed', () => {
    cy.visit('/pages/input/');
    cy.get('#calendar-input').click();
    cy.get('[data-vc-input]').should('exist');
    checkA11y();
    cy.get('h1').click();
    cy.get('[data-vc-input]').should('have.attr', 'data-vc-calendar-hidden');
    checkA11y();
  });
});

describe('Accessibility (keyboard and focus)', () => {
  it('gives every grid a single tab stop', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-month [data-vc-months-month][tabindex="0"]').should('have.length', 1);
    cy.get('#calendar-year [data-vc-years-year][tabindex="0"]').should('have.length', 1);
    cy.get('#calendar-multiple-week-numbers [data-vc="dates"]').each(($datesEl) => {
      cy.wrap($datesEl).find('[data-vc-date-btn][tabindex="0"]').should('have.length', 1);
    });
  });

  it('anchors that tab stop on the selected date', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-ranged [data-vc-date-btn][tabindex="0"]').should('have.attr', 'aria-label', 'April 10, 2023');
  });

  it('marks the selection on the gridcell, which is the role that supports it', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-ranged [data-vc-date="2023-04-10"]').should('have.attr', 'aria-selected', 'true');
    cy.get('#calendar-ranged [data-vc-date="2023-04-10"] [data-vc-date-btn]').should('not.have.attr', 'aria-selected');
  });

  it('does not take the focus when a picker is the opening view', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-month [data-vc-months-month]').should('exist');
    cy.document().its('activeElement.tagName').should('eq', 'BODY');
  });

  it('moves the focus into the picker the user opened', () => {
    cy.visit('/');
    cy.get('.vc-year').click();
    cy.focused().should('have.attr', 'data-vc-years-year');
  });

  it('keeps the focus on the arrow while browsing the year list', () => {
    cy.visit('/');
    cy.get('.vc-year').click();
    cy.get('[data-vc-arrow="next"]').click();
    cy.focused().should('have.attr', 'data-vc-arrow', 'next');
  });

  it('moves the focus with the arrow keys without scrolling the page along', () => {
    cy.visit('/');
    cy.get('[data-vc-date-btn][tabindex="0"]').focus();
    cy.focused().trigger('keydown', { key: 'ArrowRight' });
    cy.focused().should('have.attr', 'tabindex', '0').and('have.attr', 'data-vc-date-btn');
    cy.window().its('scrollY').should('eq', 0);
  });

  it('keeps arrow-key focus inside its grid and leaves disabled dates unfocusable', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-locked-titles [data-vc-date-btn][aria-disabled="true"]').first().should('be.disabled');

    cy.get('#calendar-clickable-headers [data-vc-date-btn]').then(($buttons) => {
      cy.wrap($buttons[0]).focus().trigger('keydown', { key: 'ArrowLeft' });
      cy.focused().should('have.attr', 'data-vc-date-btn');

      cy.wrap($buttons[$buttons.length - 1])
        .focus()
        .trigger('keydown', { key: 'ArrowRight' });
      cy.focused().should('have.attr', 'data-vc-date-btn');
    });
  });

  it('gives a clickable weekday header a target big enough to hit', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-clickable-headers [data-vc-week-day-btn]')
      .first()
      .then(($btn) => {
        const { width, height } = $btn[0].getBoundingClientRect();
        expect(width).to.be.at.least(24);
        expect(height).to.be.at.least(24);
      });
  });

  it('names every time control once, and wraps none of them in an empty label', () => {
    cy.visit('/');
    cy.get('#calendar [data-vc="time"] label').should('not.exist');
    cy.get('#calendar [data-vc="time"] input[name]').then(($inputs) => {
      const names = [...$inputs].map((input) => (input as HTMLInputElement).name);
      expect(new Set(names).size, 'duplicate form control name').to.eq(names.length);
    });
  });

  it('states multiselectability only where more than one date can be picked', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-ranged [data-vc="content"]').should('have.attr', 'aria-multiselectable', 'true');
    cy.get('#calendar-popups [data-vc="content"]').should('not.have.attr', 'aria-multiselectable');
  });

  it('takes the closed popup out of the focus order and the accessibility tree', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-input').click();
    cy.get('[data-vc-input]').should('not.have.attr', 'inert');
    cy.get('[data-vc-input]').should('not.have.attr', 'aria-hidden');
    cy.get('h1').click();
    cy.get('[data-vc-input]').should('have.attr', 'inert');
    cy.get('[data-vc-input]').should('have.attr', 'aria-hidden', 'true');
  });

  it('lets the keyboard walk from the field into the popup and back out with Escape', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-input').focus().click();
    cy.get('[data-vc-input]').should('not.have.attr', 'inert');
    cy.get('#calendar-input').trigger('keydown', { key: 'ArrowDown' });
    cy.focused().should('exist');
    cy.document().then((doc) => {
      expect(doc.querySelector('[data-vc-input]')?.contains(doc.activeElement)).to.eq(true);
    });
    cy.focused().trigger('keydown', { key: 'Escape' });
    cy.focused().should('have.id', 'calendar-input');
  });

  it('tells the field that it opens a picker', () => {
    cy.visit('/pages/a11y/');
    cy.get('#calendar-input').should('have.attr', 'aria-haspopup', 'dialog').and('not.have.attr', 'aria-expanded');
    cy.get('#calendar-input').click();
    cy.get('[data-vc-input]').should('have.attr', 'role', 'dialog');
  });
});

```

### `cypress/e2e/animation.cy.ts`

```ts
const visit = () => cy.visit('/pages/animation/');

const monthOf = (id: string) => cy.get(id).find('[data-vc="month"]').invoke('attr', 'data-vc-month');

// Transitions last ~200ms, so racing them would be flaky. Starting every animation paused makes
// the intermediate state hold for as long as needed.
const freezeAnimations = () =>
  cy.window().then((win) => {
    const original = win.Element.prototype.animate;
    win.Element.prototype.animate = function (this: Element, ...args: Parameters<Element['animate']>) {
      const animation = original.apply(this, args);
      animation.pause();
      return animation;
    };
  });

const column = (index: number) => cy.get('#calendar-multiple [data-vc="column"]').eq(index);

const opacityFrames = (el: Element) => el.getAnimations().map((animation) => (animation.effect as KeyframeEffect).getKeyframes().map((frame) => frame.opacity));

const timings = (el: Element) =>
  el.getAnimations().map((animation) => {
    const timing = animation.effect!.getTiming();
    return { duration: timing.duration, easing: timing.easing };
  });

// Relative to a fixed reference, not the viewport: Cypress scrolls the element into view before
// clicking, so coordinates taken before and after a click would otherwise not be comparable.
const rowOffsets = (reference: Element, root: Element, selector: string) => {
  const referenceTop = reference.getBoundingClientRect().top;
  return [...root.querySelectorAll(selector)].map((row) => Math.round(row.getBoundingClientRect().top - referenceTop));
};

describe('Animation', () => {
  it('leaves the DOM untouched when the option is off', () => {
    visit();
    cy.get('#calendar-static').find('[data-vc-arrow="next"]').click();
    cy.get('#calendar-static').find('[data-vc-ghost]').should('not.exist');
    cy.get('#calendar-static').find('[data-vc-animating]').should('not.exist');
    cy.get('#calendar-static').find('[data-vc-clip]').should('not.exist');
    monthOf('#calendar-static').should('equal', '4');
  });

  it('keeps the outgoing month on a ghost layer while the new one is rendered', () => {
    visit();
    freezeAnimations();
    cy.get('#calendar-animated').find('[data-vc-arrow="next"]').click();

    cy.get('#calendar-animated [data-vc="dates"]').should('have.attr', 'data-vc-animating');
    cy.get('#calendar-animated [data-vc="content"]').should('have.attr', 'data-vc-clip');

    const ghost = '#calendar-animated [data-vc="content"] > [data-vc-ghost]';
    cy.get(ghost).find('[data-vc-date]').first().should('have.attr', 'data-vc-date', '2023-03-27');
    cy.get(ghost).should('have.attr', 'inert');
    cy.get(ghost).should('have.css', 'position', 'absolute');
    // proves the freeze works rather than the assertions merely being quick
    cy.wait(500);
    cy.get(ghost).should('exist');
    cy.get('#calendar-animated [data-vc="dates"] > [data-vc-dates="row"] [data-vc-date]').first().should('have.attr', 'data-vc-date', '2023-05-01');
  });

  it('removes the ghost once the animation is over and matches the static calendar', () => {
    visit();
    cy.get('#calendar-animated').find('[data-vc-arrow="next"]').click();
    cy.get('#calendar-static').find('[data-vc-arrow="next"]').click();

    cy.get('#calendar-animated [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-animated [data-vc-animating]').should('not.exist');
    cy.get('#calendar-animated [data-vc-clip]').should('not.exist');

    cy.get('#calendar-static [data-vc="dates"]')
      .invoke('html')
      .then((expected) => cy.get('#calendar-animated [data-vc="dates"]').invoke('html').should('equal', expected));
  });

  it('collapses interrupted switches instead of stacking ghosts', () => {
    visit();
    for (let n = 0; n < 4; n++) cy.get('#calendar-animated').find('[data-vc-arrow="next"]').click();
    for (let n = 0; n < 4; n++) cy.get('#calendar-static').find('[data-vc-arrow="next"]').click();

    cy.get('#calendar-animated [data-vc-ghost]').should('have.length.at.most', 1);
    monthOf('#calendar-animated').should('equal', '7');
    cy.get('#calendar-animated [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-static [data-vc="dates"]')
      .invoke('html')
      .then((expected) => cy.get('#calendar-animated [data-vc="dates"]').invoke('html').should('equal', expected));
  });

  it('cross-fades the wrapper when the calendar type changes', () => {
    visit();
    freezeAnimations();
    cy.get('#calendar-animated').find('[data-vc="month"]').click();

    cy.get('#calendar-animated [data-vc="wrapper"]').should('have.attr', 'data-vc-animating');
    cy.get('#calendar-animated > [data-vc-ghost] [data-vc="dates"]').should('exist');
    cy.get('#calendar-animated [data-vc="months"] [data-vc-months-month]').should('have.length', 12);
  });

  it('settles into the picker with no leftovers', () => {
    visit();
    cy.get('#calendar-animated').find('[data-vc="month"]').click();

    cy.get('#calendar-animated [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-animated [data-vc-animating]').should('not.exist');
    cy.get('#calendar-animated').should('have.attr', 'data-vc-type', 'month');
    cy.get('#calendar-animated [data-vc-months-month]').should('have.length', 12);
  });

  it('uses a different default duration per transition', () => {
    visit();
    freezeAnimations();

    cy.get('#calendar-animated').find('[data-vc-arrow="next"]').click();
    cy.get('#calendar-animated [data-vc="dates"]').then(($el) => {
      expect(timings($el[0])).to.deep.equal([{ duration: 250, easing: 'cubic-bezier(0.4, 0, 0.2, 1)' }]);
    });

    visit();
    freezeAnimations();
    cy.get('#calendar-animated').find('[data-vc="month"]').click();
    cy.get('#calendar-animated [data-vc="wrapper"]').then(($el) => {
      expect(timings($el[0])).to.deep.equal([{ duration: 150, easing: 'cubic-bezier(0.4, 0, 0.2, 1)' }]);
    });
  });

  it('spreads a group-less object over both kinds of transition', () => {
    visit();
    freezeAnimations();

    cy.get('#calendar-multiple').find('[data-vc-arrow="next"]').click();
    cy.get('#calendar-multiple [data-vc="dates"]')
      .first()
      .then(($el) => {
        expect(timings($el[0])).to.deep.equal([{ duration: 300, easing: 'cubic-bezier(0.4, 0, 0.2, 1)' }]);
      });

    visit();
    freezeAnimations();
    column(0).find('[data-vc="month"]').click();
    column(0)
      .find('[data-vc="wrapper"]')
      .then(($el) => {
        expect(timings($el[0])).to.deep.equal([{ duration: 300, easing: 'cubic-bezier(0.4, 0, 0.2, 1)' }]);
      });
  });

  it('resolves timings separately for slide and fade', () => {
    visit();
    freezeAnimations();

    cy.get('#calendar-custom').find('[data-vc-arrow="next"]').click();
    cy.get('#calendar-custom [data-vc="dates"]').then(($el) => {
      expect(timings($el[0])).to.deep.equal([{ duration: 700, easing: 'cubic-bezier(0.68, -0.55, 0.27, 1.55)' }]);
    });

    visit();
    freezeAnimations();
    cy.get('#calendar-custom').find('[data-vc="month"]').click();
    cy.get('#calendar-custom [data-vc="wrapper"]').then(($el) => {
      expect(timings($el[0])).to.deep.equal([{ duration: 450, easing: 'ease-in-out' }]);
    });
  });

  it('ghosts every column of a multiple calendar', () => {
    visit();
    freezeAnimations();
    cy.get('#calendar-multiple').find('[data-vc-arrow="next"]').click();

    cy.get('#calendar-multiple [data-vc="content"] > [data-vc-ghost]').should('have.length', 2);
  });

  it('switches every column of a multiple calendar with no leftovers', () => {
    visit();
    cy.get('#calendar-multiple').find('[data-vc-arrow="next"]').click();

    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-multiple').should('equal', '4');
  });

  it('animates only the column whose type changed', () => {
    visit();
    freezeAnimations();
    // mark the neighbour's cells to catch a re-render
    column(1).find('[data-vc-date]').invoke('attr', 'data-mark', '1');
    column(0).find('[data-vc="month"]').click();

    column(0).find('[data-vc-ghost]').should('have.length', 1);
    column(1).find('[data-vc-ghost]').should('not.exist');
    column(1).find('[data-vc-animating]').should('not.exist');
    column(1).find('[data-vc-date][data-mark]').should('have.length', 35);
  });

  it('animates only the column that leaves the picker', () => {
    visit();
    column(0).find('[data-vc="month"]').click();
    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');

    column(1).find('[data-vc-date]').invoke('attr', 'data-mark', '1');
    freezeAnimations();
    column(0).find('[data-vc-months-month="6"]').click();

    // closing rebuilds the whole grid, yet only the column that left the picker may animate
    column(0).find('[data-vc-ghost]').should('have.length', 1);
    column(1).find('[data-vc-ghost]').should('not.exist');
    column(1).find('[data-vc-animating]').should('not.exist');
    // the grid really was rebuilt, so the assertions above do not pass by inertia
    column(1).find('[data-vc-date][data-mark]').should('not.exist');
  });

  it('fades the dim of neighbouring columns in both directions', () => {
    visit();
    freezeAnimations();
    column(0).find('[data-vc="month"]').click();
    column(1).then(($col) => expect(opacityFrames($col[0])).to.deep.equal([['1', '0.3']]));

    // closing rebuilds the grid, so the dim has to be played back explicitly
    visit();
    column(0).find('[data-vc="month"]').click();
    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');
    freezeAnimations();
    column(0).find('[data-vc-months-month="6"]').click();
    column(1).then(($col) => expect(opacityFrames($col[0])).to.deep.equal([['0.3', '1']]));
  });

  it('keeps the outgoing rows exactly where they were', () => {
    visit();
    column(0).find('[data-vc="year"]').click();
    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');

    column(0).then(($column) => {
      const before = rowOffsets($column[0], $column[0], '[data-vc-years="row"]');
      expect(before).to.have.length(3);

      freezeAnimations();
      column(0).find('[data-vc-arrow="next"]').click();
      column(0).then(() => {
        const ghost = $column[0].querySelector('[data-vc-ghost]')!;
        expect(rowOffsets($column[0], ghost, '[data-vc-years="row"]')).to.deep.equal(before);
      });
    });
  });

  it('keeps the outgoing days in place when the type changes', () => {
    visit();
    // June (5 weeks) + July (6): the column stretches to its neighbour, and the grow-0 rule for
    // the date grid is keyed on data-vc-type, which changes mid-transition
    cy.get('#calendar-multiple').find('[data-vc-arrow="next"]').click();
    cy.get('#calendar-multiple').find('[data-vc-arrow="next"]').click();
    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');
    column(0).find('[data-vc-dates="row"]').should('have.length', 5);

    column(0).then(($column) => {
      const before = rowOffsets($column[0], $column[0], '[data-vc-dates="row"]');

      freezeAnimations();
      column(0).find('[data-vc="month"]').click();
      column(0).then(() => expect(rowOffsets($column[0], $column[0], '[data-vc-dates="row"]')).to.deep.equal(before));
    });
  });

  it('leaves untouched columns alone when one column switches type', () => {
    visit();
    column(0).find('[data-vc="month"]').click();
    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');

    column(0).find('[data-vc-months-month]').should('have.length', 12);
    column(1).find('[data-vc-date]').should('have.length', 35);
    column(1).find('[data-vc="wrapper"]').children().should('have.length.greaterThan', 0);
  });
});

export {};

```

### `cypress/e2e/collapse.cy.ts`

```ts
import type { Calendar as CalendarInstance, Options } from '../../package/src';

const visit = () => cy.visit('/pages/gestures/');

type CalendarConstructor = new (selector: HTMLElement | string, options?: Options) => CalendarInstance;

const loadCalendar = (win: Window) => {
  const projectRoot = String(Cypress.config('projectRoot')).replace(/\\/g, '/');
  const fsPath = projectRoot.startsWith('/') ? projectRoot : `/${projectRoot}`;
  const evaluate = (win as Window & { eval: (code: string) => unknown }).eval;
  return evaluate(`import(${JSON.stringify(`/@fs${fsPath}/package/src/index.ts`)})`) as Promise<{ Calendar: CalendarConstructor }>;
};

const freezeAnimations = () =>
  cy.window().then((win) => {
    const original = win.Element.prototype.animate;
    win.Element.prototype.animate = function (this: Element, ...args: Parameters<Element['animate']>) {
      const animation = original.apply(this, args);
      animation.pause();
      return animation;
    };
  });

const datesOf = (id: string) => {
  cy.get(`${id} [data-vc-ghost]`).should('not.exist');
  return cy.get(`${id} [data-vc-date]`).then(($dates) => Cypress._.map($dates, (date: HTMLElement) => date.dataset.vcDate));
};

const dragControl = (id: string, dy: number, placed = false) => {
  cy.get(`${id} [data-vc="collapse"]`).then(($el) => {
    const box = $el[0].getBoundingClientRect();
    const x = Math.round(box.left + box.width / 2);
    const y = Math.round(box.top + box.height / 2);
    const options = { pointerId: 1, isPrimary: true, button: 0, eventConstructor: 'PointerEvent', force: true } as const;

    cy.wrap($el).trigger('pointerdown', { ...options, clientX: x, clientY: y });
    cy.get(id).trigger('pointermove', { ...options, clientX: x, clientY: y + Math.sign(dy) * 12 });
    cy.get(id).trigger('pointermove', { ...options, clientX: x, clientY: y + dy });
    if (placed) cy.wait(250);
    cy.get(id).trigger('pointerup', { ...options, clientX: x, clientY: y + dy });
  });
};

describe('Collapse', () => {
  it('renders the control only where the option is on', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="collapse"]').should('exist');
    cy.get('#calendar-static [data-vc="collapse"]').should('not.exist');
    cy.get('#calendar-multiple [data-vc="collapse"]').should('not.exist');
  });

  it('reports the expanded state to assistive technology', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="collapse"]').should('have.attr', 'aria-expanded', 'true');
    cy.get('#calendar-collapsed [data-vc="collapse"]').should('have.attr', 'aria-expanded', 'false');
  });

  it('updates navigation semantics while the expanded layout is staged', () => {
    visit();
    freezeAnimations();
    cy.get('#calendar-collapsed [data-vc="collapse"]').click();

    cy.get('#calendar-collapsed [data-vc="dates"]').should('have.attr', 'data-vc-collapsing');
    cy.get('#calendar-collapsed [data-vc="collapse"]').should('have.attr', 'aria-expanded', 'true').and('have.attr', 'aria-label', 'Collapse to a single week');
    cy.get('#calendar-collapsed [data-vc-arrow="prev"]').should('have.attr', 'aria-label', 'Previous month');
    cy.get('#calendar-collapsed [data-vc-arrow="next"]').should('have.attr', 'aria-label', 'Next month');
  });

  it('does not start overlapping transitions from rapid clicks', () => {
    visit();
    freezeAnimations();
    cy.get('#calendar-gestures [data-vc="collapse"]').dblclick();

    cy.get('#calendar-gestures [data-vc="dates"]').then(($dates) => {
      expect($dates[0].getAnimations()).to.have.length(1);
      $dates[0].querySelectorAll<HTMLElement>('[data-vc-dates="row"]').forEach((row) => {
        expect(row.getAnimations()).to.have.length(1);
      });
      $dates[0].getAnimations()[0].finish();
    });

    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');
  });

  it('collapses the month onto the week holding the selected date', () => {
    visit();
    cy.get('#calendar-gestures [data-vc-dates="row"]').should('have.length', 5);

    cy.get('#calendar-gestures [data-vc="collapse"]').click();

    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');
    cy.get('#calendar-gestures [data-vc-dates="row"]').should('have.length', 1);
    datesOf('#calendar-gestures').should('deep.equal', ['2023-04-17', '2023-04-18', '2023-04-19', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23']);
    cy.get('#calendar-gestures [data-vc="collapse"]').should('have.attr', 'aria-expanded', 'false');
  });

  it('re-anchors onto a date selected after the month was rendered', () => {
    visit();
    cy.get('#calendar-gestures [data-vc-date="2023-04-03"] [data-vc-date-btn]').click();
    cy.get('#calendar-gestures [data-vc="collapse"]').click();

    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');
    datesOf('#calendar-gestures').should('deep.equal', ['2023-04-03', '2023-04-04', '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', '2023-04-09']);
  });

  it('expands back to the month around the same week', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="collapse"]').click();
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');

    cy.get('#calendar-gestures [data-vc="collapse"]').click();
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-gestures [data-vc-dates="row"]').should('have.length', 5);
    cy.get('#calendar-gestures [data-vc="collapse"]').should('have.attr', 'aria-expanded', 'true');
  });

  it('leaves nothing behind on the grid once it settles', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="collapse"]').click();
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');

    cy.get('#calendar-gestures [data-vc-collapsing]').should('not.exist');

    cy.get('#calendar-gestures [data-vc="collapse"]').click();
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-gestures [data-vc-collapsing]').should('not.exist');
    cy.get('#calendar-gestures [data-vc="dates"]').should('have.css', 'overflow', 'visible');
  });

  it('clips the grid and slides the target week up while it runs', () => {
    visit();
    freezeAnimations();
    cy.get('#calendar-gestures [data-vc="collapse"]').click();

    cy.get('#calendar-gestures [data-vc="dates"]').should('have.attr', 'data-vc-collapsing');
    cy.get('#calendar-gestures [data-vc="dates"]').should('have.css', 'overflow', 'clip');

    cy.get('#calendar-gestures [data-vc-dates="row"]').should('have.length', 5);

    cy.get('#calendar-gestures [data-vc="dates"]').then(($el) => {
      const rows = Array.from($el[0].querySelectorAll<HTMLElement>('[data-vc-dates="row"]'));
      const target = rows[3];
      const offset = target.offsetTop - rows[0].offsetTop;

      rows.forEach((row) => {
        const frames = (row.getAnimations()[0].effect as KeyframeEffect).getKeyframes();
        expect(frames[1].transform).to.equal(`translateY(${-offset}px)`);
        expect(frames[1].opacity).to.equal(row === target ? '1' : '0');
      });

      const height = ($el[0].getAnimations()[0].effect as KeyframeEffect).getKeyframes();
      expect(height[1].height).to.equal(`${target.offsetHeight}px`);
    });
  });

  it('uses the collapse timing group', () => {
    visit();
    freezeAnimations();
    cy.get('#calendar-gestures [data-vc="collapse"]').click();

    cy.get('#calendar-gestures [data-vc="dates"]').then(($el) => {
      const timing = $el[0].getAnimations()[0].effect!.getTiming();
      expect(timing.duration).to.equal(300);
      expect(timing.easing).to.equal('cubic-bezier(0.4, 0, 0.2, 1)');
    });
  });

  it('re-anchors on the month the user browsed to', () => {
    visit();
    cy.get('#calendar-gestures [data-vc-arrow="next"]').click();
    cy.get('#calendar-gestures [data-vc-arrow="next"]').click();
    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');

    cy.get('#calendar-gestures [data-vc="collapse"]').click();
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');
    datesOf('#calendar-gestures').should('deep.equal', ['2023-05-29', '2023-05-30', '2023-05-31', '2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04']);
  });

  it('steps by week once collapsed and by month once expanded', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="collapse"]').click();
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');

    cy.get('#calendar-gestures [data-vc-arrow="next"]').click();
    datesOf('#calendar-gestures').should('deep.equal', ['2023-04-24', '2023-04-25', '2023-04-26', '2023-04-27', '2023-04-28', '2023-04-29', '2023-04-30']);

    cy.get('#calendar-gestures [data-vc="collapse"]').click();
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-gestures [data-vc-arrow="next"]').click();
    cy.get('#calendar-gestures [data-vc="month"]').first().should('have.text', 'May');
  });

  it('collapses when the control is dragged up', () => {
    visit();
    dragControl('#calendar-gestures', -100);

    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');
    cy.get('#calendar-gestures [data-vc-dates="row"]').should('have.length', 1);
    cy.get('#calendar-gestures [data-vc-collapsing]').should('not.exist');
    cy.get('#calendar-gestures').should('not.have.attr', 'data-vc-dragging');
  });

  it('ignores the grabber losing implicit touch capture when capture moves to the calendar', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="collapse"]').then(($el) => {
      const box = $el[0].getBoundingClientRect();
      const x = Math.round(box.left + box.width / 2);
      const y = Math.round(box.top + box.height / 2);
      const options = { pointerId: 1, isPrimary: true, button: 0, pointerType: 'touch', eventConstructor: 'PointerEvent', force: true } as const;

      cy.wrap($el).trigger('pointerdown', { ...options, clientX: x, clientY: y });
      cy.get('#calendar-gestures').trigger('pointermove', { ...options, clientX: x, clientY: y - 12 });
      cy.wrap($el).trigger('lostpointercapture', { ...options, clientX: x, clientY: y - 12 });
      cy.get('#calendar-gestures').trigger('pointermove', { ...options, clientX: x, clientY: y - 100 });
      cy.get('#calendar-gestures').trigger('pointerup', { ...options, clientX: x, clientY: y - 100 });
    });

    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');
  });

  it('springs back when the drag stops short', () => {
    visit();
    dragControl('#calendar-gestures', -20);

    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-gestures [data-vc-dates="row"]').should('have.length', 5);
    cy.get('#calendar-gestures [data-vc-collapsing]').should('not.exist');
  });

  it('expands when the control is dragged down', () => {
    visit();
    dragControl('#calendar-collapsed', 100);

    cy.get('#calendar-collapsed').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-collapsed [data-vc-dates="row"]').should('have.length', 5);
    cy.get('#calendar-collapsed [data-vc-collapsing]').should('not.exist');
  });

  it('uses the same commit distance while expanding as while collapsing', () => {
    visit();
    dragControl('#calendar-collapsed', 50, true);

    cy.get('#calendar-collapsed').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-collapsed [data-vc-dates="row"]').should('have.length', 5);
  });

  it('does not toggle again on the click that follows a drag', () => {
    visit();
    dragControl('#calendar-gestures', -100);
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');

    cy.get('#calendar-gestures [data-vc="collapse"]').trigger('click');
    cy.get('#calendar-gestures').should('have.attr', 'data-vc-type', 'week');
  });

  it('refuses to pair with the multiple type', () => {
    visit();
    cy.get('#btn-invalid-collapse').click();
    cy.get('#log').should('contain.text', 'init() threw').and('contain.text', 'only supported by the «default» and «week»');
    cy.get('#calendar-invalid').should('not.have.attr', 'data-vc');
  });

  it('does not recreate the calendar when destroy interrupts a transition', () => {
    cy.visit('/');
    cy.window().then(async (win) => {
      const { Calendar } = await loadCalendar(win);
      const host = win.document.createElement('div');
      host.id = 'calendar-collapse-destroy';
      win.document.body.appendChild(host);

      const calendar = new Calendar(host, {
        animation: { collapse: { duration: 200 } },
        enableCollapse: true,
        selectedMonth: 3,
        selectedYear: 2023,
      });
      calendar.init();
      calendar.context.mainElement.querySelector<HTMLElement>('[data-vc="collapse"]')?.click();
      calendar.destroy();
    });

    cy.wait(300);
    cy.get('#calendar-collapse-destroy').should('not.have.attr', 'data-vc');
    cy.get('#calendar-collapse-destroy').should('be.empty');
  });

  it('does not let an interrupted transition overwrite update()', () => {
    cy.visit('/');
    cy.window().then(async (win) => {
      const { Calendar } = await loadCalendar(win);
      const host = win.document.createElement('div');
      host.id = 'calendar-collapse-update';
      win.document.body.appendChild(host);

      const calendar = new Calendar(host, {
        animation: { collapse: { duration: 200 } },
        enableCollapse: true,
        selectedMonth: 3,
        selectedYear: 2023,
      });
      calendar.init();
      calendar.context.mainElement.querySelector<HTMLElement>('[data-vc="collapse"]')?.click();
      calendar.set({ selectedMonth: 5 });
    });

    cy.wait(300);
    cy.get('#calendar-collapse-update').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-collapse-update [data-vc="month"]').should('have.attr', 'data-vc-month', '5');
  });

  it('ignores collapse controls in incomplete and picker layouts', () => {
    cy.visit('/');
    cy.window().then(async (win) => {
      const { Calendar } = await loadCalendar(win);
      const incompleteHost = win.document.createElement('div');
      win.document.body.appendChild(incompleteHost);

      const incomplete = new Calendar(incompleteHost, { enableCollapse: true, layouts: { default: '<#Collapse />' } });
      incomplete.init();
      expect(() => incomplete.context.mainElement.querySelector<HTMLElement>('[data-vc="collapse"]')?.click()).not.to.throw();
      expect(incomplete.context.currentType).to.equal('default');

      const pickerHost = win.document.createElement('div');
      win.document.body.appendChild(pickerHost);
      const picker = new Calendar(pickerHost, { enableCollapse: true, layouts: { month: '<#Collapse />' } });
      picker.init();
      picker.context.mainElement.querySelector<HTMLElement>('[data-vc="month"]')?.click();
      expect(picker.context.currentType).to.equal('month');
      expect(() => picker.context.mainElement.querySelector<HTMLElement>('[data-vc="collapse"]')?.click()).not.to.throw();
      expect(picker.context.currentType).to.equal('month');
    });
  });
});

export {};

```

### `cypress/e2e/default.cy.ts`

```ts
describe('Init default calendar', () => {
  it('Check availability of calendar', () => {
    cy.visit('/');
    cy.get('#calendar').children();
  });
  it('Check months', () => {
    cy.visit('/');
    cy.get('#calendar').find('.vc-month').should('have.attr', 'data-vc-month');
    cy.get('#calendar').find('.vc-month').click();
    cy.get('#calendar')
      .find('.vc-months')
      .find('.vc-months__month')
      .then(($month) => $month[1].click());
    cy.get('#calendar').find('.vc-month').should('have.attr', 'data-vc-month', '1');
  });
  it('Check years', () => {
    cy.visit('/');
    cy.get('#calendar').find('.vc-year').should('have.attr', 'data-vc-year');
    cy.get('#calendar').find('.vc-year').click();
    cy.get('#calendar').find('.vc-years').find('.vc-years__year[data-vc-years-year="2022"]').click();
    cy.get('#calendar').find('.vc-year').should('have.attr', 'data-vc-year', '2022');
  });
  it('Check arrows', () => {
    cy.visit('/');
    cy.get('#calendar').find('.vc-arrow.vc-arrow_next').click();
    cy.get('#calendar').find('.vc-month').should('have.attr', 'data-vc-month', '4');
    cy.get('#calendar').find('.vc-arrow.vc-arrow_next').click();
    cy.get('#calendar').find('.vc-month').should('have.attr', 'data-vc-month', '5');
    for (let n = 0; n < 6; n++) {
      cy.get('#calendar').find('.vc-arrow.vc-arrow_prev').click();
    }
    cy.get('#calendar').find('.vc-month').should('have.attr', 'data-vc-month', '11');
    cy.get('#calendar').find('.vc-year').should('have.attr', 'data-vc-year', '2022');
  });
  it('Check days', () => {
    cy.visit('/');
    cy.get('#calendar')
      .find('.vc-date__btn')
      .then(($day) => {
        expect($day).to.have.length(35);
        $day[10].click();
      });
    cy.get('#calendar').find('.vc-date[data-vc-date-selected]').should('have.attr', 'data-vc-date', '2023-04-06');
  });
});

```

### `cypress/e2e/disableDatesGaps.cy.ts`

```ts
describe('disableDatesGaps on initial load (multiple-ranged)', () => {
  it('clamps displayDateMin/Max around a pre-selected selectedDates entry right after init', () => {
    cy.visit('/pages/disable-dates-gaps/');
    // enableDates: '2022-01-10:2022-01-15' and '2022-01-24:2022-01-29', selectedDates: ['2022-01-12']
    // the gap (2022-01-16..23) should already clamp the selectable range without any click
    cy.get('[data-vc-date="2022-01-15"]').should('not.have.attr', 'data-vc-date-disabled');
    cy.get('[data-vc-date="2022-01-16"]').should('have.attr', 'data-vc-date-disabled');
    cy.get('[data-vc-date="2022-01-29"]').should('have.attr', 'data-vc-date-disabled');
  });

  it('a forced click past the gap does not extend the selected range', () => {
    cy.visit('/pages/disable-dates-gaps/');
    cy.get('[data-vc-date="2022-01-29"]').click({ force: true });
    cy.get('[data-vc-date-selected]').should('have.length', 1).and('have.attr', 'data-vc-date', '2022-01-12');
  });

  it('selecting a date within the still-open range works normally', () => {
    cy.visit('/pages/disable-dates-gaps/');
    cy.get('[data-vc-date="2022-01-14"]').click();
    cy.get('[data-vc-date-selected]').should('have.length', 3);
    cy.get('[data-vc-date="2022-01-12"]').should('have.attr', 'data-vc-date-selected', 'first');
    cy.get('[data-vc-date="2022-01-14"]').should('have.attr', 'data-vc-date-selected', 'last');
  });
});

```

### `cypress/e2e/gestureOptions.cy.ts`

```ts
const visit = () => cy.visit('/pages/gestures/');

const visitWithoutAnimationsApi = () =>
  cy.visit('/pages/gestures/', {
    onBeforeLoad(win) {
      Object.defineProperty(win.Element.prototype, 'animate', { configurable: true, value: undefined });
    },
  });

const monthOf = (id: string) => cy.get(`${id} [data-vc="month"]`).first().invoke('attr', 'data-vc-month');

const pointer = { pointerId: 1, isPrimary: true, button: 0, eventConstructor: 'PointerEvent', force: true } as const;

const dragSurface = (id: string, dx: number) => {
  cy.get(`${id} [data-vc="content"]`)
    .first()
    .then(($el) => {
      const box = $el[0].getBoundingClientRect();
      const x = Math.round(box.left + box.width / 2);
      const y = Math.round(box.top + box.height / 2);

      cy.wrap($el).trigger('pointerdown', { ...pointer, clientX: x, clientY: y });
      cy.wrap($el).trigger('pointermove', { ...pointer, clientX: x + Math.sign(dx) * 12, clientY: y });
      cy.wrap($el).trigger('pointermove', { ...pointer, clientX: x + dx, clientY: y });
      cy.get(id).trigger('pointerup', { ...pointer, clientX: x + dx, clientY: y });
    });
};

const dragControl = (id: string, dy: number) => {
  cy.get(`${id} [data-vc="collapse"]`).then(($el) => {
    const box = $el[0].getBoundingClientRect();
    const x = Math.round(box.left + box.width / 2);
    const y = Math.round(box.top + box.height / 2);

    cy.wrap($el).trigger('pointerdown', { ...pointer, clientX: x, clientY: y });
    cy.get(id).trigger('pointermove', { ...pointer, clientX: x, clientY: y + Math.sign(dy) * 12 });
    cy.get(id).trigger('pointermove', { ...pointer, clientX: x, clientY: y + dy });
    cy.get(id).trigger('pointerup', { ...pointer, clientX: x, clientY: y + dy });
  });
};

describe('Gesture option combinations', () => {
  it('collapses without enableSwipe', () => {
    visit();
    cy.get('#calendar-collapse-only [data-vc="collapse"]').click();
    cy.get('#calendar-collapse-only').should('have.attr', 'data-vc-type', 'week');

    dragSurface('#calendar-collapse-only', -300);
    cy.get('#calendar-collapse-only [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-collapse-only [data-vc-date]').should('have.length', 7);
    monthOf('#calendar-collapse-only').should('equal', '3');
  });

  it('swipes without enableCollapse', () => {
    visit();
    cy.get('#calendar-multiple [data-vc="collapse"]').should('not.exist');
    dragSurface('#calendar-multiple', -300);
    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-multiple').should('equal', '4');
  });

  it('runs both gestures with no animation option at all', () => {
    visit();
    cy.get('#calendar-plain [data-vc-dates="row"]').should('have.length', 5);

    cy.get('#calendar-plain [data-vc="collapse"]').click();
    cy.get('#calendar-plain').should('have.attr', 'data-vc-type', 'week');
    cy.get('#calendar-plain [data-vc-collapsing]').should('not.exist');

    dragControl('#calendar-plain', 100);
    cy.get('#calendar-plain').should('have.attr', 'data-vc-type', 'default');
    cy.get('#calendar-plain [data-vc-dates="row"]').should('have.length', 5);

    dragSurface('#calendar-plain', -300);
    cy.get('#calendar-plain [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-plain [data-vc-clip]').should('not.exist');
    monthOf('#calendar-plain').should('equal', '4');
  });

  it('falls back when the Web Animations API is unavailable', () => {
    visitWithoutAnimationsApi();

    cy.get('#calendar-plain [data-vc="collapse"]').click();
    cy.get('#calendar-plain').should('have.attr', 'data-vc-type', 'week');

    dragSurface('#calendar-plain', -300);
    cy.get('#calendar-plain [data-vc-date]')
      .then(($dates) => Cypress._.map($dates, (date: HTMLElement) => date.dataset.vcDate))
      .should('deep.equal', ['2023-04-24', '2023-04-25', '2023-04-26', '2023-04-27', '2023-04-28', '2023-04-29', '2023-04-30']);
  });

  it('supports both gestures in inputMode', () => {
    visit();
    cy.get('#calendar-input-gestures').click();
    cy.get('#calendar-input-popup').should('be.visible');

    dragControl('#calendar-input-popup', -100);
    cy.get('#calendar-input-popup').should('have.attr', 'data-vc-type', 'week');

    dragSurface('#calendar-input-popup', -300);
    monthOf('#calendar-input-popup').should('equal', '3');
    cy.get('#calendar-input-popup [data-vc-date]')
      .then(($dates) => Cypress._.map($dates, (date: HTMLElement) => date.dataset.vcDate))
      .should('deep.equal', ['2023-04-24', '2023-04-25', '2023-04-26', '2023-04-27', '2023-04-28', '2023-04-29', '2023-04-30']);
  });

  it('supports enabling gestures through set()', () => {
    visit();
    cy.get('#calendar-static').should('not.have.attr', 'data-vc-swipe');
    cy.get('#btn-enable-gestures').click();
    cy.get('#calendar-static').should('have.attr', 'data-vc-swipe');
    cy.get('#calendar-static [data-vc="collapse"]').should('exist');

    dragSurface('#calendar-static', -300);
    monthOf('#calendar-static').should('equal', '4');
  });

  it('leaves a calendar that asked for neither gesture untouched', () => {
    visit();
    cy.get('#calendar-static [data-vc="collapse"]').should('not.exist');
    cy.get('#calendar-static').should('not.have.attr', 'data-vc-swipe');
    dragSurface('#calendar-static', -300);
    cy.get('#calendar-static [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-static').should('equal', '3');
  });

  it('claims the touch axis only where the swipe is on', () => {
    visit();
    cy.get('#calendar-plain').should('have.attr', 'data-vc-swipe');
    cy.get('#calendar-collapse-only').should('not.have.attr', 'data-vc-swipe');
    cy.get('#calendar-collapse-only [data-vc="content"]').should('not.have.css', 'touch-action', 'pan-y');
    cy.get('#calendar-plain [data-vc="content"]').should('have.css', 'touch-action', 'pan-y');
  });

  it('gives a finger a longer leash than a mouse before taking the axis', () => {
    visit();
    const nudge = (pointerType: string, by: number) =>
      cy
        .get('#calendar-plain [data-vc="content"]')
        .first()
        .then(($el) => {
          const box = $el[0].getBoundingClientRect();
          const x = Math.round(box.left + box.width / 2);
          const y = Math.round(box.top + box.height / 2);
          cy.wrap($el).trigger('pointerdown', { ...pointer, pointerType, clientX: x, clientY: y });
          cy.wrap($el).trigger('pointermove', { ...pointer, pointerType, clientX: x + by, clientY: y });
        });

    nudge('mouse', -6);
    cy.get('#calendar-plain [data-vc-ghost]').should('exist');
    cy.get('#calendar-plain').trigger('pointercancel', { ...pointer, pointerType: 'mouse' });
    cy.get('#calendar-plain [data-vc-ghost]').should('not.exist');

    nudge('touch', -6);
    cy.get('#calendar-plain [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-plain').trigger('pointercancel', { ...pointer, pointerType: 'touch' });
  });

  it('shows a grabbing cursor while a mouse drag is active', () => {
    visit();
    cy.get('#calendar-plain [data-vc="content"]')
      .first()
      .then(($el) => {
        const box = $el[0].getBoundingClientRect();
        const x = Math.round(box.left + box.width / 2);
        const y = Math.round(box.top + box.height / 2);
        cy.wrap($el).trigger('pointerdown', { ...pointer, pointerType: 'mouse', clientX: x, clientY: y });
        cy.wrap($el).trigger('pointermove', { ...pointer, pointerType: 'mouse', clientX: x - 6, clientY: y });
      });

    cy.get('#calendar-plain').should('have.attr', 'data-vc-dragging');
    cy.get('#calendar-plain').should('have.css', 'cursor', 'grabbing');
    cy.get('#calendar-plain [data-vc-date-btn]').first().should('have.css', 'cursor', 'grabbing');

    cy.get('#calendar-plain').trigger('pointercancel', { ...pointer, pointerType: 'mouse' });
    cy.get('#calendar-plain').should('not.have.attr', 'data-vc-dragging');
  });

  it('does not smear a hover range across a mouse drag', () => {
    visit();
    cy.get('#calendar-range [data-vc-date="2023-04-05"] [data-vc-date-btn]').click();
    cy.get('#calendar-range [data-vc-date-selected]').should('have.length', 1);

    cy.get('#calendar-range [data-vc="content"]')
      .first()
      .then(($el) => {
        const box = $el[0].getBoundingClientRect();
        const x = Math.round(box.left + box.width / 2);
        const y = Math.round(box.top + box.height / 2);
        cy.wrap($el).trigger('pointerdown', { ...pointer, pointerType: 'mouse', clientX: x, clientY: y });
        cy.wrap($el).trigger('pointermove', { ...pointer, pointerType: 'mouse', clientX: x - 12, clientY: y });
        cy.wrap($el).trigger('pointermove', { ...pointer, pointerType: 'mouse', clientX: x - 120, clientY: y });
        cy.wrap($el).trigger('mousemove', { clientX: x - 120, clientY: y, force: true });
      });

    cy.get('#calendar-range [data-vc-date-hover]').should('not.exist');
    cy.get('#calendar-range').trigger('pointercancel', { ...pointer, pointerType: 'mouse' });
    cy.get('#calendar-range [data-vc-ghost]').should('not.exist');
  });

  it('makes no part of the calendar selectable, bar the fields meant to be edited', () => {
    visit();
    cy.get('#calendar-static').should('have.css', 'user-select', 'none');

    ['[data-vc="header"]', '[data-vc="month"]', '[data-vc-week-day]', '[data-vc-date]', '[data-vc-date-btn]'].forEach((selector) =>
      cy.get(`#calendar-static ${selector}`).first().should('have.css', 'user-select', 'none'),
    );
  });

  it('leaves the time fields selectable', () => {
    cy.visit('/');
    cy.get('[data-vc="calendar"]').should('have.css', 'user-select', 'none');
    cy.get('[data-vc-time-input="hour"] input').should('have.css', 'user-select', 'text');
    cy.get('[data-vc-time-input="minute"] input').should('have.css', 'user-select', 'text');
  });

  it('refuses only the one pairing that cannot work', () => {
    visit();
    cy.get('#btn-invalid-collapse').click();
    cy.get('#log').should('contain.text', 'init() threw').and('contain.text', 'only supported by the «default» and «week»');
  });
});

export {};

```

### `cypress/e2e/lifecycleGuards.cy.ts`

```ts
describe('init()/destroy() lifecycle guards', () => {
  it('calling init() twice on the same instance throws, and does not corrupt the DOM', () => {
    cy.visit('/pages/lifecycle/');
    cy.get('#btn-init').click();
    cy.get('#log').should('contain.text', 'init() OK');

    cy.get('#btn-init').click();
    cy.get('#log').should('contain.text', 'init() threw').and('contain.text', 'already been initialized');

    cy.get('#calendar').should('exist').and('have.attr', 'data-vc', 'calendar');
  });

  it('calling destroy() twice on the same instance throws, without removing the element', () => {
    cy.visit('/pages/lifecycle/');
    cy.get('#btn-init').click();
    cy.get('#btn-destroy').click();
    cy.get('#log').should('contain.text', 'destroy() OK');

    cy.get('#btn-destroy').click();
    cy.get('#log').should('contain.text', 'destroy() threw').and('contain.text', 'already been destroyed');

    cy.get('#calendar').should('exist');
  });
});

```

### `cypress/e2e/multiple.cy.ts`

```ts
describe('Init multiple calendar', () => {
  it('Check availability of calendar', () => {
    cy.visit('/pages/multiple/index.html');
    cy.get('#calendar').children();
  });
  it('Check months', () => {
    cy.visit('/pages/multiple/index.html');
    cy.get('#calendar')
      .find('.vc-month')
      .then(($month) => {
        expect($month).to.have.length(2);
      });
  });
  it('Check years', () => {
    cy.visit('/pages/multiple/index.html');
    cy.get('#calendar')
      .find('.vc-year')
      .then(($year) => {
        expect($year).to.have.length(2);
      });
  });
  it('Check arrows', () => {
    cy.visit('/pages/multiple/index.html');
    cy.get('#calendar').find('.vc-arrow.vc-arrow_next').click();
    cy.get('#calendar').find('.vc-month:first').should('have.attr', 'data-vc-month', '4');
    cy.get('#calendar').find('.vc-month:last').should('have.attr', 'data-vc-month', '5');
    for (let n = 0; n < 5; n++) {
      cy.get('#calendar').find('.vc-arrow.vc-arrow_prev').click();
    }
    cy.get('#calendar').find('.vc-month:first').should('have.attr', 'data-vc-month', '11');
    cy.get('#calendar').find('.vc-month:last').should('have.attr', 'data-vc-month', '0');
    cy.get('#calendar').find('.vc-year:first').should('have.attr', 'data-vc-year', '2022');
    cy.get('#calendar').find('.vc-year:last').should('have.attr', 'data-vc-year', '2023');
  });
  it('Check days', () => {
    cy.visit('/pages/multiple/index.html');
    cy.get('#calendar')
      .find('.vc-date__btn')
      .then(($day) => {
        expect($day).to.have.length(70);
        $day[30].click();
      });
    cy.get('#calendar')
      .find('.vc-date__btn')
      .then(($day) => $day[45].click());
    cy.get('#calendar')
      .find('.vc-date[data-vc-date-selected]')
      .then(($day) => expect($day).to.have.length(16));
    cy.get('#calendar')
      .find('.vc-date__btn')
      .then(($day) => $day[45].click());
    cy.get('#calendar')
      .find('.vc-date__btn')
      .then(($day) => $day[45].click());
    cy.get('#calendar')
      .find('.vc-date')
      .then(($day) => expect($day).not.to.be.attr('data-vc-date-selected'));
  });
});

```

### `cypress/e2e/popupsRange.cy.ts`

```ts
describe('popups with a date-range key', () => {
  it('applies the same popup to every day in the range', () => {
    cy.visit('/pages/popups-range/');
    const days = ['10', '11', '12', '13', '14', '15', '16', '17'];
    days.forEach((d) => {
      cy.get(`[data-vc-date="2026-02-${d}"] [data-vc-date-popup]`).should('exist').and('contain.text', "Fred's vacation");
      cy.get(`[data-vc-date="2026-02-${d}"] [data-vc-date-btn]`).should('have.class', 'bg-orange');
    });
  });

  it('does not apply the popup outside the range', () => {
    cy.visit('/pages/popups-range/');
    cy.get('[data-vc-date="2026-02-09"] [data-vc-date-popup]').should('not.exist');
    cy.get('[data-vc-date="2026-02-18"] [data-vc-date-popup]').should('not.exist');
  });
});

```

### `cypress/e2e/shadowDom.cy.ts`

```ts
// Real pointer events are composed, so a synthetic drag has to be as well: without it the
// pointermove/pointerup pair never leaves the shadow root and window never sees the gesture.
const dispatch = (el: Element, type: string, clientX: number, clientY: number) =>
  el.dispatchEvent(
    new PointerEvent(type, {
      pointerId: 1,
      isPrimary: true,
      button: 0,
      buttons: type === 'pointerup' ? 0 : 1,
      clientX,
      clientY,
      bubbles: true,
      cancelable: true,
      composed: true,
    }),
  );

const swipeInside = (widget: string, dx: number) => {
  cy.get(widget)
    .shadow()
    .find('[data-vc="content"]')
    .first()
    .then(($el) => {
      const box = $el[0].getBoundingClientRect();
      const x = Math.round(box.left + box.width / 2);
      const y = Math.round(box.top + box.height / 2);
      dispatch($el[0], 'pointerdown', x, y);
      dispatch($el[0], 'pointermove', x + Math.sign(dx) * 12, y);
      dispatch($el[0], 'pointermove', x + dx, y);
      cy.wait(250);
      dispatch($el[0], 'pointerup', x + dx, y);
    });
};

const monthOf = (widget: string) => cy.get(widget).shadow().find('[data-vc="month"]').first().invoke('attr', 'data-vc-month');

describe('Shadow DOM support', () => {
  it('renders the popup inside the shadow root, not in document.body', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-1').shadow().find('[data-vc-shadow-input]').click();
    cy.get('#widget-1').shadow().find('[data-vc="calendar"]').should('exist').and('not.have.attr', 'data-vc-calendar-hidden');
    cy.get('body').find('> [data-vc-input]').should('not.exist');
  });

  it('clicking a date inside the shadow-DOM calendar does not close it', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-1').shadow().find('[data-vc-shadow-input]').click();
    cy.get('#widget-1').shadow().find('[data-vc-date-btn]').first().click();
    cy.get('#widget-1').shadow().find('[data-vc="calendar"]').should('not.have.attr', 'data-vc-calendar-hidden');
  });

  it('clicking outside (light DOM) closes the shadow-DOM calendar', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-1').shadow().find('[data-vc-shadow-input]').click();
    cy.get('#light-dom-outside').click({ force: true });
    cy.get('#widget-1').shadow().find('[data-vc="calendar"]').should('have.attr', 'data-vc-calendar-hidden');
  });

  it('two independent shadow-DOM instances do not interfere with each other', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-1').shadow().find('[data-vc-shadow-input]').click();
    cy.get('#widget-1').shadow().find('[data-vc="calendar"]').should('not.have.attr', 'data-vc-calendar-hidden');
    cy.get('#widget-2').shadow().find('[data-vc="calendar"]').should('not.exist');
  });

  it('destroy() removes the calendar behavior but keeps the input in the shadow DOM', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-1').shadow().find('[data-vc-shadow-destroy]').click();
    cy.get('#widget-1').shadow().find('[data-vc-shadow-input]').should('exist');
    cy.get('#widget-1').shadow().find('[data-vc="calendar"]').should('not.exist');
  });

  it('clicking Destroy twice in a row does not remove the input (regression: destroy() must be idempotent-safe)', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-1').shadow().find('[data-vc-shadow-destroy]').click();
    // the demo clears its own calendar reference after destroy, so a second click is a no-op;
    // this guards the UI-level behavior, while the library itself also rejects a raw double-call
    cy.get('#widget-1').shadow().find('[data-vc-shadow-destroy]').click();
    cy.get('#widget-1').shadow().find('[data-vc-shadow-input]').should('exist');
  });

  it('Init after Destroy creates a fresh, working calendar instance', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-1').shadow().find('[data-vc-shadow-destroy]').click();
    cy.get('#widget-1').shadow().find('[data-vc-shadow-init]').click();
    cy.get('#widget-1').shadow().find('[data-vc-shadow-input]').click();
    cy.get('#widget-1').shadow().find('[data-vc="calendar"]').should('exist').and('not.have.attr', 'data-vc-calendar-hidden');
  });

  it('collapses and swipes a plain calendar inside the shadow root', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-5').shadow().find('[data-vc="collapse"]').click();
    cy.get('#widget-5').shadow().find('[data-vc="calendar"]').should('have.attr', 'data-vc-type', 'week');
    cy.get('#widget-5').shadow().find('[data-vc="collapse"]').click();
    cy.get('#widget-5').shadow().find('[data-vc="calendar"]').should('have.attr', 'data-vc-type', 'default');

    monthOf('#widget-5').should('eq', '3');
    swipeInside('#widget-5', -200);
    monthOf('#widget-5').should('eq', '4');
  });

  it('collapses and swipes the popup of an inputMode calendar inside the shadow root', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-4').shadow().find('[data-vc-shadow-input]').click();
    cy.get('#widget-4').shadow().find('[data-vc="calendar"]').should('not.have.attr', 'data-vc-calendar-hidden');

    cy.get('#widget-4').shadow().find('[data-vc="collapse"]').click();
    cy.get('#widget-4').shadow().find('[data-vc="calendar"]').should('have.attr', 'data-vc-type', 'week');

    monthOf('#widget-4').should('eq', '3');
    swipeInside('#widget-4', -200);
    cy.get('#widget-4').shadow().find('[data-vc="calendar"]').should('not.have.attr', 'data-vc-calendar-hidden');
  });

  it('a plain (non-inputMode) calendar renders directly inside the shadow root and dates are clickable', () => {
    cy.visit('/pages/shadow-dom/');
    cy.get('#widget-3').shadow().find('[data-vc="calendar"]').should('exist');
    cy.get('#widget-3').shadow().find('[data-vc-date-btn]').first().click();
    cy.get('#widget-3').shadow().find('[data-vc-date-selected]').should('exist');
  });
});

```

### `cypress/e2e/swipe.cy.ts`

```ts
const visit = () => cy.visit('/pages/gestures/');

const monthOf = (id: string) => cy.get(`${id} [data-vc="month"]`).first().invoke('attr', 'data-vc-month');

const surface = (id: string) => cy.get(`${id} [data-vc="content"]`).first();

const dragBy = (id: string, dx: number, dy = 0) => {
  surface(id).then(($el) => {
    const box = $el[0].getBoundingClientRect();
    const startX = Math.round(box.left + box.width / 2);
    const startY = Math.round(box.top + box.height / 2);
    const options = { pointerId: 1, isPrimary: true, button: 0, eventConstructor: 'PointerEvent', force: true } as const;

    cy.wrap($el).trigger('pointerdown', { ...options, clientX: startX, clientY: startY });
    cy.wrap($el).trigger('pointermove', { ...options, clientX: startX + Math.sign(dx) * 12, clientY: startY + Math.sign(dy) * 12 });
    cy.wrap($el).trigger('pointermove', { ...options, clientX: startX + dx, clientY: startY + dy });
  });
};

const release = (id: string, dx: number, dy = 0) => {
  surface(id).then(($el) => {
    const box = $el[0].getBoundingClientRect();
    cy.wrap($el).trigger('pointerup', {
      pointerId: 1,
      isPrimary: true,
      button: 0,
      eventConstructor: 'PointerEvent',
      force: true,
      clientX: Math.round(box.left + box.width / 2) + dx,
      clientY: Math.round(box.top + box.height / 2) + dy,
    });
  });
};

const rest = () => cy.wait(250);

const flick = (id: string, dx: number, dy = 0) => {
  dragBy(id, dx, dy);
  release(id, dx, dy);
};

const swipe = (id: string, dx: number, dy = 0) => {
  dragBy(id, dx, dy);
  rest();
  release(id, dx, dy);
};

const raw = (el: Element, type: string, clientX: number, clientY: number) =>
  el.dispatchEvent(
    new PointerEvent(type, {
      pointerId: 1,
      isPrimary: true,
      button: 0,
      buttons: type === 'pointerup' ? 0 : 1,
      clientX,
      clientY,
      bubbles: true,
      cancelable: true,
    }),
  );

const assertClipped = (id: string) => {
  cy.get(id).then(($cal) => {
    $cal[0].querySelectorAll<HTMLElement>('[data-vc-ghost]').forEach((ghost) => {
      const parent = ghost.parentElement as HTMLElement;
      expect(parent.hasAttribute('data-vc-clip'), 'ghost parent is marked as clipping').to.equal(true);
      expect(getComputedStyle(parent).overflow, 'ghost parent actually clips').to.equal('clip');
      expect(getComputedStyle(parent).position, 'ghost is positioned against its clipping parent').to.equal('relative');
    });
  });
};

describe('Swipe', () => {
  it('ignores pointers when the option is off', () => {
    visit();
    swipe('#calendar-static', -300);
    cy.get('#calendar-static [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-static').should('equal', '3');
  });

  it('stages the neighbouring month without moving the calendar onto it', () => {
    visit();
    dragBy('#calendar-gestures', -120);

    cy.get('#calendar-gestures [data-vc="dates"]').should('have.attr', 'data-vc-animating');
    cy.get('#calendar-gestures [data-vc="content"]').should('have.attr', 'data-vc-clip');

    cy.get('#calendar-gestures').then(($cal) => {
      const cal = $cal[0];
      const inGhost = [...cal.querySelectorAll<HTMLElement>('[data-vc-ghost] [data-vc-date]')].map((date) => date.dataset.vcDate);
      const live = [...cal.querySelectorAll<HTMLElement>('[data-vc="dates"] [data-vc-date]')].map((date) => date.dataset.vcDate);

      expect(live, 'the real grid still holds the current month').to.include('2023-04-15');
      expect(inGhost, 'the ghost holds the incoming month').to.include('2023-05-15');
      expect(cal.querySelector('[data-vc="month"]')).to.have.text('April');
    });

    release('#calendar-gestures', -120);
  });

  it('keeps the content under the finger, pixel for pixel', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="dates"]').then(($grid) => {
      const width = $grid[0].offsetWidth;

      [0.1, 0.25, 0.5, 0.75].forEach((fraction) => {
        const by = -Math.round(width * fraction);
        dragBy('#calendar-gestures', by);

        cy.get('#calendar-gestures [data-vc="dates"]').then(($el) => {
          const moved = new DOMMatrix(getComputedStyle($el[0]).transform).m41;
          expect(Math.abs(moved - by), `content follows the finger at ${fraction * width}px`).to.be.lessThan(2);
        });

        cy.get('#calendar-gestures').trigger('pointercancel', { pointerId: 1, isPrimary: true, eventConstructor: 'PointerEvent', force: true });
        cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
      });
    });
  });

  it('commits to the next month when the drag is long enough', () => {
    visit();
    swipe('#calendar-gestures', -300);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '4');
    cy.get('#calendar-gestures [data-vc="month"]').first().should('have.text', 'May');
  });

  it('commits to the previous month when dragged the other way', () => {
    visit();
    swipe('#calendar-gestures', 300);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '2');
  });

  it('falls back when a placed drag stops short of the threshold', () => {
    visit();
    swipe('#calendar-gestures', -20);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-gestures [data-vc-animating]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '3');
    cy.get('#calendar-gestures [data-vc-date]').should('have.length', 35);
  });

  it('eases a short placed drag back instead of rewinding its tiny timeline slice', () => {
    visit();
    dragBy('#calendar-gestures', -34);
    rest();

    let play: typeof Animation.prototype.play | null = null;
    cy.window().then((win) => {
      const originalPlay = win.Animation.prototype.play;
      play = originalPlay;
      win.Animation.prototype.play = function () {
        originalPlay.call(this);
        this.pause();
      };
    });
    release('#calendar-gestures', -34);

    cy.get('#calendar-gestures [data-vc="dates"]').then(($dates) => {
      const animation = $dates[0].getAnimations()[0];
      const timing = animation.effect!.getTiming();
      const frames = (animation.effect as KeyframeEffect).getKeyframes();

      expect(timing.duration).to.equal(200);
      expect(timing.easing).to.equal('cubic-bezier(0.4, 0, 0.2, 1)');
      expect(frames[0].transform).not.to.equal('none');
      expect(frames[1].transform).to.equal('none');
      animation.finish();
    });
    cy.window().then((win) => {
      if (play) win.Animation.prototype.play = play;
    });

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '3');
  });

  it('commits a placed drag of a couple of days, with no flick behind it', () => {
    visit();
    swipe('#calendar-gestures', -70);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '4');
  });

  it('commits a short flick, which never reaches the threshold', () => {
    visit();
    flick('#calendar-gestures', -30);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '4');
  });

  it('follows the direction a flick was thrown, not the ground it covered', () => {
    visit();
    dragBy('#calendar-gestures', -200);
    rest();
    surface('#calendar-gestures').then(($el) => {
      const box = $el[0].getBoundingClientRect();
      const x = Math.round(box.left + box.width / 2);
      const y = Math.round(box.top + box.height / 2);
      const options = { pointerId: 1, isPrimary: true, button: 0, eventConstructor: 'PointerEvent', force: true } as const;
      cy.wrap($el).trigger('pointermove', { ...options, clientX: x - 150, clientY: y });
      cy.wrap($el).trigger('pointermove', { ...options, clientX: x - 100, clientY: y });
      cy.wrap($el).trigger('pointerup', { ...options, clientX: x - 100, clientY: y });
    });

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '3');
  });

  it('leaves the vertical axis to the page', () => {
    visit();
    swipe('#calendar-gestures', 0, -200);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '3');
  });

  it('does not select the date the finger was released over', () => {
    visit();
    cy.get('#calendar-gestures [data-vc-date-selected]').should('have.length', 1);
    swipe('#calendar-gestures', -300);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-gestures [data-vc-date-selected]').should('not.exist');
  });

  it('moves every column of a multiple calendar together', () => {
    visit();
    dragBy('#calendar-multiple', -120);
    cy.get('#calendar-multiple [data-vc="content"] > [data-vc-ghost]').should('have.length', 2);
    release('#calendar-multiple', -300);

    cy.get('#calendar-multiple [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-multiple').should('equal', '4');
  });

  it('steps a week at a time once collapsed', () => {
    visit();
    cy.get('#calendar-collapsed [data-vc-date]').should('have.length', 7);
    swipe('#calendar-collapsed', -300);

    cy.get('#calendar-collapsed [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-collapsed [data-vc-date]')
      .then(($dates) => Cypress._.map($dates, (date: HTMLElement) => date.dataset.vcDate))
      .should('deep.equal', ['2023-04-24', '2023-04-25', '2023-04-26', '2023-04-27', '2023-04-28', '2023-04-29', '2023-04-30']);
  });

  it('survives a finish event that lands after the next gesture started', () => {
    visit();
    cy.get('#calendar-gestures [data-vc="content"]').then(($el) => {
      const el = $el[0];
      const box = el.getBoundingClientRect();
      const x = Math.round(box.left + box.width / 2);
      const y = Math.round(box.top + box.height / 2);

      raw(el, 'pointerdown', x, y);
      raw(el, 'pointermove', x - 12, y);
      raw(el, 'pointermove', x - 300, y);
      raw(el, 'pointerup', x - 300, y);

      el.getAnimations({ subtree: true }).forEach((animation) => animation.finish());
      raw(el, 'pointerdown', x, y);
      raw(el, 'pointermove', x - 12, y);
      raw(el, 'pointermove', x - 200, y);
    });

    assertClipped('#calendar-gestures');
  });

  it('keeps every ghost clipped through a burst of interrupted swipes', () => {
    visit();
    for (let n = 0; n < 5; n++) {
      dragBy('#calendar-gestures', -200);
      release('#calendar-gestures', -200);
      assertClipped('#calendar-gestures');
    }
    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-gestures [data-vc-clip]').should('not.exist');
  });

  it('cannot be scrolled sideways by focus while a swipe is running', () => {
    visit();
    dragBy('#calendar-gestures', -200);
    cy.get('#calendar-gestures [data-vc="content"]').then(($el) => {
      const content = $el[0];
      (content.querySelector('[data-vc="dates"] [data-vc-date-btn]') as HTMLElement).focus();
      expect(content.scrollLeft, 'clip container scrolled sideways').to.equal(0);
      expect(content.scrollTop, 'clip container scrolled vertically').to.equal(0);
    });
    release('#calendar-gestures', -200);
  });

  it('settles back when the pointer is taken away mid-drag', () => {
    visit();
    dragBy('#calendar-gestures', -150);
    cy.get('#calendar-gestures [data-vc-ghost]').should('exist');

    surface('#calendar-gestures').trigger('pointercancel', { pointerId: 1, isPrimary: true, eventConstructor: 'PointerEvent', force: true });

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-gestures [data-vc-clip]').should('not.exist');
    cy.get('#calendar-gestures [data-vc-animating]').should('not.exist');
    cy.get('#calendar-gestures').should('not.have.attr', 'data-vc-dragging');
    monthOf('#calendar-gestures').should('equal', '3');
  });

  it('recovers when a drag is left hanging and never released', () => {
    visit();
    dragBy('#calendar-gestures', -150);
    cy.get('#calendar-gestures [data-vc-ghost]').should('exist');

    cy.get('#calendar-gestures').trigger('lostpointercapture', { pointerId: 1, isPrimary: true, eventConstructor: 'PointerEvent', force: true });
    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');

    swipe('#calendar-gestures', -300);
    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '4');
  });

  it('ends the drag when the pointer is released far outside the calendar', () => {
    visit();
    dragBy('#calendar-gestures', -300);
    surface('#calendar-gestures').trigger('pointerup', {
      pointerId: 1,
      isPrimary: true,
      button: 0,
      eventConstructor: 'PointerEvent',
      force: true,
      clientX: -4000,
      clientY: -4000,
    });

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-gestures [data-vc-clip]').should('not.exist');
    cy.get('#calendar-gestures').should('not.have.attr', 'data-vc-dragging');
    monthOf('#calendar-gestures').should('equal', '4');
  });

  it('does not move two periods for one gesture', () => {
    visit();
    dragBy('#calendar-gestures', -300);
    release('#calendar-gestures', -300);
    release('#calendar-gestures', -300);

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '4');
  });

  it('keeps the header in step with the grid', () => {
    visit();
    const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    for (const dx of [-300, -300, 300, -40, -300]) {
      swipe('#calendar-gestures', dx);
      cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
      cy.get('#calendar-gestures').then(($cal) => {
        const cal = $cal[0];
        const title = (cal.querySelector('[data-vc="month"]') as HTMLElement).innerText;
        const anchor = [...cal.querySelectorAll<HTMLElement>('[data-vc-date-month="current"]')][14].dataset.vcDate as string;
        expect(monthNames[Number(anchor.slice(5, 7)) - 1], `header matches the grid (${anchor})`).to.equal(title);
      });
    }
  });

  it('leaves no gesture state behind after a stray tap', () => {
    visit();
    surface('#calendar-gestures').trigger('pointerdown', { pointerId: 1, isPrimary: true, button: 0, eventConstructor: 'PointerEvent', force: true });
    surface('#calendar-gestures').trigger('pointerup', { pointerId: 1, isPrimary: true, button: 0, eventConstructor: 'PointerEvent', force: true });

    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    cy.get('#calendar-gestures [data-vc-clip]').should('not.exist');
    cy.get('#calendar-gestures').should('not.have.attr', 'data-vc-dragging');

    cy.get('#calendar-gestures [data-vc-date="2023-04-05"] [data-vc-date-btn]').click();
    cy.get('#calendar-gestures [data-vc-date-selected]').should('have.attr', 'data-vc-date', '2023-04-05');
  });

  it('recovers when pointerup happens outside before capture', () => {
    visit();
    surface('#calendar-gestures').then(($el) => {
      const box = $el[0].getBoundingClientRect();
      raw($el[0], 'pointerdown', Math.round(box.left + box.width / 2), Math.round(box.top + box.height / 2));
    });
    cy.window().then((win) => raw(win.document.body, 'pointerup', 0, 0));

    swipe('#calendar-gestures', -300);
    cy.get('#calendar-gestures [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-gestures').should('equal', '4');
  });

  it('stops where the arrows stop', () => {
    visit();
    cy.get('#calendar-bounded [data-vc-arrow="next"]').should('not.be.visible');
    swipe('#calendar-bounded', -300);
    cy.get('#calendar-bounded [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-bounded').should('equal', '3');

    swipe('#calendar-bounded', 300);
    cy.get('#calendar-bounded [data-vc-ghost]').should('not.exist');
    monthOf('#calendar-bounded').should('equal', '2');
  });
});

export {};

```

### `cypress/e2e/week.cy.ts`

```ts
const visit = () => cy.visit('/pages/week/');

const datesOf = (id: string) => {
  cy.get(`${id} [data-vc-ghost]`).should('not.exist');
  return cy.get(`${id} [data-vc-date]`).then(($dates) => Cypress._.map($dates, (date: HTMLElement) => date.dataset.vcDate));
};

const titleOf = (id: string) => cy.get(`${id} [data-vc="month"]`).first().invoke('text');

describe('Week type', () => {
  it('renders a single row of seven days', () => {
    visit();
    cy.get('#calendar-week [data-vc-dates="row"]').should('have.length', 1);
    cy.get('#calendar-week [data-vc-date]').should('have.length', 7);
    cy.get('#calendar-week').should('have.attr', 'data-vc-type', 'week');
  });

  it('anchors on the week holding the first day of the selected month', () => {
    visit();
    datesOf('#calendar-week').should('deep.equal', ['2023-03-27', '2023-03-28', '2023-03-29', '2023-03-30', '2023-03-31', '2023-04-01', '2023-04-02']);
    titleOf('#calendar-week').should('equal', 'April');
  });

  it('anchors on the selected date when there is one', () => {
    visit();
    datesOf('#calendar-week-numbers').should('deep.equal', ['2023-04-17', '2023-04-18', '2023-04-19', '2023-04-20', '2023-04-21', '2023-04-22', '2023-04-23']);
    cy.get('#calendar-week-numbers [data-vc-date-selected]').should('have.attr', 'data-vc-date', '2023-04-19');
  });

  it('steps a week at a time with the arrows', () => {
    visit();
    cy.get('#calendar-week [data-vc-arrow="next"]').click();
    datesOf('#calendar-week').should('deep.equal', ['2023-04-03', '2023-04-04', '2023-04-05', '2023-04-06', '2023-04-07', '2023-04-08', '2023-04-09']);

    cy.get('#calendar-week [data-vc-arrow="prev"]').click();
    cy.get('#calendar-week [data-vc-arrow="prev"]').click();
    datesOf('#calendar-week').should('deep.equal', ['2023-03-20', '2023-03-21', '2023-03-22', '2023-03-23', '2023-03-24', '2023-03-25', '2023-03-26']);
  });

  it('titles a straddling week by the month that owns it', () => {
    visit();
    titleOf('#calendar-week').should('equal', 'April');
    cy.get('#calendar-week [data-vc-arrow="prev"]').click();
    titleOf('#calendar-week').should('equal', 'March');
  });

  it('marks every day of the strip as belonging to the current month', () => {
    visit();
    cy.get('#calendar-week [data-vc-date-month="current"]').should('have.length', 7);
    cy.get('#calendar-week [data-vc-date-btn]').should('have.length', 7);
  });

  it('numbers the displayed week', () => {
    visit();
    cy.get('#calendar-week-numbers [data-vc-week-number]').should('have.length', 1);
    cy.get('#calendar-week-numbers [data-vc-week-number]').should('have.attr', 'data-vc-week-number', '16');
  });

  it('returns to the week after a trip through the month picker', () => {
    visit();
    cy.get('#calendar-week [data-vc="month"]').click();
    cy.get('#calendar-week [data-vc-months-month]').should('have.length', 12);

    cy.get('#calendar-week [data-vc-months-month="6"]').click();
    cy.get('#calendar-week').should('have.attr', 'data-vc-type', 'week');
    cy.get('#calendar-week [data-vc-dates="row"]').should('have.length', 1);
    datesOf('#calendar-week').should('deep.equal', ['2023-06-26', '2023-06-27', '2023-06-28', '2023-06-29', '2023-06-30', '2023-07-01', '2023-07-02']);
  });

  it('returns to the week after a trip through the year picker', () => {
    visit();
    cy.get('#calendar-week [data-vc="year"]').click();
    cy.get('#calendar-week [data-vc-years-year]').should('have.length', 15);

    cy.get('#calendar-week [data-vc-years-year="2024"]').click();
    cy.get('#calendar-week').should('have.attr', 'data-vc-type', 'week');
    cy.get('#calendar-week [data-vc-date]').should('have.length', 7);
    titleOf('#calendar-week').should('equal', 'April');
  });

  it('re-anchors the displayed dates when firstWeekday changes', () => {
    visit();
    cy.get('#btn-sunday-first').click();

    cy.get('#calendar-week [data-vc-week-day]').first().should('have.attr', 'data-vc-week-day', '0');
    cy.get('#calendar-week [data-vc-date]').first().should('have.attr', 'data-vc-date', '2023-03-26');
  });

  it('does not cross a year when year switching is disabled', () => {
    visit();
    cy.get('#calendar-week-year-locked [data-vc-arrow="next"]').should('not.be.visible');
    datesOf('#calendar-week-year-locked').should('deep.equal', [
      '2023-12-25',
      '2023-12-26',
      '2023-12-27',
      '2023-12-28',
      '2023-12-29',
      '2023-12-30',
      '2023-12-31',
    ]);
  });
});

export {};

```

### `cypress/e2e/weekNumbers.cy.ts`

```ts
const getMiddles = (containerSelector: string, itemSelector: string) =>
  cy
    .get(containerSelector)
    .find(itemSelector)
    .then(($els) => [...$els].map((el) => Math.round(el.getBoundingClientRect().top + el.getBoundingClientRect().height / 2)));

const getRowWeekNumbers = (containerSelector: string) =>
  cy
    .get(containerSelector)
    .find('[data-vc-week-number]')
    .then(($weeks) => [...$weeks].map((el) => Number(el.dataset.vcWeekNumber)));

describe('Week numbers', () => {
  it('December 2026 ends on week 53 (2026 is a 53-ISO-week year)', () => {
    cy.visit('/pages/week-numbers/');
    getRowWeekNumbers('#calendar-2026').should('deep.equal', [49, 50, 51, 52, 53]);
    cy.get('#calendar-2026').find('[data-vc-week-number="53"]').should('have.attr', 'data-vc-week-year', '2026');
  });

  it('December 2025 rolls its last row into week 1 of 2026 (2025 is a 52-ISO-week year)', () => {
    cy.visit('/pages/week-numbers/');
    getRowWeekNumbers('#calendar-2025').should('deep.equal', [49, 50, 51, 52, 1]);
    cy.get('#calendar-2025').find('[data-vc-week-number="1"]').should('have.attr', 'data-vc-week-year', '2026');
  });

  it('firstWeekday=0 (Sunday-start weeks) still numbers rows sequentially with no gaps or duplicates', () => {
    cy.visit('/pages/week-numbers/');
    getRowWeekNumbers('#calendar-sunday-start').should('deep.equal', [22, 23, 24, 25, 26]);
  });

  it('lines every number up with the row it counts', () => {
    cy.visit('/pages/week-numbers/');
    ['#calendar-2026', '#calendar-2025', '#calendar-sunday-start'].forEach((calendar) => {
      getMiddles(calendar, '[data-vc-dates="row"]').then((rows) => {
        getMiddles(calendar, '[data-vc-week-number]').should('deep.equal', rows);
      });
    });
  });

  it('lines them up under a clickable weekday header too', () => {
    cy.visit('/pages/a11y/');
    getMiddles('#calendar-clickable-headers', '[data-vc-dates="row"]').then((rows) => {
      getMiddles('#calendar-clickable-headers', '[data-vc-week-number]').should('deep.equal', rows);
    });
  });
});

```

### `cypress/support/commands.ts`

```ts
/// <reference types="@testing-library/cypress" />
/// <reference types="cypress" />
// ***********************************************
// This example commands.ts shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })
//
// declare global {
//   namespace Cypress {
//     interface Chainable {
//       login(email: string, password: string): Chainable<void>
//       drag(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       dismiss(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       visit(originalFn: CommandOriginalFn, url: string, options: Partial<VisitOptions>): Chainable<Element>
//     }
//   }
// }

```

### `cypress/support/e2e.ts`

```ts
import '@testing-library/cypress/add-commands';
import 'cypress-axe';
// ***********************************************************
// This example support/e2e.ts is processed and
// loaded automatically before your test files.
//
// This is a great place to put global configuration and
// behavior that modifies Cypress.
//
// You can change the location of this file or turn off
// automatically serving support files with the
// 'supportFile' configuration option.
//
// You can read more here:
// https://on.cypress.io/configuration
// ***********************************************************
// Import commands.js using ES2015 syntax:
import './commands';

// Alternatively you can use CommonJS syntax:
// require('./commands')

```

### `demo/index.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .skip-link {
    @apply fixed left-4 top-4 z-50 -translate-y-16 rounded bg-slate-900 px-4 py-2 text-sm font-semibold text-white transition-transform focus:translate-y-0 dark:bg-white dark:text-slate-900;
  }

  #calendar {
    @apply shadow-[0_5px_40px_5px_rgb(65_65_65_/_0.1)] dark:shadow-[inset_0_0_0_1px_rgb(255_255_255_/_0.1)];
  }

  .popup-btn-orange {
    background-color: rgb(251 146 60) !important;
    color: white !important;
  }

  .popup-btn-red {
    background-color: rgb(239 68 68) !important;
    color: white !important;
  }
}

.input {
  @apply bg-white py-2 px-3 rounded text-sm text-slate-900 w-64 border-gray-200 outline-none h-9 text-left inline-block;
}

.bg-orange {
  @apply !bg-orange-500 !text-white;
}

.bg-red {
  @apply !bg-red-500 !text-white;
}

.text-bold {
  @apply !font-bold;
}

```

### `demo/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="./favicon.svg" />
    <link rel="stylesheet" href="./index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        A universal JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript framework and library.
      </p>
      <div id="calendar"></div>
    </main>
  </body>
</html>

```

### `demo/main.ts`

```ts
import { Calendar } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  const today = new Date();
  const selectedTime = today.toLocaleString('en-US', { hour12: true, minute: '2-digit', hour: '2-digit' });

  const calendar = new Calendar('#calendar', {
    selectedMonth: 3,
    selectedYear: 2023,
    selectionTimeMode: 12,
    selectedTime,
    // displayDateMin: '2022-11-23',
    // displayDateMax: '2025-11-23',
    // displayDisabledDates: true,
  });
  calendar.init();
});

```

### `demo/pages/a11y/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        Every option combination that carries its own ARIA markup, gathered on one page for the accessibility checks.
      </p>
      <div class="flex flex-col items-center gap-12">
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>type: 'month'</code> &mdash; a picker as the opening view</figcaption>
          <div id="calendar-month"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>type: 'year'</code> &mdash; a picker as the opening view</figcaption>
          <div id="calendar-year"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>onClickWeekDay</code> and <code>onClickWeekNumber</code> &mdash; clickable headers</figcaption>
          <div id="calendar-clickable-headers"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>selectionDatesMode: 'multiple-ranged'</code> with a range tooltip</figcaption>
          <div id="calendar-ranged"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>timeControls: 'range'</code> &mdash; sliders, with the inputs disabled</figcaption>
          <div id="calendar-time-range"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>type: 'multiple'</code> with <code>enableWeekNumbers</code></figcaption>
          <div id="calendar-multiple-week-numbers"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">
            <code>selectionMonthsMode</code> and <code>selectionYearsMode</code> off &mdash; locked titles
          </figcaption>
          <div id="calendar-locked-titles"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>popups</code> &mdash; a date carrying extra content</figcaption>
          <div id="calendar-popups"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>inputMode</code> &mdash; the popup, open and closed</figcaption>
          <label class="text-sm dark:text-slate-400" for="calendar-input">Pick a date</label>
          <input id="calendar-input" class="input" type="text" readonly />
        </figure>
      </div>
    </main>
  </body>
</html>

```

### `demo/pages/a11y/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

const base: Options = { selectedMonth: 3, selectedYear: 2023 };

document.addEventListener('DOMContentLoaded', () => {
  new Calendar('#calendar-month', { ...base, type: 'month' }).init();

  new Calendar('#calendar-year', { ...base, type: 'year' }).init();

  new Calendar('#calendar-clickable-headers', {
    ...base,
    enableWeekNumbers: true,
    onClickWeekDay: () => {},
    onClickWeekNumber: () => {},
  }).init();

  new Calendar('#calendar-ranged', {
    ...base,
    selectionDatesMode: 'multiple-ranged',
    selectedDates: ['2023-04-10:2023-04-18'],
    onCreateDateRangeTooltip: () => 'Selected range',
  }).init();

  new Calendar('#calendar-time-range', { ...base, selectionTimeMode: 24, timeControls: 'range', selectedTime: '10:30' }).init();

  new Calendar('#calendar-multiple-week-numbers', { ...base, type: 'multiple', enableWeekNumbers: true, displayMonthsCount: 2 }).init();

  new Calendar('#calendar-locked-titles', { ...base, selectionMonthsMode: false, selectionYearsMode: false }).init();

  new Calendar('#calendar-popups', { ...base, popups: { '2023-04-12': { modifier: '', html: '<b>Meeting</b> at noon' } } }).init();

  new Calendar('#calendar-input', { ...base, inputMode: true }).init();
});

```

### `demo/pages/animation/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        A universal JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript framework and library.
      </p>
      <div class="flex flex-col items-center gap-12">
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>animation: true</code> &mdash; defaults</figcaption>
          <div id="calendar-animated"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">no <code>animation</code> &mdash; control</figcaption>
          <div id="calendar-static"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>type: 'multiple'</code> &mdash; one timing shared by both groups</figcaption>
          <div id="calendar-multiple"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">custom timings &mdash; overshooting slide, calm cross-fade</figcaption>
          <div id="calendar-custom"></div>
        </figure>
      </div>
    </main>
  </body>
</html>

```

### `demo/pages/animation/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  const configAnimated: Options = {
    animation: true,
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configStatic: Options = {
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configMultiple: Options = {
    type: 'multiple',
    animation: { duration: 300 },
    displayMonthsCount: 2,
    selectedMonth: 3,
    selectedYear: 2023,
  };

  // The slide overshoots past one: the month winds up, shoots past its place and settles back.
  const configCustom: Options = {
    animation: {
      slide: { duration: 700, easing: 'cubic-bezier(0.68, -0.55, 0.27, 1.55)' },
      fade: { duration: 450, easing: 'ease-in-out' },
    },
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const calendarAnimated = new Calendar('#calendar-animated', configAnimated);
  calendarAnimated.init();

  const calendarStatic = new Calendar('#calendar-static', configStatic);
  calendarStatic.init();

  const calendarMultiple = new Calendar('#calendar-multiple', configMultiple);
  calendarMultiple.init();

  const calendarCustom = new Calendar('#calendar-custom', configCustom);
  calendarCustom.init();
});

```

### `demo/pages/disable-dates-gaps/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        Issue #407 repro. Clicking 2022-01-29 should NOT select past the gap (2022-01-16 to 2022-01-23 are disabled).
      </p>
      <div id="calendar"></div>
    </main>
  </body>
</html>

```

### `demo/pages/disable-dates-gaps/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  // reproduction from https://github.com/uvarov-frontend/vanilla-calendar-pro/issues/407
  const options: Options = {
    selectionDatesMode: 'multiple-ranged',
    disableAllDates: true,
    enableDates: ['2022-01-10:2022-01-15', '2022-01-24:2022-01-29'],
    selectedDates: ['2022-01-12'],
    selectedMonth: 0,
    disableDatesGaps: true,
    selectedYear: 2022,
  };

  const calendar = new Calendar('#calendar', options);
  calendar.init();
});

```

### `demo/pages/gestures/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        A universal JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript framework and library.
      </p>
      <div class="flex flex-col items-center gap-12">
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>enableCollapse</code> and <code>enableSwipe</code> &mdash; both gestures</figcaption>
          <div id="calendar-gestures"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>enableCollapse</code> &mdash; starting collapsed</figcaption>
          <div id="calendar-collapsed"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>enableSwipe</code> with <code>type: 'multiple'</code></figcaption>
          <div id="calendar-multiple"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">
            <code>enableSwipe</code> with <code>dateMax</code> &mdash; cannot be dragged past the bound
          </figcaption>
          <div id="calendar-bounded"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">both gestures, no <code>animation</code></figcaption>
          <div id="calendar-plain"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>enableCollapse</code> on its own</figcaption>
          <div id="calendar-collapse-only"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>enableSwipe</code> with ranged selection</figcaption>
          <div id="calendar-range"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">no gestures &mdash; control</figcaption>
          <div id="calendar-static"></div>
          <button id="btn-enable-gestures" type="button" class="rounded-lg border border-slate-500 px-3 py-1 text-sm">Enable gestures dynamically</button>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">both gestures in <code>inputMode</code></figcaption>
          <input id="calendar-input-gestures" class="input" type="text" aria-label="Pick a date" readonly />
        </figure>
        <div class="flex flex-col items-center gap-3">
          <button id="btn-invalid-collapse" type="button" class="rounded-lg border border-slate-500 px-3 py-1 text-sm">
            init enableCollapse with type: 'multiple'
          </button>
          <pre id="log" class="text-xs dark:text-slate-400"></pre>
          <div id="calendar-invalid"></div>
        </div>
      </div>
    </main>
  </body>
</html>

```

### `demo/pages/gestures/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  const configGestures: Options = {
    animation: true,
    enableCollapse: true,
    enableSwipe: true,
    selectedDates: ['2023-04-19'],
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configCollapsed: Options = {
    type: 'week',
    animation: true,
    enableCollapse: true,
    enableSwipe: true,
    selectedDates: ['2023-04-19'],
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configBounded: Options = {
    animation: true,
    enableCollapse: true,
    enableSwipe: true,
    dateMax: '2023-04-30',
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configMultiple: Options = {
    type: 'multiple',
    animation: true,
    enableSwipe: true,
    displayMonthsCount: 2,
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configPlain: Options = {
    enableCollapse: true,
    enableSwipe: true,
    selectedDates: ['2023-04-19'],
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configCollapseOnly: Options = {
    animation: true,
    enableCollapse: true,
    selectedDates: ['2023-04-19'],
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configRange: Options = {
    animation: true,
    enableSwipe: true,
    selectionDatesMode: 'multiple-ranged',
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configStatic: Options = {
    animation: true,
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configInput: Options = {
    inputMode: true,
    animation: true,
    enableCollapse: true,
    enableSwipe: true,
    selectedDates: ['2023-04-19'],
    selectedMonth: 3,
    selectedYear: 2023,
    onInit(self) {
      self.context.mainElement.id = 'calendar-input-popup';
    },
  };

  const calendarGestures = new Calendar('#calendar-gestures', configGestures);
  calendarGestures.init();

  const calendarCollapsed = new Calendar('#calendar-collapsed', configCollapsed);
  calendarCollapsed.init();

  const calendarMultiple = new Calendar('#calendar-multiple', configMultiple);
  calendarMultiple.init();

  const calendarBounded = new Calendar('#calendar-bounded', configBounded);
  calendarBounded.init();

  const calendarPlain = new Calendar('#calendar-plain', configPlain);
  calendarPlain.init();

  const calendarCollapseOnly = new Calendar('#calendar-collapse-only', configCollapseOnly);
  calendarCollapseOnly.init();

  const calendarRange = new Calendar('#calendar-range', configRange);
  calendarRange.init();

  const calendarStatic = new Calendar('#calendar-static', configStatic);
  calendarStatic.init();

  const calendarInput = new Calendar('#calendar-input-gestures', configInput);
  calendarInput.init();

  document.getElementById('btn-enable-gestures')?.addEventListener('click', () => {
    calendarStatic.set({ enableCollapse: true, enableSwipe: true });
  });

  const logEl = document.getElementById('log') as HTMLPreElement;
  document.getElementById('btn-invalid-collapse')?.addEventListener('click', () => {
    try {
      new Calendar('#calendar-invalid', { type: 'multiple', displayMonthsCount: 2, enableCollapse: true }).init();
      logEl.textContent = 'init() OK';
    } catch (e) {
      logEl.textContent = `init() threw: ${(e as Error).message}`;
    }
  });
});

```

### `demo/pages/input/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        A universal JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript framework and library.
      </p>
      <button id="set-date" type="button" class="mb-7 w-64 border-gray-200 border-2">Dynamically Set Date</button>
      <div class="flex flex-col items-center gap-7">
        <div>
          <label for="calendar-input">Datepicker tag 'input'</label>
          <input id="calendar-input" class="input" name="calendar" type="text" readonly />
        </div>
        <div>
          <div>Datepicker tag 'div'</div>
          <div id="calendar-div" class="input"></div>
        </div>
      </div>
    </main>
  </body>
</html>

```

### `demo/pages/input/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

const configInput: Options = {
  inputMode: true,
  positionToInput: 'center',
  onChangeToInput(self) {
    if (!self.context.selectedDates || !self.context.inputElement) return;
    if (self.context.selectedDates[0]) {
      self.context.inputElement.value = self.context.selectedDates[0];
    } else {
      self.context.inputElement.value = '';
    }
    self.hide();
  },
};

const configDiv: Options = {
  inputMode: true,
  positionToInput: 'auto',
  onChangeToInput(self) {
    if (!self.context.selectedDates || !self.context.inputElement) return;
    if (self.context.selectedDates[0]) {
      self.context.inputElement.innerHTML = self.context.selectedDates[0];
    } else {
      self.context.inputElement.textContent = '';
    }
    self.hide();
  },
};

document.addEventListener('DOMContentLoaded', () => {
  const calendarInput = new Calendar('#calendar-input', configInput);
  calendarInput.init();

  const calendarDiv = new Calendar('#calendar-div', configDiv);
  calendarDiv.set({
    popups: {
      '2024-08-28': {
        modifier: 'bg-red',
        html: 'Meeting at 9:00 PM',
      },
      '2024-08-05': {
        modifier: 'bg-red text-bold',
        html: 'Meeting at 6:00 PM with a friend',
      },
      '2024-08-11': {
        modifier: 'bg-red text-bold',
        html: 'Diner at 8:00 PM with a friend',
      },
      '2024-08-19': {
        modifier: 'bg-orange',
        html: `<div>
          <u><b>12:00 PM</b></u>
          <p style="margin: 5px 0 0;">Airplane in Las Vegas</p>
        </div>`,
      },
      '2024-08-04': {
        modifier: 'bg-orange',
        html: `<div>
          <u><b>12:00 PM</b></u>
          <p style="margin: 5px 0 0;">Lunch with John for initial meeting</p>
        </div>`,
      },
    },
  });
  calendarDiv.init();

  document.querySelector('#set-date')?.addEventListener('click', () => {
    calendarInput.set({
      selectedDates: ['2023-04-07'],
      selectedMonth: 3,
      selectedYear: 2023,
    });
    calendarInput.context.inputElement!.value = '2023-04-07';
  });
});

```

### `demo/pages/lang/index.html`

```html
<!doctype html>
<html lang="ru">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — Выбор даты и времени</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        Средство выбора даты и времени на чистом JavaScript с использованием TypeScript, поддерживает любую структуру и библиотеку JS.
      </p>
      <button type="button" id="set-options" class="mb-7 w-64 border-gray-200 border-2">Установить настройки</button>
      <div id="calendar"></div>
    </main>
  </body>
</html>

```

### `demo/pages/lang/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

const options: Options = {
  type: 'multiple',
  selectionDatesMode: 'multiple-ranged',
  disableDatesGaps: true,
  disableDatesPast: true,
  dateMin: '2021-02-01',
  dateMax: '2025-11-30',
  displayDatesOutside: false,
  selectionTimeMode: 12,
  selectedMonth: 9,
  selectedYear: 2025,
  timeMinHour: 2,
  timeMaxHour: 20,
  timeMinMinute: 10,
  timeMaxMinute: 20,
  locale: 'ru',
  disableWeekdays: [],
  disableDates: [
    '2024-06-01',
    '2024-06-02',
    '2024-06-05',
    '2024-06-06',
    '2024-06-07',
    '2024-06-10',
    '2024-06-14',
    '2024-06-15',
    '2024-06-16',
    '2024-06-20',
    '2024-06-21',
    '2024-06-22',
    '2024-06-23',
    '2024-06-28',
    '2024-06-29',
    '2024-06-30',
  ],
  labels: {
    application: 'Календарь',
    navigation: 'Навигация календаря',
    arrowNext: {
      month: 'Следующий месяц',
      year: 'Следующий список лет',
    },
    arrowPrev: {
      month: 'Предыдущий месяц',
      year: 'Предыдущий список лет',
    },
    month: 'Выбор месяца, текущий выбранный месяц:',
    months: 'Список месяцев',
    year: 'Выбор года, текущий выбранный год:',
    years: 'Список лет',
    week: 'Дни недели',
    weekNumber: 'Номера недель в году',
    dates: 'Даты текущего месяца',
    selectingTime: 'Выбора времени',
    inputHour: 'Часы',
    inputMinute: 'Минуты',
    rangeHour: 'Ползунок для выбора часов',
    rangeMinute: 'Ползунок для выбора минут',
    btnKeeping: 'Переключить AM/PM, текущее положение:',
  },
};

document.addEventListener('DOMContentLoaded', () => {
  const calendar = new Calendar('#calendar');
  calendar.init();

  const btnSetEl = document.querySelector('#set-options');
  btnSetEl?.addEventListener('click', () => {
    calendar.set(options, { dates: false });
  });
});

```

### `demo/pages/lifecycle/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        Calling init() or destroy() more than once on the same instance should throw, not corrupt the DOM.
      </p>
      <div id="calendar"></div>
      <div class="flex gap-2 mt-6">
        <button id="btn-init" type="button" class="input">Init</button>
        <button id="btn-destroy" type="button" class="input">Destroy</button>
      </div>
      <pre id="log" class="mt-6 text-left text-sm"></pre>
    </main>
  </body>
</html>

```

### `demo/pages/lifecycle/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  let calendar: Calendar | undefined;
  const logEl = document.getElementById('log') as HTMLPreElement;

  const log = (message: string) => {
    logEl.textContent += `${message}\n`;
    logEl.dataset.vcLastMessage = message;
  };

  const options: Options = {};

  document.getElementById('btn-init')?.addEventListener('click', () => {
    if (!calendar) calendar = new Calendar('#calendar', options);
    try {
      calendar.init();
      log('init() OK');
    } catch (e) {
      log(`init() threw: ${(e as Error).message}`);
    }
  });

  document.getElementById('btn-destroy')?.addEventListener('click', () => {
    if (!calendar) {
      log('destroy() skipped: no instance yet');
      return;
    }
    try {
      calendar.destroy();
      log('destroy() OK');
    } catch (e) {
      log(`destroy() threw: ${(e as Error).message}`);
    }
  });
});

```

### `demo/pages/multiple/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        A universal JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript framework and library.
      </p>
      <div id="calendar"></div>
    </main>
  </body>
</html>

```

### `demo/pages/multiple/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

const config: Options = {
  type: 'multiple',
  selectionDatesMode: 'multiple-ranged',
  selectedMonth: 3,
  selectedYear: 2023,
  onCreateDateRangeTooltip(self) {
    const createRow = (title: string, value: string) =>
      `<div style="text-align: left; white-space: nowrap">
        <span>${title}</span>
        <b>${value}</b>
      </div>`;

    return `
      ${createRow('Start:', self.context.selectedDates[0])}
      ${self.context.selectedDates[1] ? createRow('End:', self.context.selectedDates[1]) : ''}
    `;
  },
};

document.addEventListener('DOMContentLoaded', () => {
  const calendar = new Calendar('#calendar', config);
  calendar.init();
});

```

### `demo/pages/popups-range/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        Issue #406 repro: popups with a "start:end" range key should apply the same popup to every day in the range.
      </p>
      <div id="calendar"></div>
    </main>
  </body>
</html>

```

### `demo/pages/popups-range/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  // reproduction from https://github.com/uvarov-frontend/vanilla-calendar-pro/issues/406
  const options: Options = {
    selectedMonth: 1,
    selectedYear: 2026,
    popups: {
      '2026-02-10:2026-02-17': {
        modifier: 'bg-orange',
        html: "Fred's vacation",
      },
    },
  };

  const calendar = new Calendar('#calendar', options);
  calendar.init();
});

```

### `demo/pages/shadow-dom/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        Issue #381 repro: calendar instances fully encapsulated inside separate Shadow DOM web components.
      </p>
      <div class="flex gap-10 items-start">
        <shadow-calendar-input id="widget-1"></shadow-calendar-input>
        <shadow-calendar-input id="widget-2"></shadow-calendar-input>
        <shadow-calendar-plain id="widget-3"></shadow-calendar-plain>
      </div>
      <div class="mt-12 flex items-start gap-10">
        <shadow-calendar-gestures-input id="widget-4"></shadow-calendar-gestures-input>
        <shadow-calendar-gestures-plain id="widget-5"></shadow-calendar-gestures-plain>
      </div>
      <button id="light-dom-outside" type="button" class="mt-24">Outside click target (light DOM)</button>
    </main>
  </body>
</html>

```

### `demo/pages/shadow-dom/main.ts`

```ts
import { Calendar, type Options } from '@src/index';
import calendarStyles from '@src/styles/index.css?inline';

class ShadowCalendarInput extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    const style = document.createElement('style');
    style.textContent = `${calendarStyles} input { padding: 8px; font-size: 14px; }`;
    shadow.appendChild(style);

    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <label>
        <div>Calendar inside Shadow DOM (${this.id})</div>
        <input type="text" readonly data-vc-shadow-input />
      </label>
      <button type="button" data-vc-shadow-init>Init</button>
      <button type="button" data-vc-shadow-destroy>Destroy</button>
    `;
    shadow.appendChild(wrapper);

    const initCalendar = () => {
      if (this.calendar) return; // init() is one-shot per instance - build a fresh instance instead of reusing a destroyed one

      // re-query rather than reuse a closed-over reference: destroy() replaces the input with
      // a clone, so a stale reference from a previous init() would point at a detached node
      const inputEl = shadow.querySelector('[data-vc-shadow-input]') as HTMLInputElement;

      const options: Options = {
        inputMode: true,
        positionToInput: 'auto',
        selectedTheme: 'system',
        onChangeToInput: (self) => {
          inputEl.value = self.context.selectedDates[0] ?? '';
        },
      };

      this.calendar = new Calendar(inputEl, options);
      this.calendar.init();
    };

    initCalendar();

    shadow.querySelector('[data-vc-shadow-init]')?.addEventListener('click', initCalendar);
    shadow.querySelector('[data-vc-shadow-destroy]')?.addEventListener('click', () => {
      this.calendar?.destroy();
      this.calendar = undefined;
    });
  }

  disconnectedCallback() {
    this.calendar?.destroy();
  }
}

customElements.define('shadow-calendar-input', ShadowCalendarInput);

// a plain (non-inputMode) calendar rendered directly into the shadow root: it never creates a
// popup, so none of the root-awareness fixes above are even exercised - included to demonstrate
// that this case already worked with zero changes.
class ShadowCalendarPlain extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    const style = document.createElement('style');
    style.textContent = calendarStyles;
    shadow.appendChild(style);

    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div>Plain calendar inside Shadow DOM (${this.id})</div>
      <div data-vc-shadow-plain></div>
    `;
    shadow.appendChild(wrapper);

    const targetEl = shadow.querySelector('[data-vc-shadow-plain]') as HTMLElement;
    const options: Options = { selectedTheme: 'system' };

    this.calendar = new Calendar(targetEl, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    this.calendar?.destroy();
  }
}

customElements.define('shadow-calendar-plain', ShadowCalendarPlain);

// Gestures inside a shadow root: the pointer listeners live on the calendar element, but the
// move/up pair is bound to window, so both have to survive crossing the shadow boundary.
const gestureOptions: Options = {
  animation: true,
  enableCollapse: true,
  enableSwipe: true,
  selectedTheme: 'system',
  selectedDates: ['2023-04-19'],
  selectedMonth: 3,
  selectedYear: 2023,
};

class ShadowCalendarGesturesInput extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    const style = document.createElement('style');
    style.textContent = `${calendarStyles} input { padding: 8px; font-size: 14px; }`;
    shadow.appendChild(style);

    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div>Shadow DOM + inputMode + gestures (${this.id})</div>
      <input type="text" readonly aria-label="Pick a date" data-vc-shadow-input>
    `;
    shadow.appendChild(wrapper);

    const inputEl = shadow.querySelector('[data-vc-shadow-input]') as HTMLInputElement;

    this.calendar = new Calendar(inputEl, {
      ...gestureOptions,
      inputMode: true,
      positionToInput: 'auto',
      onChangeToInput: (self) => {
        inputEl.value = self.context.selectedDates[0] ?? '';
      },
    });
    this.calendar.init();
  }

  disconnectedCallback() {
    this.calendar?.destroy();
  }
}

customElements.define('shadow-calendar-gestures-input', ShadowCalendarGesturesInput);

class ShadowCalendarGesturesPlain extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    const style = document.createElement('style');
    style.textContent = calendarStyles;
    shadow.appendChild(style);

    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div>Shadow DOM + gestures (${this.id})</div>
      <div data-vc-shadow-plain></div>
    `;
    shadow.appendChild(wrapper);

    this.calendar = new Calendar(shadow.querySelector('[data-vc-shadow-plain]') as HTMLElement, gestureOptions);
    this.calendar.init();
  }

  disconnectedCallback() {
    this.calendar?.destroy();
  }
}

customElements.define('shadow-calendar-gestures-plain', ShadowCalendarGesturesPlain);

```

### `demo/pages/week-numbers/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        A universal JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript framework and library.
      </p>
      <div class="flex flex-col items-center gap-10">
        <div id="calendar-2026"></div>
        <div id="calendar-2025"></div>
        <div id="calendar-sunday-start"></div>
      </div>
    </main>
  </body>
</html>

```

### `demo/pages/week-numbers/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  // 2026 has 53 ISO weeks (Dec 28-30, 2026 fall in week 53)
  const config2026: Options = {
    selectedMonth: 11,
    selectedYear: 2026,
    enableWeekNumbers: true,
  };

  // December 2025's last week rolls over into week 1 of 2026 (year-boundary case, control for #402)
  const config2025: Options = {
    selectedMonth: 11,
    selectedYear: 2025,
    enableWeekNumbers: true,
  };

  // firstWeekday other than Monday (ISO 8601 has no official rule here) - checks the library's
  // generalized week numbering stays self-consistent (sequential, no gaps/duplicates)
  const configSundayStart: Options = {
    selectedMonth: 5,
    selectedYear: 2028,
    firstWeekday: 0,
    enableWeekNumbers: true,
  };

  const calendar2026 = new Calendar('#calendar-2026', config2026);
  calendar2026.init();

  const calendar2025 = new Calendar('#calendar-2025', config2025);
  calendar2025.init();

  const calendarSundayStart = new Calendar('#calendar-sunday-start', configSundayStart);
  calendarSundayStart.init();
});

```

### `demo/pages/week/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="initial-scale=1,width=device-width" />
    <meta name="format-detection" content="telephone=no" />
    <title>Vanilla Calendar Pro — JavaScript Date &amp; Time Picker</title>
    <link rel="icon" type="image/svg+xml" href="../../favicon.svg" />
    <link rel="stylesheet" href="../../index.css" />
    <script defer src="./main.ts" type="module"></script>
  </head>
  <body
    class="font-sans bg-white bg-light-mode text-slate-900 min-h-screen container mx-auto text-center flex flex-col items-center py-12 dark:bg-slate-900 dark:bg-dark-mode dark:text-white"
  >
    <a class="skip-link" href="#main-content">Skip to main content</a>
    <main id="main-content" class="flex w-full flex-col items-center">
      <h1 class="block mb-7 text-6xl font-extrabold">Vanilla Calendar Pro</h1>
      <p class="block max-w-[700px] text-lg mb-12 dark:text-slate-400">
        A universal JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript framework and library.
      </p>
      <div class="flex flex-col items-center gap-12">
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>type: 'week'</code> &mdash; a standalone week strip</figcaption>
          <div id="calendar-week"></div>
          <button id="btn-sunday-first" type="button" class="rounded-lg border border-slate-500 px-3 py-1 text-sm">Set Sunday as the first weekday</button>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>type: 'week'</code> &mdash; with week numbers and a selected date</figcaption>
          <div id="calendar-week-numbers"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400">a month, for comparison</figcaption>
          <div id="calendar-month"></div>
        </figure>
        <figure class="flex flex-col items-center gap-3">
          <figcaption class="text-sm dark:text-slate-400"><code>type: 'week'</code> &mdash; year switching disabled</figcaption>
          <div id="calendar-week-year-locked"></div>
        </figure>
      </div>
    </main>
  </body>
</html>

```

### `demo/pages/week/main.ts`

```ts
import { Calendar, type Options } from '@src/index';

import '@src/styles/index.css';

document.addEventListener('DOMContentLoaded', () => {
  const configWeek: Options = {
    type: 'week',
    animation: true,
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configWeekNumbers: Options = {
    type: 'week',
    animation: true,
    enableWeekNumbers: true,
    selectedDates: ['2023-04-19'],
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configMonth: Options = {
    animation: true,
    selectedMonth: 3,
    selectedYear: 2023,
  };

  const configWeekYearLocked: Options = {
    type: 'week',
    selectionYearsMode: false,
    selectedDates: ['2023-12-29'],
    selectedMonth: 11,
    selectedYear: 2023,
  };

  const calendarWeek = new Calendar('#calendar-week', configWeek);
  calendarWeek.init();

  const calendarWeekNumbers = new Calendar('#calendar-week-numbers', configWeekNumbers);
  calendarWeekNumbers.init();

  const calendarMonth = new Calendar('#calendar-month', configMonth);
  calendarMonth.init();

  const calendarWeekYearLocked = new Calendar('#calendar-week-year-locked', configWeekYearLocked);
  calendarWeekYearLocked.init();

  document.getElementById('btn-sunday-first')?.addEventListener('click', () => {
    calendarWeek.set({ firstWeekday: 0 });
  });
});

```

### `docs/en/learn.mdx`

```mdx
---
title: Introduction
description: Page Description
---

# Introduction to Vanilla Calendar Pro

**Vanilla Calendar Pro** is a powerful, flexible, and lightweight tool for handling dates and times, created for developers who need a functional and easily customizable calendar for web applications or websites. It is independent of external libraries and highly performant, making it an excellent choice for integrating into any projects that require a calendar.

This calendar is designed for developers working on a wide variety of projects, whether personal sites, corporate portals, or complex web applications. Vanilla Calendar Pro is perfect for those looking for a simple date display solution and those needing more advanced features like time selection and interactive actions.

## Key Features

Vanilla Calendar Pro offers a rich set of features that allow the creation of convenient and adaptive calendar widgets.

Key features include:

- **Lightweight**: The final JavaScript file is minified and optimized for fast loading.
- **Dependency-Free**: Completely standalone, with no need for additional libraries.
- **Easy Localization**: Supports easy localization for any language.
- **Customizable**: Easily configurable through CSS and HTML markup.
- **Multiple Instances**: Allows unlimited calendars on a single page.
- **Theme Support**: Automatically switches between light and dark themes and supports custom themes.
- **Week Start Customization**: Enables choosing any day of the week as the starting day.
- **Weekend Customization**: Allows setting custom weekends for each week.
- **Week Number Display**: Can display week numbers throughout the year.
- **Not Tied to `<input>`**: Unlike many calendars, it is not limited to use with the `<input>` element.
- **Accessibility**: Includes ARIA labels, `tabindex`, and full keyboard navigation, enhancing accessibility.
- **Date and Time Range Selection**: Supports selecting date and time ranges with minimum and maximum limits.
- **Pop-Ups and Tooltips**: Allows setting up pop-ups with custom information and adds tooltips for date range selections.

## Try Vanilla Calendar Pro

Below is a live example of Vanilla Calendar Pro in a JS sandbox. You can modify the parameters and instantly see how the calendar adapts to your settings.

<Sandbox example="installation-and-usage" />

<Info>**This demo example** — one of many in this section — helps you understand how to use Vanilla Calendar Pro and customize it to your needs.</Info>

In the following sections, you will find everything needed for successful integration and setup of Vanilla Calendar Pro.

```

### `docs/en/learn/additional-features-animation.mdx`

```mdx
---
title: Animation
new: true
description: Learn how to configure slide, cross-fade and collapse transitions between calendar views.
section: 6. Additional Features
---

# Animation

Transitions between views can be animated. Arrow navigation and swiping slide horizontally, the month and year pickers cross-fade, and collapsing animates the calendar between its month and week heights.

<Info>
  Animation is off by default for backwards compatibility: the option was added later, and slide and cross-fade transitions temporarily change what a DOM query
  sees.
</Info>

<Sandbox example="additional-features-animation" height={400} />

## One Timing for Everything

Passing an object instead of `true` overrides the timing. Values at the top level reach every transition.

<Sandbox example="additional-features-animation-shared" height={400} />

## Separate Timings

The three groups can be tuned independently. Nest values under `slide` for arrows and swiping, `fade` for pickers, or `collapse` for folding between the month and week. Nested values win over the ones at the top level.

The example below gives the slide an overshooting curve, while the pickers and collapse control use their own calmer timings.

<Sandbox example="additional-features-animation-custom" height={400} />

<Info>
  Animated settling is skipped when the visitor asks for reduced motion through `prefers-reduced-motion: reduce`. Gestures still follow the pointer and settle
  immediately on release.
</Info>

## Querying the Calendar While It Animates

During slide and cross-fade transitions, the outgoing content stays in the DOM inside an `inert` `[data-vc-ghost]` layer, so date elements can momentarily be present twice. Callbacks such as `onClickArrow` and `onClickDate` fire inside that window, so exclude the layer if you inspect the calendar from them. Collapsing does not create a ghost layer.

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/en/learn/additional-features-collapse.mdx`

```mdx
---
title: Collapse
new: true
description: Learn how to let visitors fold a month down to a single week and expand it again.
section: 6. Additional Features
---

# Collapse

`enableCollapse` adds a control under the grid. Clicking it folds the month down to one week, and clicking it again unfolds it. The option is off by default and does not require `enableSwipe` or `animation`.

<Sandbox example="additional-features-collapse" height={420} />

The control adapts to the device. On a mouse it is a chevron; on a touch screen it becomes a grabber that can be dragged up and down, and the calendar follows the finger the whole way. A slow drag has to cover a quarter of the travel, while a quick flick can commit sooner because release velocity is also taken into account. Otherwise the calendar springs back.

The target week is chosen from the first selected date when it belongs to the displayed month. Otherwise the calendar uses today when it belongs to that month, or the first day of the displayed month as the final fallback.

While collapsed the arrows step one week at a time. Expanding again returns to the month around that same week.

<Info>Collapsing switches `type` to `'week'`, so `calendar.type` tells you the current state and `set({ type: 'week' })` does the same thing without the transition. Only the `default` and `week` types accept this option; pairing it with `multiple` throws on `init()`.</Info>

## Timing

The transition uses the [`animation`](/docs/reference/settings) option. Its timing can be configured independently through the `collapse` group:

```ts
new Calendar('#calendar', {
  animation: { collapse: { duration: 450 } },
  enableCollapse: true,
});
```

<Info>
  Without `animation`, or when the visitor asks for reduced motion through `prefers-reduced-motion: reduce`, dragging still tracks the finger but the release
  settles instantly.
</Info>

```

### `docs/en/learn/additional-features-layouts.mdx`

```mdx
---
title: Layouts
description: Layouts allow you to customize the HTML markup of the calendar, adding your own elements such as buttons. Learn how to customize the calendar header and add elements for different types of calendars.
section: 6. Additional Features
---

# Layouts

The calendar provides a convenient way to customize the HTML markup using the `layouts` parameter. This allows you to add your own elements, such as buttons or any other HTML element, to the calendar.

`layouts` takes the `type` of the calendar as the key and a string as the value.

In the following example, the calendar header is customized for `type: 'default'`, and a regular button is added inside the calendar.

<Sandbox example="additional-features-layouts" />

Now, let's use the `inputMode: true` parameter. We will add a button that will hide the calendar when clicked.

<Sandbox example="additional-features-layouts-btn-close" input={true} />

```

### `docs/en/learn/additional-features-popups-and-tooltip.mdx`

```mdx
---
title: Popups and Tooltips
description: Learn how to add popups with information for any day in the calendar and use tooltips for selecting date ranges.
section: 6. Additional Features
---

# Popups and Tooltips

## Popups

The calendar allows you to add popups with information for any day, which will be displayed when hovering over that day.

In the provided example, a specific day is highlighted using a CSS modifier, and information is added to the popup.

Additional details about popups can be found in the reference guide.

<Sandbox example="additional-features-popups" />

## Tooltips

Tooltips can be used when the `selectionDatesMode` parameter is set to `'multiple-ranged'`. Using `onCreateDateRangeTooltip`, you can create a fully customized tooltip.

<Sandbox example="additional-features-tooltips" />

```

### `docs/en/learn/additional-features-styles.mdx`

```mdx
---
title: Styles
description: Customize the styles of the calendar by replacing the CSS classes with your own. Learn how to customize the appearance of the calendar.
section: 6. Additional Features
---

# Styles

All CSS classes used in the calendar are variables that can be customized by replacing them with your own values.

<Info>When replacing CSS classes with your own, keep in mind that you will need to create and style this class in your own CSS.</Info>

Below is an example of replacing the class for the arrows with your own. A full list of classes can be found in the reference guide.

<Sandbox example="additional-features-styles" />

## CSS Variables

If you only need to change colors, you don't need to replace any classes at all — every color in the built-in themes is exposed as a CSS custom property, with the theme's original color as the fallback:

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

Nothing changes unless you explicitly set a variable. The full list of variables is available in the [reference guide](/docs/reference/styles).

```

### `docs/en/learn/additional-features-swipe.mdx`

```mdx
---
title: Swipe
new: true
description: Learn how to let visitors drag the calendar sideways to reach the next or previous period.
section: 6. Additional Features
---

# Swipe

`enableSwipe` lets the calendar content be dragged sideways. It is off by default, works independently of `enableCollapse` and `animation`, and can be enabled in every view the arrows can navigate — `default`, `multiple`, `week` and the year list. The gesture moves by whatever the arrows move by in the current view.

<Sandbox example="additional-features-swipe" height={420} />

The neighbouring period is rendered as soon as the gesture starts and travels with the pointer, so the drag shows where it is going rather than an empty gap. A slow drag has to cover a quarter of the width, while a quick flick can commit sooner because release velocity is also taken into account. Otherwise the content slides back.

<Info>
  The gesture only claims the horizontal axis, so the page still scrolls vertically over the calendar. A swipe is available only while the corresponding arrow
  is visible, so it observes `dateMin`, `dateMax` and navigation restrictions. The date under the pointer on release is not selected.
</Info>

## Timing

The gesture uses the `slide` group of the [`animation`](/docs/reference/settings) option, the same timing as arrow navigation:

```ts
new Calendar('#calendar', {
  animation: { slide: { duration: 350 } },
  enableSwipe: true,
});
```

<Info>
  Without `animation`, or when the visitor asks for reduced motion through `prefers-reduced-motion: reduce`, dragging still tracks the pointer but the release
  settles instantly.
</Info>

## Querying the Calendar Mid-Gesture

A swipe leans on the same ghost layer as the arrow animation, so while it runs the outgoing period is still in the DOM inside an `inert` `[data-vc-ghost]` element and the date cells are momentarily present twice. Exclude that layer if your own code walks them.

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/en/learn/additional-features-themes.mdx`

```mdx
---
title: Themes
description: The calendar supports custom themes and by default has light and dark themes. Learn how to configure themes and use system settings or your own themes.
section: 6. Additional Features
---

# Themes

The calendar supports custom themes and by default has light and dark themes.

If the `themeAttrDetect` parameter is set to `false`, the theme will be determined by the user's system settings or the `selectedTheme` parameter.

The calendar can automatically detect and track the site's theme based on the set tag and attribute. Additional information about this parameter can be found in the reference guide.

If your site supports only one theme or you want to customize the appearance of the calendar to your liking, you can explicitly select one of the available themes.

The example below demonstrates the forced use of the dark theme:

<Sandbox example="additional-features-themes-dark" themeDetection={false} />

And here is the same example, but using the light theme:

<Sandbox example="additional-features-themes-light" themeDetection={false} />

As described above, you can use your own themes, create them yourself, or import them from the calendar if they exist.

<Sandbox example="additional-features-themes-slate-light" themeDetection={false} />

```

### `docs/en/learn/components-for-libraries-angular.mdx`

```mdx
---
title: Angular Component
description: Learn how to create and use an Angular component for Vanilla Calendar Pro. A detailed guide to creating the component and integrating it into an Angular application.
section: 7. Components for Libraries
---

# Angular Component

<Info>
  This example targets Angular 15+ (standalone components).
</Info>

To demonstrate, let's create a simple Angular component for Vanilla Calendar Pro. Create a file named `vanilla-calendar.component.ts` and copy the following code into it:

```ts
import { AfterViewInit, Component, ElementRef, Input, ViewChild } from '@angular/core';
import { Calendar, Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

@Component({
  selector: 'vanilla-calendar',
  standalone: true,
  template: `<div #calendarRef></div>`,
})
export class VanillaCalendarComponent implements AfterViewInit {
  @Input() config?: Options;
  @ViewChild('calendarRef') calendarRef!: ElementRef<HTMLDivElement>;

  ngAfterViewInit() {
    const calendar = new Calendar(this.calendarRef.nativeElement, this.config);
    calendar.init();
  }
}
```

Then import the created `VanillaCalendarComponent` into the component where you want to display the calendar.

```ts
// ...
import { VanillaCalendarComponent } from './vanilla-calendar.component';
// ...
```

Add it to the `imports` array of a standalone component and use it in the template.

```ts
@Component({
  // ...
  imports: [VanillaCalendarComponent],
  template: `
    <!-- -->
    <vanilla-calendar />
    <!-- -->
  `,
})
```

The `VanillaCalendarComponent` can accept any HTML attributes supported by the `<div>` tag (Angular forwards them to the host element automatically), as well as the `config` input for configuring the calendar.

```ts
template: `
  <!-- -->
  <vanilla-calendar [config]="{ type: 'multiple' }" class="thisIsMyClass" />
  <!-- -->
`,
```

```

### `docs/en/learn/components-for-libraries-react.mdx`

```mdx
---
title: React Component
description: Learn how to create and use a React component for Vanilla Calendar Pro. A detailed guide to creating the component and integrating it into a React application.
section: 7. Components for Libraries
---

# React Component

<Info>
  This example targets React 16.8+ (functional components with Hooks). If you are not using TypeScript, use the `.jsx` extension instead of `.tsx` and remove the `CalendarProps` interface from the component.
</Info>

For demonstration purposes, let's consider the simplest React component for Vanilla Calendar Pro. Create a file named `VanillaCalendar.tsx` and copy the following code into it:

```tsx
import { useEffect, useRef, useState } from 'react';
import { Options, Calendar } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

interface CalendarProps extends React.HTMLAttributes<HTMLDivElement> {
  config?: Options,
}

function VanillaCalendar({ config, ...attributes }: CalendarProps) {
  const ref = useRef(null);
  const [calendar, setCalendar] = useState<Calendar | null>(null);

  useEffect(() => {
    if (!ref.current) return;
    setCalendar(new Calendar(ref.current, config));
  }, [ref, config])

  useEffect(() => {
    if (!calendar) return;
    calendar.init()
  }, [calendar])

  return (
    <div {...attributes} ref={ref}></div>
  )
}

export default VanillaCalendar;
```

Then, import the created `VanillaCalendar` component into your React application where you plan to display the calendar.

```tsx
import VanillaCalendar from './VanillaCalendar';
```

Use the created component.

```tsx
// ...
<VanillaCalendar />
// ...
```

The `VanillaCalendar` component can accept any HTML attributes supported by the `<div>` tag, as well as the `config` parameter for configuring the calendar.

```tsx
// ...
<VanillaCalendar config={{
    type: 'multiple',
  }} className="thisIsMyClass" />
// ...
```

```

### `docs/en/learn/components-for-libraries-vue.mdx`

```mdx
---
title: Vue Component
description: Learn how to create and use a Vue component for Vanilla Calendar Pro. A detailed guide on creating the component and integrating it into a Vue application.
section: 7. Components for Libraries
---

# Vue Component

<Info>
  This example targets Vue 3.2+ (Composition API with `<script setup>`).
</Info>

To demonstrate, let's create a simple Vue component for Vanilla Calendar Pro. Create a file named `VanillaCalendar.vue` and copy the following code into it:

```vue
<script setup lang="ts">
import { onMounted, ref, useAttrs } from 'vue';
import { Calendar, Options } from 'vanilla-calendar-pro';
import 'vanilla-calendar-pro/styles/index.css'

const calendarRef = ref(null);
const attributes = useAttrs();
const { config } = defineProps<{ config?: Options }>();

onMounted(() => {
  if (!calendarRef.value) return;
  const calendar = new Calendar(calendarRef.value, config);
  calendar.init();
});
</script>

<template>
  <div v-bind="attributes" ref="calendarRef"></div>
</template>
```

Then import the created `VanillaCalendar` component into your Vue application where you want to display the calendar.

```vue
<script setup lang="ts">
// ...
import VanillaCalendar from './VanillaCalendar.vue';
// ...
</script>
```

Use the created component.

```vue
<template>
  <!-- -->
  <VanillaCalendar />
  <!-- -->
</template>
```

The `VanillaCalendar` component can accept any HTML attributes supported by the `<div>` tag, as well as the `config` parameter for calendar configuration.

```vue
<template>
  <!-- -->
  <VanillaCalendar :config="{ type: 'multiple' }" />
  <!-- -->
</template>
```

```

### `docs/en/learn/components-for-libraries-web-component.mdx`

```mdx
---
title: Web Component
description: Learn how to wrap Vanilla Calendar Pro in a native Web Component, with an optional Shadow DOM variant for full style and DOM encapsulation.
section: 7. Components for Libraries
---

# Web Component

<Info>
  A Web Component is a native, framework-agnostic custom HTML element. Once registered, it works the same way in any framework, or in plain HTML — no wrapper library required.
</Info>

## Plain Web Component

For demonstration purposes, let's consider the simplest native Web Component wrapping Vanilla Calendar Pro. Create a file named `VanillaCalendarElement.ts` and copy the following code into it:

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    this.calendar = new Calendar(this, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

The custom element renders the calendar directly into its own (light) DOM — no extra setup is required, and `disconnectedCallback` calls `calendar.destroy()` so the calendar cleans up after itself whenever the custom element is removed from the page.

Once registered, use the custom element anywhere in your HTML, in any framework or none at all:

```html
<vanilla-calendar-element></vanilla-calendar-element>
```

## Web Component with Shadow DOM

If you need full style and DOM encapsulation — for example, to ship the calendar inside a design-system component without its CSS leaking out or clashing with the host page — you can attach a Shadow DOM instead. Vanilla Calendar Pro fully supports being initialized inside a Shadow DOM: popups are appended to the correct root, clicks and focus are tracked relative to the shadow boundary, and the system-theme listener is scoped per instance. No special option is required.

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    // the calendar's own CSS has to be loaded inside the shadow root too, since
    // styles in the outer document don't cross the shadow boundary
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css';
    shadow.appendChild(link);

    const container = document.createElement('div');
    shadow.appendChild(container);

    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    // pass the element directly rather than a string selector: a string selector is
    // resolved with document.querySelector, which can't reach inside a Shadow DOM
    this.calendar = new Calendar(container, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

A few points worth calling out:

- The calendar's stylesheet is loaded with a `<link>` element appended directly inside the shadow root, since styles declared in the outer document do not cross the shadow boundary.
- The container is passed to `new Calendar(...)` as an element rather than as a string selector: a string selector is resolved with `document.querySelector`, which cannot reach inside a Shadow DOM.

```

### `docs/en/learn/date-management-date-min-and-max.mdx`

```mdx
---
title: Maximum and Minimum Date
description: Learn how to set a date range in the calendar using the dateMin and dateMax parameters. Configure the minimum and maximum dates to limit the allowed range.
section: 4. Managing Dates and Time
---

# Maximum and Minimum Date

The date range in the calendar can be set using the `dateMin` and `dateMax` parameters. These parameters specify the allowed range of dates in the calendar.

By default, the minimum date is `'1970-01-01'`, which corresponds to the beginning of <a href="https://en.wikipedia.org/wiki/Unix_time" rel="noopener noreferrer" target="_blank">UNIX time</a>.
The maximum date is set to `'2470-12-31'` by default and is chosen arbitrarily.

If you need to set a specific range of possible dates, replace the values of the `dateMin` and `dateMax` parameters with the dates you need. Note that the calendar will not process dates outside the specified range.

<Sandbox example="date-management-date-min-and-max" />

```

### `docs/en/learn/date-management-display-range-dates.mdx`

```mdx
---
title: Display Date Range
description: Learn how to set the range of displayed dates in the calendar using the displayDateMin and displayDateMax parameters. Configure the display and selection of dates within a specified range.
section: 4. Managing Dates and Time
---

# Display Date Range

The `displayDateMin` and `displayDateMax` parameters define the range of dates that can be displayed in the calendar but do not affect the calendar's lifecycle. They only indicate which dates are allowed to be displayed and selected.

For example, if the `displayDisabledDates` parameter is set to `true`, then the minimum and maximum years available for viewing by the user will be determined by the values of the `dateMin` and `dateMax` parameters.

<Sandbox example="date-management-display-range-dates" />

Changing the `displayDisabledDates` parameter allows you to control the dates available for viewing and selection in the calendar.

```

### `docs/en/learn/date-management-enable-or-disable-days.mdx`

```mdx
---
title: Enable or Disable Days
description: Learn how to disable or enable specific days in the calendar. Configure the availability of days for selection based on your needs.
section: 4. Managing Dates and Time
---

# Enable or Disable Days

You may need to disable certain days so that they are not available for selection.

<Sandbox example="date-management-disable-dates" />

Sometimes it may be easier to disable all days and enable specific days rather than listing the disabled days.

<Sandbox example="date-management-enable-dates" />

```

### `docs/en/learn/date-management-enable-time-picker.mdx`

```mdx
---
title: Enable Time Selection
description: Learn how to enable and configure time selection in the calendar. Supports 12-hour and 24-hour formats, setting initial time, managing time range, and step.
section: 4. Managing Dates and Time
---

# Enable Time Selection

By default, time selection is disabled, but you can easily enable it and configure it according to your needs.

## 12-Hour Day with AM/PM

You can enable the 12-hour time format and add AM/PM markers.

<Sandbox example="date-management-enable-time-picker-12" height={400} />

## 24-Hour Day

If you need a 24-hour time format without AM/PM, you can configure it as follows.

<Sandbox example="date-management-enable-time-picker-24" height={400} />

## Setting Your Own Time

You can set the initial time when initializing the calendar. For a 24-hour day, you do not need to specify the AM/PM marker.

<Sandbox example="date-management-enable-time-picker-your-time" height={400} />

## Managing Time Range

You can set the possible time range.

<Sandbox example="date-management-enable-time-picker-range" height={400} />

## Managing Time Step

In addition to everything else, you can configure the time step for minutes and hours. You can also disable the ability to manually enter time in the input field.

<Sandbox example="date-management-enable-time-picker-control" height={400} />

```

### `docs/en/learn/date-management-forbid-choice.mdx`

```mdx
---
title: Disable Day, Month, and Year Selection
description: Learn how to disable the ability to select the day, month, or year in the calendar. Configure the calendar according to your needs.
section: 4. Managing Dates and Time
---

# Disable Day, Month, and Year Selection

The calendar allows you to easily disable the ability to select the day, month, or year individually.

<Sandbox example="date-management-forbid-choice" />

```

### `docs/en/learn/date-management-other-today.mdx`

```mdx
---
title: Custom Today
description: Learn how to specify a different day as today in the calendar. Configure the calendar according to your needs.
section: 4. Managing Dates and Time
---

# Custom Today

The calendar provides the ability to specify which day should be considered today.

<Sandbox example="date-management-other-today" />

```

### `docs/en/learn/date-management-selected-days-month-year.mdx`

```mdx
---
title: Selected Days, Month, and Year on Initialization
description: Learn how to specify selected days, month, and year when initializing the calendar. Configure the calendar according to your needs.
section: 4. Managing Dates and Time
---

# Selected Days, Month, and Year on Initialization

The calendar allows you to explicitly specify selected days upon initialization, as well as the month and year that will be displayed regardless of the current date.

This is useful if you need to pre-select certain dates and set a specific month and year.

<Sandbox example="date-management-selected-days-month-year" />

```

### `docs/en/learn/handle-click-a-day.mdx`

```mdx
---
title: Handling Day Click
description: Learn how to handle clicks on days in the calendar using the onClickDate() action. Configure the handling of selecting a single day or a range of dates.
section: 5. Action Handlers
---

# Handling Day Click

For user interaction with the calendar, various actions are provided, one of which is `onClickDate()`. This action allows you to track when a user clicks on a specific day in the calendar.

Example with outputting the selected day to the console:

<Sandbox example="handle-click-a-day" />

Note that the selected day is represented as an array, as the user can select not only a single day but also a range of dates if allowed by the calendar parameters.

<Sandbox example="handle-click-a-day-ranged" />

```

### `docs/en/learn/handle-click-on-a-month-in-the-month-selection.mdx`

```mdx
---
title: Handling Month Click in Month List
description: Learn how to handle clicks on months in the month list. Get information about the selected month and its index.
section: 5. Action Handlers
---

# Handling Month Click in Month List

When a month is clicked in the list of all months, you can handle this event and get information about the selected element and its index.

<Info>It is important to note that according to JS standards, months are numbered starting from zero, where January corresponds to the zeroth month and December to the eleventh.</Info>

<Sandbox example="handle-click-on-a-month-in-the-month-selection" />

```

### `docs/en/learn/handle-click-on-the-arrows.mdx`

```mdx
---
title: Handling Arrow Clicks
description: Learn how to handle clicks on the arrows to switch the month or year in the calendar. Configure event handling according to your needs.
section: 5. Action Handlers
---

# Handling Arrow Clicks

When any of the arrows are clicked, an event occurs to switch the month or year in the calendar. This event can be used according to your needs.

<Sandbox example="handle-click-on-the-arrows" />

```

### `docs/en/learn/handle-click-on-the-year-in-the-year-selection.mdx`

```mdx
---
title: Handling Year Click in Year Selection
description: Learn how to handle clicks on the year in the year list. Get information about the selected year and its number.
section: 5. Action Handlers
---

# Handling Year Click in Year Selection

Just like selecting a month, you can select a year by clicking on the year header in the calendar.

When a year is clicked from the list, you can get information about the selected element that was clicked, as well as the year number.

<Sandbox example="handle-click-on-the-year-in-the-year-selection" />

```

### `docs/en/learn/handle-click-on-weekday-and-the-week-number.mdx`

```mdx
---
title: Handling Day of Week and Week Number Clicks
description: Learn how to handle clicks on the day of the week and the week number in the calendar. Configure event handling to select all days of the month related to the selected day of the week or to select dates in the selected week.
section: 5. Action Handlers
---

# Handling Day of Week and Week Number Clicks

## Day of the Week

You can intercept a click on a day of the week and, for example, select all days of the month that correspond to that day of the week.

<Sandbox example="handle-click-on-weekday" />

## Week Number

You can display week numbers in the calendar using the `enableWeekNumbers` parameter and handle clicks on them. Having information about the dates in the selected week, you can easily select these dates in the same way.

<Sandbox example="handle-click-on-the-week-number" />

```

### `docs/en/learn/handle-get-and-change-every-day.mdx`

```mdx
---
title: Getting and Modifying Each Day
description: Learn how to get and modify each day in the calendar. Perform various operations, add additional information, or make changes to each day.
section: 5. Action Handlers
---

# Getting and Modifying Each Day

With access to each day in the calendar, you can perform various operations, add additional information, or make changes to each day.

For example, you can add a random cost or value to each day.

<Sandbox example="handle-get-and-change-every-day" height={370} />

```

### `docs/en/learn/handle-select-and-change-of-time.mdx`

```mdx
---
title: Selecting and Changing Time
description: Learn how to activate and handle the selection and change of time in the calendar. Get data with each change of time.
section: 5. Action Handlers
---

# Selecting and Changing Time

By activating the `selectionTimeMode` parameter, you gain the ability to automatically receive the necessary data with each change of time.

<Sandbox example="handle-select-and-change-of-time" height={400} />

```

### `docs/en/learn/installation-and-usage.mdx`

```mdx
---
title: Installation and Usage
description: Learn how to install and use Vanilla Calendar Pro. Integrate the calendar through a package manager or CDN, and configure it according to your needs.
section: 1. Getting Started
---

# Installation and Usage

Vanilla Calendar Pro is easily integrated into any project. There are several installation methods, depending on how you prefer to manage dependencies and build your project.

## Installation via Package Manager

The most common way to install Vanilla Calendar Pro is by using a package manager. This method is ideal for projects using Node.js and modern build tools.

1. Install the package:

```bash
npm install vanilla-calendar-pro
# or
yarn add vanilla-calendar-pro
# or
pnpm add vanilla-calendar-pro
```

2. Create an HTML element in the body of your document with an arbitrary CSS selector:

```html
<html>
  <head>
  </head>
  <body>
    <div id="calendar"></div>
  </body>
</html>
```

<Info>For demonstration purposes in this section, we will use `#calendar` as the CSS selector, but you can create and use any other selector.</Info>

3. Import the script, create a calendar instance, and initialize it in your JavaScript or TypeScript file.

```ts
import { Calendar } from 'vanilla-calendar-pro';

const calendar = new Calendar('#calendar', {
  // Your settings
});
calendar.init();
```

4. Import the styles in the same file. The `index.css` file contains the layout grid for the calendar, as well as light and dark themes.

```ts
import 'vanilla-calendar-pro/styles/index.css';
```

You also have the option to include the layout and theme styles separately, like this:

```ts
import 'vanilla-calendar-pro/styles/layout.css'; // Only the skeleton
import 'vanilla-calendar-pro/styles/themes/light.css'; // Light theme
import 'vanilla-calendar-pro/styles/themes/dark.css'; // Dark theme
// or any other custom theme...
```

5. Full example of simple initialization without any custom settings:

<Sandbox example="installation-and-usage" />

<Info>As you may have noticed in this example, we are using a flat calendar view without using the **«Input»** field, if you are interested in how you can integrate a calendar into **«Input»**, check out [this example](/docs/learn/type-default#with-input).</Info>

## Local or CDN

If you need to quickly integrate Vanilla Calendar Pro without using build tools or package managers, you can include it via CDN or <a href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro@latest/package.zip" rel="noopener noreferrer" target="_blank">download the archive</a> with the latest version and include it locally.

```html
<html>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/index.js" defer></script>
  </head>
  <body style="display: flex; align-items: start">
    <div id="calendar"></div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        // Destructure the Calendar constructor
        const { Calendar } = window.VanillaCalendarPro;
        // Create a calendar instance and initialize it.
        const calendar = new Calendar('#calendar');
        calendar.init();
      });
    </script>
  </body>
</html>
```

```

### `docs/en/learn/internationalization-locale.mdx`

```mdx
---
title: Localization
description: Learn how to localize the calendar using the locale parameter or set the locale manually by providing arrays of month and weekday names.
section: 3. Internationalization
---

# Localization

If your locale is supported by the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString" rel="noopener noreferrer" target="_blank">`.toLocaleString()`</a> method, you can simply pass it to the `locale` parameter to localize the calendar.

<Sandbox example="internationalization-locale" />

If the locale is not supported or translated incorrectly, you can always set the locale manually. To do this, you need to provide arrays of month and weekday names instead of the language tag.

<Sandbox example="internationalization-assign-manually" />

```

### `docs/en/learn/internationalization-week-numbers.mdx`

```mdx
---
title: Week Numbers
description: Learn how to enable the display of week numbers in the calendar by setting the enableWeekNumbers parameter to true.
section: 3. Internationalization
---

# Week Numbers

In some countries, week numbers are used to denote dates.
You can enable the display of week numbers in the calendar by setting the `enableWeekNumbers` parameter to `true`.

<Sandbox example="internationalization-week-numbers" />

```

### `docs/en/learn/internationalization-weekday-first-and-weekdays.mdx`

```mdx
---
title: First Day of the Week and Weekends
description: Learn how to configure the first day of the week and weekends in the calendar. Change the ISO 8601 standard and assign any days of the week as weekends or disable them.
section: 3. Internationalization
---

# First Day of the Week and Weekends

By default, the calendar is based on the European standard **ISO 8601**. This means that the first day of the week is Monday.

Using separate parameters to define the first day of the week and the displayed weekends, you can specify any day as the first day of the week and assign any days of the week as weekends or completely disable them by specifying an empty array.

<Sandbox example="internationalization-weekday-first-and-weekdays" />

```

### `docs/en/learn/internationalization-weekends-and-holidays.mdx`

```mdx
---
title: Additional Weekends and Holidays
description: Learn how to specify additional weekends and holidays in the calendar. Mark these days in red by setting them manually.
section: 3. Internationalization
---

# Additional Weekends and Holidays

In the calendar, you can specify additional weekends or holidays that will be marked in red. These days should be set manually.

<Sandbox example="internationalization-weekends-and-holidays" />

```

### `docs/en/learn/type-default.mdx`

```mdx
---
title: Default (Single)
description: Learn how to use the 'default' calendar type to display one month and select days. Configure the calendar to display when clicking on an element with the inputMode parameter.
section: 2. Calendar Types
---

# Default (Single)

## Static

The `'default'` calendar type displays one month, allows you to select days, navigate between months using arrows, and select the month and year from the respective headers. This is the standard display mode for the calendar.

<Sandbox example="type-default" />

## With Input

If you need to display the calendar when clicking on an **«Input»**, you can easily configure it by initializing it with the `inputMode: true` parameter.

<Info>
  It is important to note that **«Input»** in the context of this calendar does not necessarily have to be an `<input>` tag. It can be any HTML element, such as a `<div>`. In **«Input»**, you can initialize any type of calendar.
</Info>

By default, the calendar does not write any values to the **«Input»** field, giving you unique control over what you want to see in the `value`.

<Sandbox example="type-default-in-input" height={470} input={true} />

```

### `docs/en/learn/type-month.mdx`

```mdx
---
title: Month
description: Learn how to use the 'month' calendar type to display a list of months and select months and years. Restrict the user's selection to only the month and year.
section: 2. Calendar Types
---

# Month

The `'month'` calendar type displays a list of months and allows the user to select months and years from the respective headers. This mode is useful if you need to restrict the user's selection to only the month and year, without the ability to select specific days.

<Sandbox example="type-month" />

```

### `docs/en/learn/type-multiple.mdx`

```mdx
---
title: Multiple
description: Learn how to use the 'multiple' calendar type to display multiple months and select dates. Configure the selection of date ranges with the selectionDatesMode parameter.
section: 2. Calendar Types
---

# Multiple

The `'multiple'` calendar type displays multiple months, allowing you to select days in each of them. This type of calendar is useful when the user needs to select multiple dates across different months. To do this, you need to use the `selectionDatesMode` parameter and set its value to `'multiple'`.

Example code for creating a calendar with the `'multiple'` type:

<Sandbox example="type-multiple" vertically={false} height={680} />

If you need to select date ranges, you can use the `selectionDatesMode` parameter and set its value to `'multiple-ranged'`. This allows you to select date ranges instead of individual days.

<Info>When the `selectionDatesMode` parameter is set to `'multiple-ranged'`, for performance optimization, the array of selected dates contains only the start and end dates. You can disable this and get the full list of selected dates using `enableEdgeDatesOnly`.</Info>

<Sandbox example="type-multiple-ranged" vertically={false} height={680} />

```

### `docs/en/learn/type-week.mdx`

```mdx
---
title: Week
new: true
description: Learn how to use the 'week' calendar type to show a single week instead of a whole month, and how the arrows step through weeks.
section: 2. Calendar Types
---

# Week

The `'week'` calendar type shows a single week instead of a whole month. It suits booking flows and any screen where the month grid takes more room than the choice deserves.

The strip opens on the week holding the first selected date when that date belongs to the displayed month. Otherwise it uses today when today belongs to that month, and finally the week holding the first day of `selectedMonth`.

<Sandbox example="type-week" height={300} />

The arrows step one week at a time and carry the strip across month boundaries. Every day is rendered as a day of the current period, so nothing is greyed out as an outside date and clicking one never moves the strip.

<Info>
  A week that straddles two months is titled by the month that owns it — the one holding its fourth day, the same rule that decides its ISO week number.
</Info>

## Folding a Month Down to a Week

`enableCollapse` adds a control under the grid that switches between the month and the week, so the visitor picks the view instead of you. See [Collapse](/docs/learn/additional-features-collapse) for the whole story.

The same controls work in `inputMode`. This popup opens as a week, expands to the whole month with `enableCollapse`, and pages the current view with `enableSwipe`:

<Sandbox example="type-week-in-input" height={470} input={true} />

## Switching Programmatically

Collapsing sets `type`, which makes the two views reachable from your own code as well:

```ts
calendar.set({ type: 'week' }); // fold down to a week
calendar.set({ type: 'default' }); // back to the month
calendar.type; // 'week' while collapsed
```

<Info>
  `displayMonthsCount` stays at `1` for this type; several weeks side by side are not supported. Use `type: 'multiple'` when you need more than one grid.
</Info>

```

### `docs/en/learn/type-year.mdx`

```mdx
---
title: Year
description: Learn how to use the 'year' calendar type to display a list of years and select the year and month. Restrict the user's selection to only the year and month.
section: 2. Calendar Types
---

# Year

The `'year'` calendar type displays a list of years, allowing the user to select a year from the list and a month from the corresponding header. This mode is useful if you need to restrict the user's selection to only the year and month, excluding the ability to select specific days.

<Sandbox example="type-year" />

```

### `docs/en/reference.mdx`

```mdx
---
title: Guide Overview
description: Page Description
---

# Guide Overview

This section provides detailed documentation on working with the **Vanilla Calendar Pro API**. If you're looking for an introduction to the features, please check out the [«Learn»](/docs/learn) section.

The Vanilla Calendar Pro API documentation is divided into several functional subsections:

1. **Instance Creation** — how and where to create a calendar instance.
2. **Utilities** — functions that allow you to format dates.
3. **Methods** — available methods for working with the calendar instance.
4. **Settings** — all options that can be provided to change the behavior and display of the calendar.
5. **Actions** — event handlers that allow you to receive and process various interaction data with the calendar.
6. **Popups** — pop-ups allow you to select any day and display brief information about it directly in the calendar when hovering over that day.
7. **Layouts** — templates that allow you to practically alter the entire DOM structure of the calendar and add your own HTML elements.
8. **Styles** — a CSS class object for styling the calendar. It allows you to use any CSS framework, like Tailwind CSS, or custom classes.
9. **Aria-labels** — an object of strings for `aria-label`. Allows you to localize all calendar labels to ensure accessibility.

```

### `docs/en/reference/actions.mdx`

```mdx
---
title: Actions
description: Learn about the various actions that can be configured for the calendar, including event handlers for clicks on dates, weeks, months, years, and arrows, as well as time changes and tooltip displays.
section: 5
---

# Actions

## onClickDate()

`Type: Function`

`Default: null`

`Options: onClickDate(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickDate(self, event) {},
});
```

This method is triggered after clicking on a day in the calendar. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `event` - mouse event.

<Info>
  It is important to know that each HTML day element contains a data attribute with the full date in the format `YYYY-MM-DD`.
  If you need to get the day, month, and year separately, you can use standard JS methods.
  For example: `new Date('2022-11-07').getDate()` will return `7`.
</Info>

---

## onClickWeekDay()

`Type: Function`

`Default: null`

`Options: onClickWeekDay(self, day, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekDay(self, day, dateEls, event) {},
});
```

This method is triggered after clicking on a weekday in the calendar. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `day` - week day;
- `dateEls` - array of days (html elements);
- `event` - mouse event.

---

## onClickWeekNumber()

`Type: Function`

`Default: null`

`Options: onClickWeekNumber(self, number, year, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekNumber(self, number, year, dateEls, event) {},
});
```

This method is triggered after clicking on a week number in the calendar, but for it to work, the `enableWeekNumbers` parameter must be set to `true`. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `number` - week number;
- `year` - year of the week;
- `dateEls` - array of days (html elements);
- `event` - mouse event.

---

## onClickTitle()

`Type: Function`

`Default: null`

`Options: onClickTitle(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickTitle(self, event) {},
});
```

This method is triggered after clicking on the month or year title in the calendar. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `event` - mouse event.

---

## onClickMonth()

`Type: Function`

`Default: null`

`Options: onClickMonth(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickMonth(self, event) {},
});
```

This method is triggered after selecting a month in the calendar. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `event` - mouse event.

---

## onClickYear()

`Type: Function`

`Default: null`

`Options: onClickYear(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickYear(self, event) {},
});
```

This method is triggered after selecting a year in the calendar. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `event` - mouse event.

---

## onClickArrow()

`Type: Function`

`Default: null`

`Options: onClickArrow(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickArrow(self, event) {},
});
```

This method is triggered after clicking on an arrow in the calendar. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `event` - mouse event.

---

## onChangeTime()

`Type: Function`

`Default: null`

`Options: onChangeTime(self, event, isError) => void | null`

```ts
new Calendar('#calendar', {
  onChangeTime(self, event) {},
});
```

This method is triggered after changing the time in the calendar. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `event` - change event;
- `isError` - returns true if the user entered an incorrect time.

---

## onChangeToInput()

`Type: Function`

`Default: null`

`Options: onChangeToInput(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onChangeToInput(self, event) {},
});
```

For this method to work, the `inputMode` parameter must be set to `true`.
This method is triggered after clicking on a day in the calendar or changing the time in any way.
You can get the following parameters:
- `self` - reference to the initialized calendar;
- `event` - event.

---

## onCreateDateRangeTooltip()

`Type: Function`

`Default: null`

`Options: onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) {},
});
```

Allows creating a tooltip for a date range. Triggers on clicking and hovering over a day if the `selectionDatesMode` parameter is set to `'multiple-ranged'`.
You can get the following parameters:
- `self` - reference to the initialized calendar.
- `dateEl` - HTML date element;
- `tooltipEl` - HTML tooltip element;
- `dateElBCR` - object with information about the position and size of the HTML date element;
- `mainElBCR` - object with information about the position and size of the main HTML calendar element.

---

## onCreateDateEls()

`Type: Function`

`Default: null`

`Options: onCreateDateEls(self, dateEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateEls(self, dateEl) {},
});
```

This method is triggered during calendar initialization and any changes. It provides access to information about each day. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `dateEl` - HTML date element.

---

## onCreateMonthEls()

`Type: Function`

`Default: null`

`Options: onCreateMonthEls(self, monthEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateMonthEls(self, monthEl) {},
});
```

This method is triggered when the calendar type is set to `'month'`. The calendar type also becomes `'month'` when the user clicks on the month title or during initialization with the parameter `type = 'month'`. It provides access to information about each month. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `monthEl` - HTML month element.

---

## onCreateYearEls()

`Type: Function`

`Default: null`

`Options: onCreateYearEls(self, yearEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateYearEls(self, yearEl) {},
});
```

This method is triggered when the calendar type is set to `'year'`. The calendar type becomes `'year'` when the user clicks on the year title or during initialization with the parameter `type = 'year'`. It provides access to information about each year. You can get the following parameters:
- `self` - reference to the initialized calendar;
- `yearEl` - HTML year element.

---

## onInit()

`Type: Function`

`Default: null`

`Options: onInit(self) => void | null`

```ts
new Calendar('#calendar', {
  onInit(self) {},
});
```

This method is triggered during calendar initialization. If the `inputMode` parameter is set to `true`, the method will execute on the first display of the calendar, as this is when the calendar is initialized.
- `self` - reference to the initialized calendar.

---

## onUpdate()

`Type: Function`

`Default: null`

`Options: onUpdate(self) => void | null`

```ts
new Calendar('#calendar', {
  onUpdate(self) {},
});
```

This method is triggered when the calendar is updated/reset using the `.update()` method.
- `self` - reference to the initialized calendar.

---

## onDestroy()

`Type: Function`

`Default: null`

`Options: onDestroy(self) => void | null`

```ts
new Calendar('#calendar', {
  onDestroy(self) {},
});
```

This method is triggered when the calendar is destroyed.
- `self` - reference to the initialized calendar.

---

## onShow()

`Type: Function`

`Default: null`

`Options: onShow(self) => void | null`

```ts
new Calendar('#calendar', {
  onShow(self) {},
});
```

This method is triggered when the calendar is displayed to the user, but only if the `inputMode` parameter is set to `true`.
- `self` - reference to the initialized calendar.

---

## onHide()

`Type: Function`

`Default: null`

`Options: onHide(self) => void | null`

```ts
new Calendar('#calendar', {
  onHide(self) {},
});
```

This method is triggered when the calendar is hidden, but only if the `inputMode` parameter is set to `true`.
- `self` - reference to the initialized calendar.

```

### `docs/en/reference/creating-an-instance.mdx`

```mdx
---
title: Creating an Instance
description: Learn how to create an instance of Vanilla Calendar Pro using a CSS selector or HTML element. Configure the calendar to initialize in a wrapper or popup when clicking on an element.
section: 1
---

# Creating an Instance

`new Calendar()` - creates an instance of **Vanilla Calendar Pro**, which is an encapsulation of the calendar, its settings, and methods.

<Info>If you included **Vanilla Calendar Pro** using the `<script>` tag, the object is available as a global variable **window.VanillaCalendarPro**.</Info>

The `Calendar` instance takes two parameters. The first **required** parameter can be a **CSS selector** or **HTML element**.

The **CSS selector** or **HTML element** can represent a wrapper for the calendar, in which the calendar will be initialized, or an **«Input»**.

A calendar wrapper is a `<div>` tag inside which the calendar itself will be initialized.

Initialization in a calendar wrapper:

```html
<div id="calendar"></div>
```

```ts
new Calendar('#calendar');
// or
const calendarEl = document.querySelector('#calendar');
new Calendar(calendarEl);
```

**«Input»** in the context of this calendar does not necessarily mean an `<input>` tag; it can be any HTML element, such as a `<div>`.

When clicking on the **«Input»**, a popup with the calendar will appear.

Initialization in an **«Input»**:

```html
<input type="text" id="input">
<!-- or -->
<div id="input"></div>
```

```ts
new Calendar('#input', { inputMode: true });
// or
const calendarInput = document.querySelector('#input');
new Calendar(calendarInput, {
  inputMode: true,
});
```

The second **optional** parameter is an object defining the settings and actions of the calendar.

```ts
new Calendar('#calendar', {
  // Settings
});
```

```

### `docs/en/reference/labels.mdx`

```mdx
---
title: Aria Labels
description: Aria labels allow you to localize all aria-labels in the calendar for accessibility.
section: 9
---

# Aria Labels

`labels` provides the ability to localize all aria-labels in the calendar for accessibility.

Below is a list of all default aria-labels.

```ts
new Calendar('#calendar', {
  labels: {
    application: 'Calendar',
    navigation: 'Calendar Navigation',
    arrowNext: {
      month: 'Next month',
      year: 'Next list of years',
      week: 'Next week',
    },
    arrowPrev: {
      month: 'Previous month',
      year: 'Previous list of years',
      week: 'Previous week',
    },
    month: 'Select month, current selected month:',
    months: 'List of months',
    year: 'Select year, current selected year:',
    years: 'List of years',
    week: 'Days of the week',
    weekNumber: 'Numbers of weeks in a year',
    collapse: 'Collapse to a single week',
    expand: 'Expand to the whole month',
    dates: 'Dates in the current month',
    selectingTime: 'Selecting a time ',
    inputHour: 'Hours',
    inputMinute: 'Minutes',
    rangeHour: 'Slider for selecting hours',
    rangeMinute: 'Slider for selecting minutes',
    btnKeeping: 'Switch AM/PM, current position:',
  },
});
```

```

### `docs/en/reference/layouts.mdx`

```mdx
---
title: Layouts
description: Layouts allow you to change the DOM structure of the calendar and add your own HTML elements.
section: 7
---

# Layouts

Layouts allow you to almost completely change the DOM structure of the calendar and add your own HTML elements, such as buttons. Each type of calendar has its own default template, and you can customize each of them.

<Info>
  Tags containing the symbol **«#»** are registered components of the calendar and should contain a closing slash at the end of the tag, except for the tag **\<#Multiple>\<#/Multiple>**, which wraps one month.
  All default templates list all possible components for that template.
</Info>

## layouts.default

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    default: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

This is the default template for displaying one month and its dates.

---

## layouts.multiple

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    multiple: `
      <div class="${self.styles.controls}" data-vc="controls" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.grid}" data-vc="grid">
        <#Multiple>
          <div class="${self.styles.column}" data-vc="column" role="group">
            <div class="${self.styles.header}" data-vc="header">
              <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
                <#Month />
                <#Year />
              </div>
            </div>
            <div class="${self.styles.wrapper}" data-vc="wrapper">
              <#WeekNumbers />
              <div class="${self.styles.content}" data-vc="content">
                <#Week />
                <#Dates />
              </div>
            </div>
          </div>
        <#/Multiple>
        <#DateRangeTooltip />
      </div>
      <#ControlTime />
    `,
  },
});
```

This is the default template for displaying multiple months and their dates.

---

## layouts.month

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    month: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Months />
        </div>
      </div>
    `,
  },
});
```

This is the default template for selecting a month.

---

## layouts.year

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    year: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [year] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [year] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Years />
        </div>
      </div>
    `,
  },
});
```

This is the default template for selecting a year.

---

## layouts.week

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    week: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [week] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [week] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

This is the default template for a single week. It matches `layouts.default` apart from the arrows, which step a week at a time.

```

### `docs/en/reference/methods.mdx`

```mdx
---
title: Methods
description: Methods for managing the calendar, including initialization, updating, setting parameters, deleting, showing, and hiding the calendar.
section: 3
---

# Methods

## init()

The `init()` method is the main instance method that starts the calendar initialization process.

```ts
const calendar = new Calendar(element, params);
calendar.init();
```

---

## update()

The `update()` method allows you to apply new settings to the calendar and perform a reset.
This method accepts an object with optional arguments to control the reset, by default resetting the user-selected date, month, and year after the update.

All arguments default to `true`:

```ts
{
  year: boolean;
  month: boolean;
  dates: boolean | 'only-first';
  holidays: boolean;
  time: boolean;
}
```

- `true` - will reset to the parameters specified in the settings;
- `false` - will not perform a reset, leaving the parameters selected by the user;
- `'only-first'` - resets all selected dates, leaving only the earliest one. If the date selection type is specified as `'multiple-ranged'`, a `'mousemove'` and `'keydown'` handler is added for hovering.

Example usage:

```ts
calendar.locale = 'de-AT';
calendar.firstWeekday = 0;

calendar.update({
  dates: true,
});
```

---

## set()

If you need to specify new parameters or handlers for a calendar that is not yet initialized or already initialized, you can use the `.set()` method.
This method accepts an object with new parameters and an object with optional arguments to control the reset, by default resetting the user-selected date, month, and year after the update.

Example usage:

```ts
calendar.set({
  locale: 'de-AT',
  firstWeekday: 0,
}, {
  dates: true,
});
```

This method can be an alternative to specifying parameters when creating a calendar instance. If you call this method before initialization, do not specify the object for controlling the reset.

```ts
const calendar = new Calendar(element);
calendar.set({ locale: 'de-AT', firstWeekday: 0 });
calendar.init();
```

---

## destroy()

If you need to completely delete the calendar instance, you can use the `destroy()` method.

```ts
calendar.destroy();
```

---

## show()

The `show()` method allows you to display the calendar if it was hidden.

```ts
calendar.show();
```

---

## hide()

The `hide()` method allows you to hide the calendar if it was shown.

```ts
calendar.hide();
```

```

### `docs/en/reference/popups.mdx`

```mdx
---
title: Popups
description: Popups allow you to highlight any day and display brief information about it directly in the calendar when hovering over the day.
section: 6
---

# Popups

Popups allow you to highlight any day and display brief information about it directly in the calendar when hovering over the day.

## popups['date']

`Type: String`

`Default: null`

`Options: 'YYYY-MM-DD' | 'YYYY-MM-DD:YYYY-MM-DD' | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {},
    '2022-07-01:2022-07-05': {},
  }
});
```

Dates in the format `YYYY-MM-DD` are used as keys. In the given example, a popup is set for June 28, 2022.

<Info>A key can also be a date range in the form `'YYYY-MM-DD:YYYY-MM-DD'` (any delimiter works between the two dates). The same popup (`modifier`/`html`) is then applied to every day in that range, instead of having to repeat an identical entry for each date.</Info>

---

## popups['date'].modifier

`Type: String`

`Default: null`

`Options: CSS classes | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
    },
  }
});
```

`modifier` accepts arbitrary CSS classes separated by spaces. Using these classes, you can style the date to make it highlighted or change its appearance.

---

## popups['date'].html

`Type: String`

`Default: null`

`Options: '' | HTML | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
      html: `<div>
        <u><b>12:00 PM</b></u>
        <p style="margin: 5px 0 0;">Airplane in Las Vegas</p>
      </div>`,
      // or just text
      // html: 'Airplane in Las Vegas',
    },
  }
});
```

`html` accepts plain text or HTML markup for formatting the popup.
In this example, when hovering over June 28, 2022, a popup will be displayed with the text "Airplane in Las Vegas" and the time "12:00 PM", and the styles specified in the classes `bg-red` and `color-pink` will be applied.

```

### `docs/en/reference/settings.mdx`

```mdx
---
title: Settings
description: Calendar settings, including display type, input mode, positioning, localization, dates and times.
new:
  - animation
  - enableCollapse
  - enableSwipe
section: 4
---

# Settings

## type

`Type: String`

`Default: 'default'`

`Options: 'default' | 'multiple' | 'month' | 'year' | 'week'`

```ts
new Calendar('#calendar', {
  type: 'default',
});
```

The `type` parameter defines the type of calendar displayed. The `week` type shows a single week rather than a whole month. It works on its own or with `enableCollapse`, which lets visitors switch between the month and week views.

---

## inputMode

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  inputMode: true,
});
```

The `inputMode` parameter indicates that the `mainElement`, passed as the first parameter, represents an input field rather than a wrapper for the calendar.

---

## openOnFocus

`Type: Boolean | Function`

`Default: true`

`Options: true | false | () => false`

```ts
new Calendar('#calendar', {
  openOnFocus: false,
  // or with a callback
  openOnFocus: (self) => !self.context.isShowInInputMode,
});
```

If the `openOnFocus` parameter is `true` or the callback returns `true`, then focusing the input will open the calendar. Use `false` or a callback to control this behavior and implement your own focus handler.

---

## positionToInput

`Type: String`

`Default: 'left'`

`Options: 'auto' | 'center' | 'left' | 'right' | ['bottom' | 'top', 'center' | 'left' | 'right']`

```ts
new Calendar('#calendar', {
  positionToInput: 'auto',
  // positionToInput: ['bottom', 'center'],
});
```

This parameter defines the position of the calendar relative to the input if the calendar is initialized with the `inputMode` parameter.

`positionToInput` accepts a string with the value `'left'`, `'center'`, or `'right'`, or an array of values `[Y-axis, X-axis]`, where the Y-axis can be `'bottom'` or `'top'`, and the X-axis can be `'left'`, `'center'`, or `'right'`.
If the Y-axis is not specified, the default value `'bottom'` is used.

You can use the value `positionToInput: 'auto'` to automatically determine the best position based on the available space in the viewport.
The option allows calculating the available space on all 4 sides and will first try to display the calendar below the input, which is the default position.
If there is not enough space below, it will evaluate another best available position.

---

## animation

`Type: Boolean | Object`

`Default: false`

`Options: true | false | { duration?: Number, easing?: String, slide?: Timing, fade?: Timing, collapse?: Timing }`

`Timing: { duration?: Number, easing?: String }`

```ts
new Calendar('#calendar', {
  animation: true,
  // animation: { duration: 400, easing: 'ease-out' },
  // animation: { slide: { duration: 400 }, fade: { duration: 120 }, collapse: { duration: 300 } },
});
```

Animates transitions between views. Arrow navigation and `enableSwipe` use a horizontal slide, the month and year pickers cross-fade, and `enableCollapse` animates the calendar between its month and week heights.

Defaults differ per transition — `250ms` for the slides, `150ms` for the cross-fade and `300ms` for collapsing, all with `cubic-bezier(0.4, 0, 0.2, 1)`. An object overrides any of them: `duration` is in milliseconds, and `easing` accepts a CSS easing function. Values at the top level apply to every transition; nest them under `slide` (arrows and `enableSwipe`), `fade` (pickers) or `collapse` (`enableCollapse`) to target one group. Nested values win over top-level values.

<Info>
  Animated settling is skipped when the visitor asks for reduced motion through `prefers-reduced-motion: reduce`. Gestures still follow the pointer, but commit
  or return immediately on release.
</Info>

The default is `false` for backwards compatibility: the option was added later, and turning it on changes what a DOM query sees during slide and cross-fade transitions. Their outgoing content stays in the DOM inside an `inert` `[data-vc-ghost]` layer, so date elements can briefly be present twice. Exclude that layer if your own code queries them; collapsing does not create a ghost layer.

---

## firstWeekday

`Type: Number`

`Default: 1`

`Options: from 0 to 6`

```ts
new Calendar('#calendar', {
  firstWeekday: 1,
});
```

This parameter sets the first day of the week. Specify a number from 0 to 6, where the number represents the day of the week identifier. According to JS standards, the days of the week start with 0, and 0 is Sunday.

---

## monthsToSwitch

`Type: Number`

`Default: 1`

`Options: from 1 to 12`

```ts
new Calendar('#calendar', {
  monthsToSwitch: 1,
});
```

The `monthsToSwitch` parameter controls the number of switchable months.

<Info>
  When `monthsToSwitch` is greater than `1`, the month picker view will also only allow selecting months that are reachable from the currently selected month in
  steps of `monthsToSwitch` — other months will appear disabled. This keeps navigation consistent with the configured step size (most relevant together with
  `displayMonthsCount` in `type: 'multiple'`, where it keeps multiple visible months in sync).
</Info>

---

## themeAttrDetect

`Type: String | false`

`Default: 'html[data-theme]'`

`Options: string | false`

```ts
new Calendar('#calendar', {
  themeAttrDetect: 'html[data-theme]',
});
```

To have the calendar automatically track and apply the site's theme, you can pass a string value in the form of a CSS selector.
Square brackets indicate an attribute containing the theme name.
By default, the `html` tag with the `data-theme` attribute is tracked, but you can configure any other attribute and tag, for example, `class`, if the class name is used to set the theme: `'html[class]'`.
If set to `false`, the theme will be determined by the user's system or the `selectedTheme` parameter.

---

## locale

`Type: String`

`Default: 'en'`

`Options: Language label | Array<locale>`

```ts
new Calendar('#calendar', {
  locale: 'en',
  // Or specify an object for your labels
  // locale: {
  //   months: {
  //     long: [],
  //     short: [],
  //   },
  //   weekday: {
  //     long: [],
  //     short: [],
  //   }
  // },
});
```

This parameter sets the language localization of the calendar.
You can specify a language label according to <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry" target="_blank" rel="nofollow noreferrer">BCP 47</a> or provide arrays of month and weekday names, see more details [here](/docs/learn/internationalization-locale).

---

## dateToday

`Type: Date object`

`Default: 'today'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateToday: 'today',
});
```

The `dateToday` parameter defines which day will be considered today for the calendar.

---

## dateMin

`Type: String`

`Default: '1970-01-01'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMin: '1970-01-01',
});
```

The `dateMin` parameter sets the minimum allowable date that the calendar will consider and which cannot be less than this date.

---

## dateMax

`Type: String`

`Default: '2470-12-31'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMax: '2470-12-31',
});
```

The `dateMax` parameter sets the maximum allowable date that the calendar will consider and which cannot be greater than this date.

---

## displayDateMin

`Type: String`

`Default: '1970-01-01'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMin: '2022-07-01',
});
```

This parameter sets the minimum date that the user can select. Dates earlier than the specified date will be disabled and unavailable for selection.

<Info>
  It is important to note that `displayDateMin` and `displayDateMax` disable dates outside the range, while `dateMin` and `dateMax` do not create them at all.
</Info>

<Info>
  Passing `null` to `displayDateMin` in `.set()` explicitly resets it back to its default value. Passing `undefined` (e.g. omitting the property) leaves the
  current value unchanged.
</Info>

---

## displayDateMax

`Type: String`

`Default: '2470-12-31'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMax: '2024-07-01',
});
```

This parameter sets the maximum date that the user can select. Dates later than the specified date will be disabled and unavailable for selection.

<Info>
  It is important to note that `displayDateMin` and `displayDateMax` disable dates outside the range, while `dateMin` and `dateMax` do not create them at all.
</Info>

<Info>
  Passing `null` to `displayDateMax` in `.set()` explicitly resets it back to its default value. Passing `undefined` (e.g. omitting the property) leaves the
  current value unchanged.
</Info>

---

## displayDatesOutside

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  displayDatesOutside: false,
});
```

With this parameter, you can decide whether to display days from the previous and next month.

---

## displayDisabledDates

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  displayDisabledDates: false,
});
```

This parameter determines whether all days, including disabled days, will be displayed.

---

## displayMonthsCount

`Type: Number`

`Default: 2`

`Options: from 2 to 12`

```ts
new Calendar('#calendar', {
  displayMonthsCount: 2,
});
```

The `displayMonthsCount` parameter defines the number of months displayed if the calendar type is set to `'multiple'`.

---

## disableDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  disableDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

This parameter allows you to disable specified dates, regardless of the specified range.

<Info>To specify a date range, use any delimiter between dates within a single string.</Info>

---

## disableAllDates

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableAllDates: true,
});
```

This parameter disables all days and can be useful when using `enableDates`.

---

## disableDatesPast

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableDatesPast: true,
});
```

This parameter disables all past days.

---

## disableDatesGaps

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableDatesGaps: true,
});
```

This parameter disables the selection of days within a range with disabled dates. It only works if the `selectionDatesMode` parameter is set to `'multiple-ranged'`.

---

## disableWeekdays

`Type: Number`

`Default: []`

`Options: from 0 to 6`

```ts
new Calendar('#calendar', {
  disableWeekdays: [0, 6],
});
```

This parameter allows you to disable specified weekdays. Specify an array with numbers from 0 to 6, where each number represents a day of the week identifier. According to JS standards, the days of the week start with 0, and 0 is Sunday.

---

## disableToday

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableToday: true,
});
```

With this parameter, you can disable the selection of today's date in the calendar.

---

## enableDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  enableDates: ['2022-08-11:2022-08-16', '2022-08-20', 1722152977141, new Date()],
});
```

This parameter allows you to enable specified dates, regardless of the range and disabled dates.

<Info>To specify a date range, use any delimiter between dates within a single string.</Info>

---

## enableEdgeDatesOnly

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableEdgeDatesOnly: true,
});
```

This parameter allows you to get only the start and end dates selected by the user, ignoring intermediate dates. This parameter only works if `selectionDatesMode` is set to `'multiple-ranged'`.

<Info>
  It is important to note that when using this parameter, disabled dates within the date range will have no effect. Therefore, use this option only if you are
  interested in the start and end dates selected by the user.
</Info>

---

## enableDateToggle

`Type: Boolean | Function`

`Default: true`

`Options: true | false | () => false`

```ts
new Calendar('#calendar', {
  enableDateToggle: false,
  // or with a callback
  enableDateToggle: (self) => new Date(self.selectedDates[0]) < new Date(),
});
```

If the `enableDateToggle` parameter is `true` or the callback returns `true`, then clicking on a selected date again will deselect it.

---

## enableWeekNumbers

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableWeekNumbers: true,
});
```

With this parameter, you can decide whether to display week numbers in the year.

---

## enableMonthChangeOnDayClick

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableMonthChangeOnDayClick: false,
});
```

With this parameter, you can decide whether the month will switch when clicking on a day from the previous or next month.

---

## enableJumpToSelectedDate

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableJumpToSelectedDate: true,
  selectedDates: ['2018-05-02'],
});
```

If this option is enabled and one or more selected dates are specified, but without specifying `selectedMonth` and `selectedYear`, the calendar will jump to the first selected date. If set to `false`, the calendar will always open for the current month and year.

<Info>This option has no effect if `selectedMonth` and `selectedYear` are specified.</Info>

---

## enableCollapse

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableCollapse: true,
});
```

Adds a control under the grid that folds the month down to one week and unfolds it again. The week is anchored to the first selected date when it belongs to the displayed month, otherwise to today when it belongs to that month, and otherwise to the first day of the displayed month. The control is a chevron on devices with a mouse and a grabber on touch devices, which can be dragged up and down.

<Info>`enableCollapse` does not require `enableSwipe` or `animation`. Collapsing switches `type` to `'week'`, so reading `calendar.type` tells you the current state, and `set({ type: 'week' })` does the same thing without the transition. Only the `default` and `week` types support this option; other types throw during `init()`.</Info>

---

## enableSwipe

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableSwipe: true,
});
```

Lets the visitor drag the calendar content sideways to reach the next or previous period in every view the arrows can navigate — `default`, `multiple`, `week` and the year list. The neighbouring period follows the pointer. Release distance and velocity decide whether it settles into place or returns.

<Info>
  `enableSwipe` does not require `enableCollapse` or `animation`; without animation, release settles immediately. Vertical scrolling over the calendar is left
  to the page, and a swipe is available only while the corresponding arrow is visible, so it observes `dateMin`, `dateMax` and navigation restrictions. The drag
  does not select the date it ends on.
</Info>

---

## selectionDatesMode

`Type: String | false`

`Default: 'single'`

`Options: 'single' | 'multiple' | 'multiple-ranged' | false`

```ts
new Calendar('#calendar', {
  selectionDatesMode: 'single',
});
```

This parameter determines whether selecting one or multiple days is allowed, or if date selection is completely disabled.

---

## selectionMonthsMode

`Type: Boolean`

`Default: true`

`Options: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionMonthsMode: false,
});
```

This parameter allows you to disable month selection, allow month switching only with arrows, or allow month switching in any way.

---

## selectionYearsMode

`Type: Boolean`

`Default: true`

`Options: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionYearsMode: false,
});
```

This parameter allows you to disable year selection, allow year switching only with arrows, or allow year switching in any way.

---

## selectionTimeMode

`Type: false | Number`

`Default: false`

`Options: false | 24 | 12`

```ts
new Calendar('#calendar', {
  selectionTimeMode: true,
});
```

This parameter enables time selection. You can also specify the time format using a number: 24-hour or 12-hour format.

---

## selectedDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  selectedDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

This parameter allows you to specify a list of dates that will be selected when the calendar is initialized.

<Info>To specify a date range, use any delimiter between dates within a single string.</Info>

---

## selectedMonth

`Type: Number`

`Default: null`

`Options: from 0 to 11 | null`

```ts
new Calendar('#calendar', {
  selectedMonth: 0,
});
```

This parameter defines the month that will be displayed when the calendar is initialized. According to JS standards, months are numbered from 0 to 11. See [enableJumpToSelectedDate](/docs/reference/settings#enablejumptoselecteddate) to default to the first selected date.

---

## selectedYear

`Type: Number`

`Default: null`

`Options: Number (YYYY) | null`

```ts
new Calendar('#calendar', {
  selectedYear: 2022,
});
```

This parameter defines the year that will be displayed when the calendar is initialized. See [enableJumpToSelectedDate](/docs/reference/settings#enablejumptoselecteddate) to default to the first selected date.

---

## selectedHolidays

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  selectedHolidays: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

This parameter allows you to specify dates that will be considered holidays and will receive an additional data attribute for styling.

<Info>To specify a date range, use any delimiter between dates within a single string.</Info>

---

## selectedWeekends

`Type: Number`

`Default: [0, 6]`

`Options: number[0-6]`

```ts
new Calendar('#calendar', {
  selectedWeekends: [0, 6],
});
```

This parameter allows you to specify the weekend days of the week. Specify an array with numbers from 0 to 6, where each number represents a day of the week identifier. According to JS standards, the days of the week start with 0, and 0 is Sunday.

---

## selectedTime

`Type: String`

`Default: null`

`Options: 'hh:mm aa' | null`

```ts
new Calendar('#calendar', {
  selectedTime: '03:44 AM',
});
```

This parameter allows you to set the time that will be displayed when the calendar is initialized. The time is set in the format `'hh:mm aa'`, where `'aa'` is the AM/PM marker. If using the 24-hour format, the `'aa'` marker is not required.

---

## selectedTheme

`Type: String`

`Default: 'system'`

`Options: string (custom theme) | 'light' | 'dark' | 'system'`

```ts
new Calendar('#calendar', {
  selectedTheme: 'system',
});
```

This parameter defines the theme of the calendar. By default, the theme is determined by the user's system or the site settings.

---

## timeMinHour

`Type: Number`

`Default: 0`

`Options: from 0 to 23`

```ts
new Calendar('#calendar', {
  timeMinHour: 0,
});
```

This parameter specifies which hour will be the minimum for selection.

---

## timeMaxHour

`Type: Number`

`Default: 23`

`Options: from 0 to 23`

```ts
new Calendar('#calendar', {
  timeMaxHour: 23,
});
```

This parameter specifies which hour will be the maximum for selection.

---

## timeMinMinute

`Type: Number`

`Default: 0`

`Options: from 0 to 59`

```ts
new Calendar('#calendar', {
  timeMinMinute: 0,
});
```

This parameter specifies which minute will be the minimum for selection.

---

## timeMaxMinute

`Type: Number`

`Default: 59`

`Options: from 0 to 59`

```ts
new Calendar('#calendar', {
  timeMaxMinute: 59,
});
```

This parameter specifies which minute will be the maximum for selection.

---

## timeControls

`Type: String`

`Default: 'all'`

`Options: 'all' | 'range'`

```ts
new Calendar('#calendar', {
  timeControls: 'all',
});
```

This parameter defines the method of time selection: `'all'` (any method) or `'range'` (only with the controller).

---

## timeStepHour

`Type: Number`

`Default: 1`

`Options: from 1 to 23`

```ts
new Calendar('#calendar', {
  timeStepHour: 1,
});
```

This parameter sets the step for the hour controller.

---

## timeStepMinute

`Type: Number`

`Default: 1`

`Options: from 1 to 59`

```ts
new Calendar('#calendar', {
  timeStepMinute: 1,
});
```

This parameter sets the step for the minute controller.

---

## sanitizerHTML

`Type: Function`

`Default: (html) => html`

```ts
import DOMPurify from 'dompurify';

new Calendar('#calendar', {
  sanitizerHTML: (html) => DOMPurify.sanitize(html),
});
```

`sanitizerHTML` can sanitize HTML templates to make them safe for CSP.

<Info>
  Note that the example uses the third-party library{' '}
  <a href="https://www.npmjs.com/package/dompurify" target="_blank" rel="nofollow noreferrer">
    `dompurify`
  </a>
  . `sanitizerHTML` is not required for the calendar to function.
</Info>

```

### `docs/en/reference/styles.mdx`

```mdx
---
title: Styles
description: A comprehensive guide to customizing CSS classes in the calendar using the styles parameter, including a list of default classes and their replacement.
section: 8
---

# Styles

`styles` provides the ability to override any CSS class in the calendar. You can replace any values with a list of CSS classes.

Below is a list of all default classes.

## CSS Classes

```ts
new Calendar('#calendar', {
  styles: {
    // Basics
    calendar: 'vc',
    controls: 'vc-controls',
    grid: 'vc-grid',
    column: 'vc-column',

    // Header
    header: 'vc-header',
    headerContent: 'vc-header__content',
    month: 'vc-month',
    year: 'vc-year',
    arrowPrev: 'vc-arrow vc-arrow_prev',
    arrowNext: 'vc-arrow vc-arrow_next',

    // Month / year picker
    wrapper: 'vc-wrapper',
    content: 'vc-content',
    months: 'vc-months',
    monthsRow: 'vc-months__row',
    monthsCell: 'vc-months__cell',
    monthsMonth: 'vc-months__month',
    years: 'vc-years',
    yearsRow: 'vc-years__row',
    yearsCell: 'vc-years__cell',
    yearsYear: 'vc-years__year',

    // Week row / week numbers
    week: 'vc-week',
    weekDay: 'vc-week__day',
    weekDayBtn: 'vc-week__day-btn',
    weekNumbers: 'vc-week-numbers',
    weekNumbersTitle: 'vc-week-numbers__title',
    weekNumbersContent: 'vc-week-numbers__content',
    weekNumber: 'vc-week-number',

    // Dates
    collapse: 'vc-collapse',
    dates: 'vc-dates',
    datesRow: 'vc-dates__row',
    date: 'vc-date',
    dateBtn: 'vc-date__btn',

    // Popups and tooltip
    datePopup: 'vc-date__popup',
    dateRangeTooltip: 'vc-date-range-tooltip',

    // Time controls
    time: 'vc-time',
    timeContent: 'vc-time__content',
    timeHour: 'vc-time__hour',
    timeMinute: 'vc-time__minute',
    timeKeeping: 'vc-time__keeping',
    timeRanges: 'vc-time__ranges',
    timeRange: 'vc-time__range',
  },
});
```

---

## CSS Variables

Every color in the built-in themes (`light`, `dark`, `slate-light`) is defined through a CSS custom property with the theme's original color as the fallback. This means you can restyle the calendar by setting a handful of variables, without touching any CSS classes or waiting for a theme override to cascade correctly.

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

If a variable is left unset, the calendar renders exactly as before — nothing changes unless you explicitly set a variable.

<Info>Setting a variable on `:root` applies it across all themes at once (light/dark/slate-light all read the same variable names). To restyle only one theme, scope the override to that theme's selector instead, e.g. `[data-vc-theme='dark'] { --vc-date-selected-bg: #7c3aed; }`.</Info>

### Base

| Variable                   | light      | dark       | slate-light |
| -------------------------- | ---------- | ---------- | ----------- |
| `--vc-bg`                  | white      | slate-900  | slate-100   |
| `--vc-color`               | slate-900  | white      | gray-800    |
| `--vc-focus-outline-color` | orange-300 | orange-300 | blue-300    |

### Header / title

| Variable                    | light     | dark      | slate-light |
| --------------------------- | --------- | --------- | ----------- |
| `--vc-header-color`         | slate-900 | white     | gray-800    |
| `--vc-title-color`          | slate-900 | white     | gray-800    |
| `--vc-title-color-hover`    | slate-500 | slate-500 | gray-600    |
| `--vc-title-color-disabled` | slate-300 | slate-700 | gray-400    |

### Month / year picker

| Variable                           | light     | dark      | slate-light |
| ---------------------------------- | --------- | --------- | ----------- |
| `--vc-months-years-bg`             | white     | slate-900 | slate-100   |
| `--vc-months-years-color`          | slate-500 | white     | gray-600    |
| `--vc-months-years-bg-hover`       | slate-100 | slate-800 | slate-200   |
| `--vc-months-years-color-disabled` | slate-300 | slate-700 | gray-400    |
| `--vc-months-years-bg-selected`    | cyan-500  | slate-500 | blue-500    |
| `--vc-months-years-color-selected` | white     | white     | white       |

### Collapse control

| Variable              | light     | dark      | slate-light |
| --------------------- | --------- | --------- | ----------- |
| `--vc-collapse-color` | slate-300 | slate-600 | slate-300   |

### Week row / week numbers

| Variable                        | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-week-numbers-title-color` | slate-500 | white     | gray-600    |
| `--vc-week-number-color`        | slate-500 | white     | gray-600    |
| `--vc-week-number-color-hover`  | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-color`           | slate-500 | white     | gray-600    |
| `--vc-week-day-color-hover`     | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-off-color`       | rose-500  | rose-500  | red-500     |
| `--vc-week-day-off-color-hover` | rose-600  | rose-600  | red-600     |

### Dates

| Variable                                     | light     | dark      | slate-light |
| -------------------------------------------- | --------- | --------- | ----------- |
| `--vc-date-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-color`                            | slate-900 | slate-400 | gray-800    |
| `--vc-date-color-hover` <sup>dark only</sup> | —         | slate-200 | —           |
| `--vc-date-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-edge-bg`                    | slate-200 | slate-700 | slate-300   |
| `--vc-date-disabled-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-outside-color`                    | slate-400 | slate-600 | gray-400    |
| `--vc-date-today-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-today-color`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-today-outside-color`              | slate-500 | slate-600 | gray-600    |
| `--vc-date-selected-bg`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-selected-color`                   | white     | white     | white       |
| `--vc-date-selected-outside-bg`              | slate-300 | slate-700 | slate-300   |
| `--vc-date-selected-outside-color`           | slate-500 | slate-300 | gray-600    |

### Weekends / holidays

| Variable                                                     | light     | dark      | slate-light |
| ------------------------------------------------------------ | --------- | --------- | ----------- |
| `--vc-date-weekend-color`                                    | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-bg-hover`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-bg`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-edge-bg`                            | rose-100  | slate-700 | slate-300   |
| `--vc-date-weekend-disabled-color`                           | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-today-color`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-today-disabled-color`                     | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-outside-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-weekend-outside-color`                            | slate-400 | slate-600 | gray-400    |
| `--vc-date-weekend-outside-color-hover` <sup>dark only</sup> | —         | slate-300 | —           |
| `--vc-date-weekend-outside-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-outside-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-today-outside-color`                      | slate-400 | slate-400 | gray-400    |
| `--vc-date-weekend-disabled-outside-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-selected-bg`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-selected-color`                           | white     | white     | white       |

### Selected ranges (`multiple-ranged`)

| Variable                               | light           | dark            | slate-light     |
| -------------------------------------- | --------------- | --------------- | --------------- |
| `--vc-date-range-middle-bg`            | cyan-500 at 70% | cyan-500 at 80% | blue-500 at 80% |
| `--vc-date-range-middle-color`         | white           | white           | white           |
| `--vc-date-range-middle-outside-bg`    | slate-200       | slate-800       | slate-200       |
| `--vc-date-range-middle-outside-color` | slate-500       | slate-300       | gray-600        |
| `--vc-date-range-middle-weekend-bg`    | rose-500 at 70% | rose-500 at 80% | red-500 at 80%  |
| `--vc-date-range-middle-weekend-color` | white           | white           | white           |

### Popups & tooltip

| Variable                        | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-date-popup-bg`            | white     | slate-800 | white       |
| `--vc-date-popup-color`         | slate-900 | white     | gray-800    |
| `--vc-date-range-tooltip-bg`    | slate-50  | slate-800 | slate-50    |
| `--vc-date-range-tooltip-color` | slate-500 | slate-400 | slate-500   |

### Time controls

| Variable                                             | light      | dark      | slate-light |
| ---------------------------------------------------- | ---------- | --------- | ----------- |
| `--vc-time-border-color`                             | slate-300  | slate-800 | gray-300    |
| `--vc-time-separator-color`                          | slate-900  | white     | gray-800    |
| `--vc-time-input-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-input-color`                              | slate-900  | white     | gray-800    |
| `--vc-time-input-bg-hover`                           | orange-100 | slate-700 | blue-100    |
| `--vc-time-keeping-color`                            | slate-500  | slate-500 | gray-600    |
| `--vc-time-keeping-color-hover` <sup>dark only</sup> | —          | slate-400 | —           |
| `--vc-time-range-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-range-track-color`                        | slate-300  | slate-600 | slate-300   |
| `--vc-time-range-thumb-bg`                           | white      | slate-800 | slate-100   |
| `--vc-time-range-thumb-border`                       | slate-300  | slate-600 | gray-300    |
| `--vc-time-range-thumb-border-hover`                 | slate-400  | slate-400 | gray-400    |

<Info>
  The three variables marked "dark only" exist because the dark theme has an extra hover state on those elements that the light/slate-light themes don't —
  there's nothing to override in the other themes for those specific variables.
</Info>

```

### `docs/en/reference/utilities.mdx`

```mdx
---
title: Utilities
description: Discover 4 convenient date utilities provided with Vanilla Calendar Pro. These features allow you to format dates, convert them to desired formats, and determine week numbers.
section: 2
---

# Utilities

The calendar comes with its utilities, making it easy to work with date formatting.

There are 4 utilities in total, and they are functions that can be used anywhere in your code, even without the calendar.

1. **`parseDates(dates: string[])`** — Takes an array of date ranges using a delimiter between dates in the string format `FormatDateString ('YYYY-MM-DD')`. Returns an array of dates in the string format `FormatDateString ('YYYY-MM-DD')`.
```ts
import { parseDates } from 'vanilla-calendar-pro/utils';
parseDates(['2024-12-12:2024-12-15']); // return: ['2024-12-12', '2024-12-13', '2024-12-14', '2024-12-15']
```

2. **`getDateString(date: Date)`** — Takes a date of type `Date`. Returns the date in the string format `FormatDateString ('YYYY-MM-DD')`.
```ts
import { getDateString } from 'vanilla-calendar-pro/utils';
getDateString(new Date('24.12.2024')); // return: 2024-12-24
```

3. **`getDate(date: FormatDateString)`** — Takes a date in string format, e.g., `FormatDateString ('YYYY-MM-DD')`. Returns a date of type `Date`.
```ts
import { getDate } from 'vanilla-calendar-pro/utils';
getDate('2024-12-12'); // return: Tue Dec 24 2024 00:00:00 GMT
```

4. **`getWeekNumber(date: FormatDateString, weekStartDay: WeekDayID)`** — Takes a date in string format `FormatDateString ('YYYY-MM-DD')` and the week start day, specifically its `id` of type `number` from 0 to 6. Returns an object `{ year: yearNumber, week: weekNumber }` for the date specified in the arguments.
```ts
import { getWeekNumber } from 'vanilla-calendar-pro/utils';
getWeekNumber('2024-12-12', 1); // return: {year: 2024, week: 50}
```

```

### `docs/ko/learn.mdx`

```mdx
---
title: 소개
description: 페이지 설명
---

# Vanilla Calendar Pro 소개

**Vanilla Calendar Pro**는 날짜와 시간을 다루기 위한 강력하고 유연하며 가벼운 도구로, 웹 애플리케이션이나 웹사이트에서 기능적이고 쉽게 커스터마이징 가능한 캘린더가 필요한 개발자를 위해 만들어졌습니다. 외부 라이브러리에 의존하지 않고 성능이 뛰어나, 캘린더가 필요한 어떤 프로젝트에도 훌륭하게 통합할 수 있습니다.

이 캘린더는 개인 사이트, 기업 포털, 복잡한 웹 애플리케이션 등 다양한 프로젝트를 만드는 개발자를 대상으로 설계되었습니다. Vanilla Calendar Pro는 간단한 날짜 표시 솔루션을 찾는 분들에게도, 시간 선택이나 인터랙티브 액션 같은 고급 기능이 필요한 분들에게도 적합합니다.

## 주요 기능

Vanilla Calendar Pro는 편리하고 적응적인 캘린더 위젯을 만들 수 있도록 풍부한 기능을 제공합니다.

주요 기능은 다음과 같습니다:

- **가벼움**: 최종 JavaScript 파일이 최소화 및 최적화되어 빠르게 로드됩니다.
- **의존성 없음**: 완전히 독립적이며 추가 라이브러리가 필요 없습니다.
- **손쉬운 로컬라이징**: 어떤 언어든 쉽게 로컬라이징할 수 있습니다.
- **커스터마이징 가능**: CSS와 HTML 마크업을 통해 손쉽게 설정할 수 있습니다.
- **다중 인스턴스**: 한 페이지에 제한 없이 여러 캘린더를 사용할 수 있습니다.
- **테마 지원**: 라이트/다크 테마를 자동 전환하고 사용자 지정 테마도 지원합니다.
- **주 시작일 설정**: 주의 시작 요일을 자유롭게 선택할 수 있습니다.
- **주말 설정**: 각 주의 주말을 사용자 지정할 수 있습니다.
- **주 번호 표시**: 연중 주 번호를 표시할 수 있습니다.
- **`<input>`에 종속되지 않음**: 많은 캘린더와 달리 `<input>` 요소에 제한되지 않습니다.
- **접근성**: ARIA 라벨, `tabindex`, 키보드 네비게이션을 제공해 접근성을 강화합니다.
- **날짜 및 시간 범위 선택**: 최소/최대 제한을 포함한 날짜 및 시간 범위 선택을 지원합니다.
- **팝업 및 툴팁**: 선택한 날짜에 대한 정보를 팝업으로 표시하고 날짜 범위 선택에 대한 툴팁을 추가할 수 있습니다.

## Vanilla Calendar Pro 체험하기

아래는 JS 샌드박스에서 실행되는 Vanilla Calendar Pro 라이브 예제입니다. 파라미터를 수정하면 캘린더가 설정에 맞게 즉시 어떻게 바뀌는지 확인할 수 있습니다.

<Sandbox example="installation-and-usage" />

<Info>**이 데모 예제** — 이 섹션의 여러 예제 중 하나 — 는 Vanilla Calendar Pro를 사용하고 원하는 대로 커스터마이징하는 방법을 이해하는 데 도움이 됩니다.</Info>

다음 섹션에서 Vanilla Calendar Pro를 성공적으로 통합하고 설정하는 데 필요한 모든 내용을 확인할 수 있습니다.

```

### `docs/ko/learn/additional-features-animation.mdx`

```mdx
---
title: 애니메이션
new: true
description: 캘린더 뷰 전환의 슬라이드, 크로스페이드, 접기 애니메이션을 설정하는 방법을 알아보세요.
section: 6. 추가 기능
---

# 애니메이션

뷰 사이의 전환에 애니메이션을 적용할 수 있습니다. 화살표 탐색과 스와이프는 가로로 슬라이드되고, 월·연도 선택 화면은 크로스페이드되며, 접기는 월과 주 사이에서 캘린더 높이를 애니메이션합니다.

<Info>
  애니메이션은 하위 호환성을 위해 기본적으로 꺼져 있습니다. 이 옵션은 나중에 추가되었고, 슬라이드와 크로스페이드가 진행되는 동안 DOM 조회 결과가 잠시 달라지기
  때문입니다.
</Info>

<Sandbox example="additional-features-animation" height={400} />

## 모든 전환에 하나의 타이밍

`true` 대신 객체를 전달하면 타이밍을 덮어씁니다. 최상위 값은 모든 전환에 적용됩니다.

<Sandbox example="additional-features-animation-shared" height={400} />

## 전환별 타이밍

세 전환 그룹은 서로 독립적으로 조정할 수 있습니다. 화살표와 스와이프에는 `slide`, 선택 화면에는 `fade`, 월과 주 사이의 접기에는 `collapse` 아래에 값을 중첩하세요. 중첩된 값이 최상위 값보다 우선합니다.

아래 예시에서 슬라이드는 목표 지점을 넘겼다가 돌아오는 곡선을 사용하고, 선택 화면과 접기 컨트롤은 각각 더 차분한 타이밍을 사용합니다.

<Sandbox example="additional-features-animation-custom" height={400} />

<Info>
  방문자가 `prefers-reduced-motion: reduce`로 모션 최소화를 요청한 경우 정착 애니메이션은 실행되지 않습니다. 제스처는 계속 포인터를 따라가며 손을 떼면 즉시
  정착합니다.
</Info>

## 애니메이션 중 캘린더 조회하기

슬라이드와 크로스페이드가 진행되는 동안 사라지는 내용은 `inert`가 지정된 `[data-vc-ghost]` 레이어 안에 남아 있으므로, 그 시간에는 날짜 요소가 두 번 존재할 수 있습니다. `onClickArrow`나 `onClickDate` 같은 콜백은 이 구간 안에서 호출되므로, 콜백에서 캘린더를 조회한다면 이 레이어를 제외하세요. 접기는 고스트 레이어를 만들지 않습니다.

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/ko/learn/additional-features-collapse.mdx`

```mdx
---
title: 접기
new: true
description: 방문자가 한 달을 한 주로 접고 다시 펼칠 수 있게 하는 방법을 알아보세요.
section: 6. 추가 기능
---

# 접기

`enableCollapse`는 그리드 아래에 컨트롤을 추가합니다. 누르면 월이 한 주로 접히고, 다시 누르면 펼쳐집니다. 이 옵션은 기본적으로 꺼져 있으며 `enableSwipe`나 `animation` 없이도 사용할 수 있습니다.

<Sandbox example="additional-features-collapse" height={420} />

컨트롤은 기기에 맞춰 달라집니다. 마우스에서는 셰브론이고, 터치 화면에서는 위아래로 끌 수 있는 그래버가 되며 캘린더가 손가락을 그대로 따라옵니다. 천천히 끌 때는 전체 거리의 4분의 1을 넘어야 하며, 빠르게 튕기면 손을 뗄 때의 속도도 반영되므로 더 일찍 완료될 수 있습니다. 그 밖의 경우에는 원래대로 돌아갑니다.

표시된 월에 속하는 첫 번째 선택 날짜가 있으면 그 날짜를 기준으로 주를 정합니다. 없으면 해당 월에 속하는 오늘을 사용하고, 그마저 없으면 표시된 월의 1일을 기준으로 합니다.

접혀 있는 동안 화살표는 한 번에 한 주씩 이동합니다. 다시 펼치면 그 주를 둘러싼 월로 돌아갑니다.

<Info>접으면 `type`이 `'week'`로 바뀌므로 `calendar.type`으로 현재 상태를 알 수 있고, `set({ type: 'week' })`는 전환 없이 같은 결과를 냅니다. 이 옵션은 `default`와 `week` 타입에서만 받아들여지며, `multiple`과 함께 쓰면 `init()`에서 오류가 발생합니다.</Info>

## 타이밍

전환은 [`animation`](/docs/reference/settings) 옵션을 사용합니다. `collapse` 그룹에서 타이밍을 별도로 설정할 수 있습니다.

```ts
new Calendar('#calendar', {
  animation: { collapse: { duration: 450 } },
  enableCollapse: true,
});
```

<Info>`animation`이 없거나 방문자가 `prefers-reduced-motion: reduce`로 모션 줄이기를 요청해도 끌기는 계속 손가락을 따라가지만, 손을 떼면 즉시 정착합니다.</Info>

```

### `docs/ko/learn/additional-features-layouts.mdx`

```mdx
---
title: 레이아웃
description: 레이아웃을 사용하면 캘린더의 HTML 마크업을 커스터마이징하고 버튼 같은 요소를 추가할 수 있습니다. 캘린더 헤더를 커스터마이징하고 다양한 타입에 요소를 추가하는 방법을 알아보세요.
section: 6. 추가 기능
---

# 레이아웃

캘린더는 `layouts` 파라미터를 통해 HTML 마크업을 편리하게 커스터마이징할 수 있습니다. 이를 통해 버튼이나 다른 HTML 요소를 캘린더에 추가할 수 있습니다.

`layouts`는 캘린더의 `type`을 키로, 문자열을 값으로 받습니다.

다음 예제에서는 `type: 'default'`에 대해 캘린더 헤더를 커스터마이징하고, 캘린더 안에 일반 버튼을 추가합니다.

<Sandbox example="additional-features-layouts" />

이제 `inputMode: true` 파라미터를 사용해 보겠습니다. 클릭 시 캘린더를 숨기는 버튼을 추가합니다.

<Sandbox example="additional-features-layouts-btn-close" input={true} />

```

### `docs/ko/learn/additional-features-popups-and-tooltip.mdx`

```mdx
---
title: 팝업 및 툴팁
description: 캘린더의 특정 날짜에 대한 정보를 팝업으로 표시하고, 날짜 범위 선택 시 툴팁을 사용하는 방법을 알아보세요.
section: 6. 추가 기능
---

# 팝업 및 툴팁

## 팝업

캘린더는 특정 날짜에 대한 정보를 팝업으로 추가할 수 있으며, 해당 날짜에 마우스를 올리면 표시됩니다.

제공된 예제에서는 CSS 모디파이어로 특정 날짜를 강조하고, 팝업에 정보를 추가합니다.

팝업에 대한 추가 정보는 레퍼런스 가이드에서 확인할 수 있습니다.

<Sandbox example="additional-features-popups" />

## 툴팁

툴팁은 `selectionDatesMode` 파라미터가 `'multiple-ranged'`로 설정되어 있을 때 사용할 수 있습니다. `onCreateDateRangeTooltip`를 이용하면 완전히 커스터마이징된 툴팁을 만들 수 있습니다.

<Sandbox example="additional-features-tooltips" />

```

### `docs/ko/learn/additional-features-styles.mdx`

```mdx
---
title: 스타일
description: CSS 클래스를 자신의 값으로 교체하여 캘린더 스타일을 커스터마이징할 수 있습니다. 캘린더의 외형을 변경하는 방법을 알아보세요.
section: 6. 추가 기능
---

# 스타일

캘린더에서 사용되는 모든 CSS 클래스는 변수로 제공되며, 원하는 값으로 교체하여 커스터마이징할 수 있습니다.

<Info>CSS 클래스를 자신의 것으로 교체할 때는, 해당 클래스를 직접 만들고 스타일링해야 한다는 점을 기억하세요.</Info>

아래는 화살표 클래스만 자신의 것으로 교체한 예제입니다. 전체 클래스 목록은 레퍼런스 가이드에서 확인할 수 있습니다.

<Sandbox example="additional-features-styles" />

## CSS 변수

색상만 바꾸고 싶다면 클래스를 재정의할 필요조차 없습니다 — 내장 테마의 모든 색상은 CSS custom property로 노출되어 있으며, 기본값(fallback)은 각 테마의 원래 색상입니다:

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

변수를 명시적으로 설정하기 전까지는 아무것도 바뀌지 않습니다. 전체 변수 목록은 [레퍼런스 가이드](/docs/reference/styles)에서 확인할 수 있습니다.

```

### `docs/ko/learn/additional-features-swipe.mdx`

```mdx
---
title: 스와이프
new: true
description: 방문자가 캘린더를 옆으로 끌어 다음 또는 이전 기간으로 이동하게 하는 방법을 알아보세요.
section: 6. 추가 기능
---

# 스와이프

`enableSwipe`를 켜면 캘린더 콘텐츠를 옆으로 끌 수 있습니다. 이 옵션은 기본적으로 꺼져 있고 `enableCollapse` 및 `animation`과 독립적으로 동작하며, 화살표로 이동할 수 있는 모든 뷰(`default`, `multiple`, `week`, 연도 목록)에서 사용할 수 있습니다. 제스처는 현재 뷰에서 화살표가 움직이는 만큼 이동합니다.

<Sandbox example="additional-features-swipe" height={420} />

이웃한 기간은 제스처가 시작되는 순간 렌더링되어 포인터와 함께 움직이므로, 끄는 동안 빈 공간이 아니라 도착할 곳이 보입니다. 천천히 끌 때는 너비의 4분의 1을 넘어야 하며, 빠르게 튕기면 손을 뗄 때의 속도도 반영되므로 더 일찍 이동할 수 있습니다. 그 밖의 경우에는 되돌아갑니다.

<Info>
  제스처는 가로축만 가져가므로 캘린더 위에서도 페이지는 그대로 세로로 스크롤됩니다. 스와이프는 해당 화살표가 보일 때만 가능하므로 `dateMin`, `dateMax`와 탐색
  제한을 따릅니다. 손을 뗄 때 포인터 아래에 있던 날짜는 선택되지 않습니다.
</Info>

## 타이밍

제스처는 [`animation`](/docs/reference/settings) 옵션의 `slide` 그룹을 사용하므로 화살표 탐색과 같은 타이밍이 적용됩니다.

```ts
new Calendar('#calendar', {
  animation: { slide: { duration: 350 } },
  enableSwipe: true,
});
```

<Info>`animation`이 없거나 방문자가 `prefers-reduced-motion: reduce`로 모션 줄이기를 요청해도 끌기는 계속 포인터를 따라가지만, 손을 떼면 즉시 정착합니다.</Info>

## 제스처 도중 캘린더 조회하기

스와이프는 화살표 애니메이션과 같은 고스트 레이어를 사용합니다. 따라서 진행 중에는 사라지는 기간이 `inert`가 지정된 `[data-vc-ghost]` 요소 안에 남아 있어 날짜 셀이 잠시 두 번 존재합니다. 직접 작성한 코드에서 셀을 순회한다면 이 레이어를 제외하세요.

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/ko/learn/additional-features-themes.mdx`

```mdx
---
title: 테마
description: 캘린더는 커스텀 테마를 지원하며 기본으로 라이트/다크 테마를 제공합니다. 시스템 설정 또는 사용자 지정 테마를 사용하는 방법을 알아보세요.
section: 6. 추가 기능
---

# 테마

캘린더는 커스텀 테마를 지원하며 기본으로 라이트/다크 테마를 제공합니다.

`themeAttrDetect` 파라미터가 `false`로 설정되면, 테마는 사용자의 시스템 설정 또는 `selectedTheme` 파라미터로 결정됩니다.

캘린더는 지정된 태그와 속성을 기준으로 사이트의 테마를 자동 감지하고 추적할 수 있습니다. 이 파라미터에 대한 자세한 내용은 레퍼런스 가이드에서 확인할 수 있습니다.

사이트가 하나의 테마만 지원하거나 캘린더의 외형을 원하는 대로 커스터마이징하려면, 제공되는 테마 중 하나를 명시적으로 선택할 수 있습니다.

아래 예제는 다크 테마를 강제로 사용하는 방법을 보여줍니다:

<Sandbox example="additional-features-themes-dark" themeDetection={false} />

아래는 동일한 예제이지만 라이트 테마를 사용합니다:

<Sandbox example="additional-features-themes-light" themeDetection={false} />

위에서 설명한 것처럼, 직접 만든 테마를 사용하거나 캘린더에 존재하는 테마를 가져와 사용할 수 있습니다.

<Sandbox example="additional-features-themes-slate-light" themeDetection={false} />

```

### `docs/ko/learn/components-for-libraries-angular.mdx`

```mdx
---
title: Angular 컴포넌트
description: Vanilla Calendar Pro를 위한 Angular 컴포넌트를 만들고 사용하는 방법을 알아보세요. 컴포넌트 생성과 Angular 애플리케이션 통합에 대한 상세 가이드입니다.
section: 7. 라이브러리용 컴포넌트
---

# Angular 컴포넌트

<Info>
  이 예제는 Angular 15+ (standalone 컴포넌트) 기준입니다.
</Info>

데모를 위해 Vanilla Calendar Pro용 간단한 Angular 컴포넌트를 만들어 보겠습니다. `vanilla-calendar.component.ts` 파일을 만들고 아래 코드를 붙여넣으세요:

```ts
import { AfterViewInit, Component, ElementRef, Input, ViewChild } from '@angular/core';
import { Calendar, Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

@Component({
  selector: 'vanilla-calendar',
  standalone: true,
  template: `<div #calendarRef></div>`,
})
export class VanillaCalendarComponent implements AfterViewInit {
  @Input() config?: Options;
  @ViewChild('calendarRef') calendarRef!: ElementRef<HTMLDivElement>;

  ngAfterViewInit() {
    const calendar = new Calendar(this.calendarRef.nativeElement, this.config);
    calendar.init();
  }
}
```

그 다음, 캘린더를 표시할 컴포넌트에서 생성한 `VanillaCalendarComponent`를 임포트합니다.

```ts
// ...
import { VanillaCalendarComponent } from './vanilla-calendar.component';
// ...
```

standalone 컴포넌트의 `imports` 배열에 추가하고 템플릿에서 사용하세요.

```ts
@Component({
  // ...
  imports: [VanillaCalendarComponent],
  template: `
    <!-- -->
    <vanilla-calendar />
    <!-- -->
  `,
})
```

`VanillaCalendarComponent`는 `<div>`가 지원하는 모든 HTML 속성(Angular가 자동으로 호스트 엘리먼트에 전달합니다)과 캘린더 설정을 위한 `config` 입력을 받을 수 있습니다.

```ts
template: `
  <!-- -->
  <vanilla-calendar [config]="{ type: 'multiple' }" class="thisIsMyClass" />
  <!-- -->
`,
```

```

### `docs/ko/learn/components-for-libraries-react.mdx`

```mdx
---
title: React 컴포넌트
description: Vanilla Calendar Pro를 위한 React 컴포넌트를 만들고 사용하는 방법을 알아보세요. 컴포넌트 생성과 React 애플리케이션 통합에 대한 상세 가이드입니다.
section: 7. 라이브러리용 컴포넌트
---

# React 컴포넌트

<Info>
  이 예제는 React 16.8+ (Hooks를 사용하는 함수형 컴포넌트) 기준입니다. TypeScript를 사용하지 않는다면 `.tsx` 대신 `.jsx` 확장자를 사용하고, 컴포넌트에서 `CalendarProps` 인터페이스를 제거하세요.
</Info>

데모를 위해 Vanilla Calendar Pro용 가장 단순한 React 컴포넌트를 살펴보겠습니다. `VanillaCalendar.tsx` 파일을 만들고 아래 코드를 붙여넣으세요:

```tsx
import { useEffect, useRef, useState } from 'react';
import { Options, Calendar } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

interface CalendarProps extends React.HTMLAttributes<HTMLDivElement> {
  config?: Options,
}

function VanillaCalendar({ config, ...attributes }: CalendarProps) {
  const ref = useRef(null);
  const [calendar, setCalendar] = useState<Calendar | null>(null);

  useEffect(() => {
    if (!ref.current) return;
    setCalendar(new Calendar(ref.current, config));
  }, [ref, config])

  useEffect(() => {
    if (!calendar) return;
    calendar.init()
  }, [calendar])

  return (
    <div {...attributes} ref={ref}></div>
  )
}

export default VanillaCalendar;
```

그 다음, 캘린더를 표시할 React 애플리케이션 위치에서 생성한 `VanillaCalendar` 컴포넌트를 임포트합니다.

```tsx
import VanillaCalendar from './VanillaCalendar';
```

생성한 컴포넌트를 사용하세요.

```tsx
// ...
<VanillaCalendar />
// ...
```

`VanillaCalendar` 컴포넌트는 `<div>`가 지원하는 모든 HTML 속성과 캘린더 설정을 위한 `config` 파라미터를 받을 수 있습니다.

```tsx
// ...
<VanillaCalendar config={{
    type: 'multiple',
  }} className="thisIsMyClass" />
// ...
```

```

### `docs/ko/learn/components-for-libraries-vue.mdx`

```mdx
---
title: Vue 컴포넌트
description: Vanilla Calendar Pro를 위한 Vue 컴포넌트를 만들고 사용하는 방법을 알아보세요. 컴포넌트 생성과 Vue 애플리케이션 통합에 대한 상세 가이드입니다.
section: 7. 라이브러리용 컴포넌트
---

# Vue 컴포넌트

<Info>
  이 예제는 Vue 3.2+ (`<script setup>`을 사용하는 Composition API) 기준입니다.
</Info>

데모를 위해 Vanilla Calendar Pro용 간단한 Vue 컴포넌트를 만들어 보겠습니다. `VanillaCalendar.vue` 파일을 생성하고 아래 코드를 복사해 넣으세요:

```vue
<script setup lang="ts">
import { onMounted, ref, useAttrs } from 'vue';
import { Calendar, Options } from 'vanilla-calendar-pro';
import 'vanilla-calendar-pro/styles/index.css'

const calendarRef = ref(null);
const attributes = useAttrs();
const { config } = defineProps<{ config?: Options }>();

onMounted(() => {
  if (!calendarRef.value) return;
  const calendar = new Calendar(calendarRef.value, config);
  calendar.init();
});
</script>

<template>
  <div v-bind="attributes" ref="calendarRef"></div>
</template>
```

그 다음, 캘린더를 표시할 Vue 애플리케이션 위치에서 생성한 `VanillaCalendar` 컴포넌트를 임포트합니다.

```vue
<script setup lang="ts">
// ...
import VanillaCalendar from './VanillaCalendar.vue';
// ...
</script>
```

생성한 컴포넌트를 사용하세요.

```vue
<template>
  <!-- -->
  <VanillaCalendar />
  <!-- -->
</template>
```

`VanillaCalendar` 컴포넌트는 `<div>`가 지원하는 모든 HTML 속성과 캘린더 설정을 위한 `config` 파라미터를 받을 수 있습니다.

```vue
<template>
  <!-- -->
  <VanillaCalendar :config="{ type: 'multiple' }" />
  <!-- -->
</template>
```

```

### `docs/ko/learn/components-for-libraries-web-component.mdx`

```mdx
---
title: 웹 컴포넌트
description: Vanilla Calendar Pro를 네이티브 웹 컴포넌트로 감싸는 방법과, 스타일 및 DOM을 완전히 캡슐화하는 선택적 Shadow DOM 방식을 알아보세요.
section: 7. 라이브러리용 컴포넌트
---

# 웹 컴포넌트

<Info>
  웹 컴포넌트는 프레임워크에 종속되지 않는 네이티브 커스텀 HTML 엘리먼트입니다. 한 번 등록하면 어떤 프레임워크에서든, 혹은 순수 HTML에서든 별도의 래퍼 라이브러리 없이 동일하게 동작합니다.
</Info>

## 일반 웹 컴포넌트

데모를 위해 Vanilla Calendar Pro를 감싸는 가장 단순한 네이티브 웹 컴포넌트를 살펴보겠습니다. `VanillaCalendarElement.ts` 파일을 만들고 아래 코드를 붙여넣으세요:

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    this.calendar = new Calendar(this, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

이 커스텀 엘리먼트는 캘린더를 자신의 일반(light) DOM에 직접 렌더링합니다 — 별도의 설정이 필요 없으며, `disconnectedCallback`은 `calendar.destroy()`를 호출하여 커스텀 엘리먼트가 페이지에서 제거될 때마다 캘린더가 스스로 정리되도록 합니다.

등록이 끝나면, 어떤 프레임워크에서든 또는 프레임워크 없이도 HTML 어디에나 커스텀 엘리먼트를 사용할 수 있습니다:

```html
<vanilla-calendar-element></vanilla-calendar-element>
```

## Shadow DOM을 사용하는 웹 컴포넌트

스타일과 DOM을 완전히 캡슐화해야 한다면 — 예를 들어 디자인 시스템 컴포넌트 안에 캘린더를 넣으면서 CSS가 밖으로 새어 나가거나 호스트 페이지와 충돌하지 않게 하려면 — 대신 Shadow DOM을 연결할 수 있습니다. Vanilla Calendar Pro는 Shadow DOM 내부에서의 초기화를 완벽하게 지원합니다: 팝업은 올바른 루트에 추가되고, 클릭과 포커스는 shadow 경계를 기준으로 추적되며, 시스템 테마 리스너는 인스턴스별로 범위가 지정됩니다. 별도의 옵션은 필요하지 않습니다.

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    // the calendar's own CSS has to be loaded inside the shadow root too, since
    // styles in the outer document don't cross the shadow boundary
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css';
    shadow.appendChild(link);

    const container = document.createElement('div');
    shadow.appendChild(container);

    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    // pass the element directly rather than a string selector: a string selector is
    // resolved with document.querySelector, which can't reach inside a Shadow DOM
    this.calendar = new Calendar(container, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

몇 가지 짚고 넘어갈 점:

- 외부 문서에 선언된 스타일은 shadow 경계를 넘지 못하므로, 캘린더의 스타일시트는 shadow root 내부에 직접 추가된 `<link>` 요소로 로드됩니다.
- 컨테이너는 문자열 선택자가 아닌 요소 자체로 `new Calendar(...)`에 전달됩니다: 문자열 선택자는 `document.querySelector`로 해석되는데, 이는 Shadow DOM 내부에 접근할 수 없습니다.

```

### `docs/ko/learn/date-management-date-min-and-max.mdx`

```mdx
---
title: 최소 및 최대 날짜
description: dateMin과 dateMax 파라미터로 캘린더의 날짜 범위를 설정하는 방법을 알아보세요. 최소/최대 날짜를 구성하여 허용 범위를 제한할 수 있습니다.
section: 4. 날짜 및 시간 관리
---

# 최소 및 최대 날짜

캘린더의 날짜 범위는 `dateMin`과 `dateMax` 파라미터로 설정할 수 있습니다. 이 파라미터들은 캘린더에서 허용되는 날짜 범위를 지정합니다.

기본 최소 날짜는 `'1970-01-01'`이며, 이는 <a href="https://en.wikipedia.org/wiki/Unix_time" rel="noopener noreferrer" target="_blank">UNIX 시간</a>의 시작을 의미합니다.
기본 최대 날짜는 `'2470-12-31'`로 설정되어 있으며 임의로 선택된 값입니다.

가능한 날짜 범위를 특정 값으로 제한해야 한다면 `dateMin`과 `dateMax`의 값을 원하는 날짜로 교체하세요. 지정된 범위를 벗어난 날짜는 캘린더에서 처리되지 않습니다.

<Sandbox example="date-management-date-min-and-max" />

```

### `docs/ko/learn/date-management-display-range-dates.mdx`

```mdx
---
title: 표시 날짜 범위
description: displayDateMin 및 displayDateMax 파라미터로 캘린더에 표시할 날짜 범위를 설정하는 방법을 알아보세요. 지정된 범위 내에서 날짜 표시와 선택을 구성할 수 있습니다.
section: 4. 날짜 및 시간 관리
---

# 표시 날짜 범위

`displayDateMin`과 `displayDateMax` 파라미터는 캘린더에 표시할 수 있는 날짜 범위를 정의하지만, 캘린더의 라이프사이클에는 영향을 주지 않습니다. 즉, 표시 및 선택이 허용되는 날짜만 지정합니다.

예를 들어 `displayDisabledDates` 파라미터가 `true`로 설정되어 있으면, 사용자가 볼 수 있는 최소/최대 연도는 `dateMin`과 `dateMax` 파라미터 값으로 결정됩니다.

<Sandbox example="date-management-display-range-dates" />

`displayDisabledDates` 파라미터를 변경하면 캘린더에서 표시 및 선택 가능한 날짜를 제어할 수 있습니다.

```

### `docs/ko/learn/date-management-enable-or-disable-days.mdx`

```mdx
---
title: 날짜 활성화/비활성화
description: 캘린더에서 특정 날짜를 비활성화하거나 활성화하는 방법을 알아보세요. 필요에 따라 선택 가능 여부를 구성할 수 있습니다.
section: 4. 날짜 및 시간 관리
---

# 날짜 활성화/비활성화

선택할 수 없도록 특정 날짜를 비활성화해야 할 때가 있습니다.

<Sandbox example="date-management-disable-dates" />

때로는 비활성 날짜 목록을 나열하는 것보다, 모든 날짜를 비활성화한 다음 특정 날짜만 활성화하는 편이 더 쉬울 수 있습니다.

<Sandbox example="date-management-enable-dates" />

```

### `docs/ko/learn/date-management-enable-time-picker.mdx`

```mdx
---
title: 시간 선택 활성화
description: 캘린더에서 시간 선택을 활성화하고 설정하는 방법을 알아보세요. 12/24시간 형식, 초기 시간 설정, 시간 범위 및 간격을 지원합니다.
section: 4. 날짜 및 시간 관리
---

# 시간 선택 활성화

기본적으로 시간 선택은 비활성화되어 있지만, 필요에 따라 쉽게 활성화하고 설정할 수 있습니다.

## AM/PM이 있는 12시간 형식

12시간 형식을 활성화하고 AM/PM 표시를 추가할 수 있습니다.

<Sandbox example="date-management-enable-time-picker-12" height={400} />

## 24시간 형식

AM/PM 없이 24시간 형식이 필요하다면 아래처럼 설정합니다.

<Sandbox example="date-management-enable-time-picker-24" height={400} />

## 사용자 지정 시간 설정

캘린더 초기화 시 시작 시간을 설정할 수 있습니다. 24시간 형식에서는 AM/PM 표기를 지정할 필요가 없습니다.

<Sandbox example="date-management-enable-time-picker-your-time" height={400} />

## 시간 범위 관리

선택 가능한 시간 범위를 설정할 수 있습니다.

<Sandbox example="date-management-enable-time-picker-range" height={400} />

## 시간 간격 관리

분과 시간의 간격(step)을 설정할 수 있으며, 입력 필드에서 시간을 직접 입력하는 기능을 비활성화할 수도 있습니다.

<Sandbox example="date-management-enable-time-picker-control" height={400} />

```

### `docs/ko/learn/date-management-forbid-choice.mdx`

```mdx
---
title: 날짜/월/연도 선택 비활성화
description: 캘린더에서 날짜, 월 또는 연도를 선택하는 기능을 비활성화하는 방법을 알아보세요. 필요에 맞게 캘린더를 구성할 수 있습니다.
section: 4. 날짜 및 시간 관리
---

# 날짜/월/연도 선택 비활성화

캘린더는 날짜, 월, 연도 선택을 개별적으로 손쉽게 비활성화할 수 있습니다.

<Sandbox example="date-management-forbid-choice" />

```

### `docs/ko/learn/date-management-other-today.mdx`

```mdx
---
title: 사용자 지정 오늘
description: 캘린더에서 오늘로 간주할 다른 날짜를 지정하는 방법을 알아보세요. 필요에 맞게 캘린더를 구성할 수 있습니다.
section: 4. 날짜 및 시간 관리
---

# 사용자 지정 오늘

캘린더는 오늘로 간주할 날짜를 지정할 수 있는 기능을 제공합니다.

<Sandbox example="date-management-other-today" />

```

### `docs/ko/learn/date-management-selected-days-month-year.mdx`

```mdx
---
title: 초기화 시 선택된 날짜, 월, 연도
description: 캘린더 초기화 시 선택된 날짜와 표시할 월/연도를 지정하는 방법을 알아보세요. 필요에 맞게 캘린더를 구성할 수 있습니다.
section: 4. 날짜 및 시간 관리
---

# 초기화 시 선택된 날짜, 월, 연도

캘린더는 초기화 시 선택된 날짜를 명시적으로 지정할 수 있으며, 현재 날짜와 관계없이 표시할 월과 연도를 설정할 수도 있습니다.

특정 날짜를 미리 선택하거나 특정 월/연도를 표시해야 하는 경우에 유용합니다.

<Sandbox example="date-management-selected-days-month-year" />

```

### `docs/ko/learn/handle-click-a-day.mdx`

```mdx
---
title: 날짜 클릭 처리
description: onClickDate() 액션으로 캘린더의 날짜 클릭을 처리하는 방법을 알아보세요. 단일 날짜 또는 날짜 범위 선택을 처리할 수 있습니다.
section: 5. 액션 핸들러
---

# 날짜 클릭 처리

캘린더와의 사용자 상호작용을 위해 여러 액션이 제공되며, 그중 하나가 `onClickDate()`입니다. 이 액션을 사용하면 사용자가 캘린더의 특정 날짜를 클릭했을 때를 추적할 수 있습니다.

선택된 날짜를 콘솔에 출력하는 예제:

<Sandbox example="handle-click-a-day" />

선택된 날짜는 배열로 전달됩니다. 캘린더 파라미터에 따라 단일 날짜뿐 아니라 날짜 범위를 선택할 수 있기 때문입니다.

<Sandbox example="handle-click-a-day-ranged" />

```

### `docs/ko/learn/handle-click-on-a-month-in-the-month-selection.mdx`

```mdx
---
title: 월 목록에서 월 클릭 처리
description: 월 목록에서 월을 클릭했을 때의 처리를 알아보세요. 선택된 월과 인덱스 정보를 얻을 수 있습니다.
section: 5. 액션 핸들러
---

# 월 목록에서 월 클릭 처리

모든 월 목록에서 월을 클릭하면 해당 이벤트를 처리하고 선택된 요소와 인덱스 정보를 얻을 수 있습니다.

<Info>JS 표준에 따라 월은 0부터 번호가 매겨집니다. 즉, 1월은 0, 12월은 11입니다.</Info>

<Sandbox example="handle-click-on-a-month-in-the-month-selection" />

```

### `docs/ko/learn/handle-click-on-the-arrows.mdx`

```mdx
---
title: 화살표 클릭 처리
description: 캘린더에서 월/연도 전환을 위한 화살표 클릭을 처리하는 방법을 알아보세요. 필요에 맞게 이벤트를 구성할 수 있습니다.
section: 5. 액션 핸들러
---

# 화살표 클릭 처리

화살표를 클릭하면 캘린더에서 월 또는 연도를 전환하는 이벤트가 발생합니다. 이 이벤트를 필요에 맞게 사용할 수 있습니다.

<Sandbox example="handle-click-on-the-arrows" />

```

### `docs/ko/learn/handle-click-on-the-year-in-the-year-selection.mdx`

```mdx
---
title: 연도 선택에서 연도 클릭 처리
description: 연도 목록에서 연도를 클릭했을 때의 처리를 알아보세요. 선택된 연도와 번호 정보를 얻을 수 있습니다.
section: 5. 액션 핸들러
---

# 연도 선택에서 연도 클릭 처리

월을 선택하는 것과 마찬가지로, 캘린더의 연도 헤더를 클릭하여 연도를 선택할 수 있습니다.

목록에서 연도를 클릭하면, 클릭된 요소와 연도 값을 가져올 수 있습니다.

<Sandbox example="handle-click-on-the-year-in-the-year-selection" />

```

### `docs/ko/learn/handle-click-on-weekday-and-the-week-number.mdx`

```mdx
---
title: 요일 및 주 번호 클릭 처리
description: 캘린더에서 요일과 주 번호 클릭을 처리하는 방법을 알아보세요. 선택한 요일에 해당하는 월의 모든 날짜를 선택하거나, 선택한 주의 날짜를 선택하도록 이벤트를 구성할 수 있습니다.
section: 5. 액션 핸들러
---

# 요일 및 주 번호 클릭 처리

## 요일

요일 클릭을 가로채서, 예를 들어 해당 요일에 해당하는 월의 모든 날짜를 선택할 수 있습니다.

<Sandbox example="handle-click-on-weekday" />

## 주 번호

`enableWeekNumbers` 파라미터로 캘린더에 주 번호를 표시하고, 해당 번호 클릭을 처리할 수 있습니다. 선택한 주의 날짜 정보를 얻으면 같은 방식으로 손쉽게 선택할 수 있습니다.

<Sandbox example="handle-click-on-the-week-number" />

```

### `docs/ko/learn/handle-get-and-change-every-day.mdx`

```mdx
---
title: 각 날짜 가져오기 및 수정
description: 캘린더의 각 날짜를 가져오고 수정하는 방법을 알아보세요. 다양한 작업을 수행하거나 정보를 추가하거나 변경할 수 있습니다.
section: 5. 액션 핸들러
---

# 각 날짜 가져오기 및 수정

캘린더의 각 날짜에 접근할 수 있다면 다양한 작업을 수행하고, 추가 정보를 넣거나 날짜별로 변경할 수 있습니다.

예를 들어 각 날짜에 임의의 비용이나 값을 추가할 수 있습니다.

<Sandbox example="handle-get-and-change-every-day" height={370} />

```

### `docs/ko/learn/handle-select-and-change-of-time.mdx`

```mdx
---
title: 시간 선택 및 변경 처리
description: 캘린더에서 시간 선택과 변경을 활성화하고 처리하는 방법을 알아보세요. 시간 변경 시마다 데이터를 받을 수 있습니다.
section: 5. 액션 핸들러
---

# 시간 선택 및 변경 처리

`selectionTimeMode` 파라미터를 활성화하면 시간 변경 시마다 필요한 데이터를 자동으로 받을 수 있습니다.

<Sandbox example="handle-select-and-change-of-time" height={400} />

```

### `docs/ko/learn/installation-and-usage.mdx`

```mdx
---
title: 설치 및 사용
description: Vanilla Calendar Pro를 설치하고 사용하는 방법을 알아보세요. 패키지 매니저나 CDN으로 캘린더를 통합하고, 필요에 맞게 설정할 수 있습니다.
section: 1. 시작하기
---

# 설치 및 사용

Vanilla Calendar Pro는 어떤 프로젝트에도 쉽게 통합할 수 있습니다. 의존성과 빌드를 어떻게 관리하는지에 따라 여러 설치 방법이 있습니다.

## 패키지 매니저로 설치

가장 일반적인 방법은 패키지 매니저를 사용하는 것입니다. 이 방법은 Node.js와 최신 빌드 도구를 사용하는 프로젝트에 적합합니다.

1. 패키지를 설치합니다:

```bash
npm install vanilla-calendar-pro
# or
yarn add vanilla-calendar-pro
# or
pnpm add vanilla-calendar-pro
```

2. 문서의 body에 임의의 CSS 셀렉터를 가진 HTML 요소를 만듭니다:

```html
<html>
  <head>
  </head>
  <body>
    <div id="calendar"></div>
  </body>
</html>
```

<Info>이 섹션의 데모에서는 CSS 셀렉터로 `#calendar`를 사용하지만, 원하는 어떤 셀렉터도 만들고 사용할 수 있습니다.</Info>

3. 스크립트를 가져오고, 캘린더 인스턴스를 만든 뒤 JavaScript 또는 TypeScript 파일에서 초기화합니다.

```ts
import { Calendar } from 'vanilla-calendar-pro';

const calendar = new Calendar('#calendar', {
  // Your settings
});
calendar.init();
```

4. 같은 파일에서 스타일을 가져옵니다. `index.css`에는 캘린더의 레이아웃 그리드와 라이트/다크 테마가 포함되어 있습니다.

```ts
import 'vanilla-calendar-pro/styles/index.css';
```

또는 다음처럼 레이아웃과 테마 스타일을 별도로 포함할 수도 있습니다:

```ts
import 'vanilla-calendar-pro/styles/layout.css'; // Only the skeleton
import 'vanilla-calendar-pro/styles/themes/light.css'; // Light theme
import 'vanilla-calendar-pro/styles/themes/dark.css'; // Dark theme
// or any other custom theme...
```

5. 별도의 커스텀 설정 없이 간단히 초기화하는 전체 예제:

<Sandbox example="installation-and-usage" />

<Info>이 예제에서 보셨듯이, 우리는 **«Input»** 필드를 사용하지 않는 플랫 캘린더 뷰를 사용합니다. **«Input»**에 캘린더를 통합하는 방법이 궁금하다면 [이 예제](/docs/learn/type-default#with-input)를 확인하세요.</Info>

## 로컬 또는 CDN

빌드 도구나 패키지 매니저를 쓰지 않고 빠르게 Vanilla Calendar Pro를 통합하려면 CDN을 사용하거나 최신 버전의 <a href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro@latest/package.zip" rel="noopener noreferrer" target="_blank">아카이브를 다운로드</a>하여 로컬에 포함할 수 있습니다.

```html
<html>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/index.js" defer></script>
  </head>
  <body style="display: flex; align-items: start">
    <div id="calendar"></div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        // Destructure the Calendar constructor
        const { Calendar } = window.VanillaCalendarPro;
        // Create a calendar instance and initialize it.
        const calendar = new Calendar('#calendar');
        calendar.init();
      });
    </script>
  </body>
</html>
```

```

### `docs/ko/learn/internationalization-locale.mdx`

```mdx
---
title: 로컬라이징
description: locale 파라미터로 캘린더를 로컬라이징하거나, 월/요일 이름 배열을 제공하여 수동으로 로컬라이징하는 방법을 알아보세요.
section: 3. 국제화
---

# 로컬라이징

<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString" rel="noopener noreferrer" target="_blank">`.toLocaleString()`</a> 메서드에서 지원하는 로케일이라면 `locale` 파라미터에 전달하기만 하면 캘린더가 로컬라이징됩니다.

<Sandbox example="internationalization-locale" />

로케일이 지원되지 않거나 번역이 올바르지 않다면, 언제든지 수동으로 로컬라이징할 수 있습니다. 이 경우 언어 태그 대신 월과 요일 이름 배열을 제공해야 합니다.

<Sandbox example="internationalization-assign-manually" />

```

### `docs/ko/learn/internationalization-week-numbers.mdx`

```mdx
---
title: 주 번호
description: enableWeekNumbers 파라미터를 true로 설정해 캘린더에 주 번호를 표시하는 방법을 알아보세요.
section: 3. 국제화
---

# 주 번호

일부 국가에서는 날짜 표시에 주 번호를 사용합니다.
`enableWeekNumbers` 파라미터를 `true`로 설정하면 캘린더에 주 번호를 표시할 수 있습니다.

<Sandbox example="internationalization-week-numbers" />

```

### `docs/ko/learn/internationalization-weekday-first-and-weekdays.mdx`

```mdx
---
title: 주 시작 요일과 주말
description: 캘린더에서 주 시작 요일과 주말을 설정하는 방법을 알아보세요. ISO 8601 표준을 변경하고 원하는 요일을 주말로 지정하거나 비활성화할 수 있습니다.
section: 3. 국제화
---

# 주 시작 요일과 주말

기본적으로 캘린더는 유럽 표준 **ISO 8601**을 기준으로 합니다. 따라서 주 시작 요일은 월요일입니다.

주 시작 요일과 표시할 주말을 각각 지정하는 파라미터를 사용하면, 어떤 요일이든 주 시작 요일로 지정하고 원하는 요일을 주말로 설정하거나 빈 배열을 지정해 주말 표시를 완전히 비활성화할 수 있습니다.

<Sandbox example="internationalization-weekday-first-and-weekdays" />

```

### `docs/ko/learn/internationalization-weekends-and-holidays.mdx`

```mdx
---
title: 추가 주말 및 공휴일
description: 캘린더에서 추가 주말이나 공휴일을 지정하는 방법을 알아보세요. 수동으로 지정해 빨간색으로 표시할 수 있습니다.
section: 3. 국제화
---

# 추가 주말 및 공휴일

캘린더에서 추가 주말이나 공휴일을 지정하면 해당 날짜가 빨간색으로 표시됩니다. 이러한 날짜는 수동으로 설정해야 합니다.

<Sandbox example="internationalization-weekends-and-holidays" />

```

### `docs/ko/learn/type-default.mdx`

```mdx
---
title: 기본(단일)
description: "'default' 캘린더 타입으로 한 달을 표시하고 날짜를 선택하는 방법을 알아보세요. inputMode 파라미터로 요소 클릭 시 캘린더가 표시되도록 설정할 수 있습니다."
section: 2. 캘린더 타입
---

# 기본(단일)

## 정적

`'default'` 캘린더 타입은 한 달을 표시하고 날짜를 선택할 수 있으며, 화살표로 월을 이동하고 헤더에서 월/연도를 선택할 수 있습니다. 이는 캘린더의 표준 표시 모드입니다.

<Sandbox example="type-default" />

## Input과 함께

**«Input»**을 클릭했을 때 캘린더를 표시해야 한다면, `inputMode: true` 파라미터로 초기화하여 쉽게 설정할 수 있습니다.

<Info>
  이 캘린더에서 **«Input»**은 반드시 `<input>` 태그일 필요가 없습니다. `<div>` 같은 어떤 HTML 요소라도 될 수 있습니다. **«Input»**에서는 모든 타입의 캘린더를 초기화할 수 있습니다.
</Info>

기본적으로 캘린더는 **«Input»** 필드에 어떤 값도 쓰지 않기 때문에, `value`에 무엇을 보여줄지 완전히 제어할 수 있습니다.

<Sandbox example="type-default-in-input" height={470} input={true} />

```

### `docs/ko/learn/type-month.mdx`

```mdx
---
title: 월
description: "'month' 캘린더 타입으로 월 목록을 표시하고 월과 연도를 선택하는 방법을 알아보세요. 사용자의 선택을 월/연도로 제한할 수 있습니다."
section: 2. 캘린더 타입
---

# 월

`'month'` 캘린더 타입은 월 목록을 표시하고, 헤더에서 월과 연도를 선택할 수 있게 합니다. 특정 날짜를 선택하지 못하도록 하고 월과 연도만 선택하게 해야 할 때 유용합니다.

<Sandbox example="type-month" />

```

### `docs/ko/learn/type-multiple.mdx`

```mdx
---
title: 다중
description: "'multiple' 캘린더 타입으로 여러 달을 표시하고 날짜를 선택하는 방법을 알아보세요. selectionDatesMode 파라미터로 날짜 범위 선택을 설정할 수 있습니다."
section: 2. 캘린더 타입
---

# 다중

`'multiple'` 캘린더 타입은 여러 달을 표시하며, 각 달에서 날짜를 선택할 수 있습니다. 서로 다른 달에 걸쳐 여러 날짜를 선택해야 할 때 유용합니다. 이를 위해 `selectionDatesMode` 파라미터를 사용하고 값을 `'multiple'`로 설정합니다.

`'multiple'` 타입 캘린더를 만드는 예제 코드:

<Sandbox example="type-multiple" vertically={false} height={680} />

날짜 범위를 선택해야 한다면 `selectionDatesMode` 파라미터를 `'multiple-ranged'`로 설정할 수 있습니다. 이렇게 하면 개별 날짜 대신 날짜 범위를 선택할 수 있습니다.

<Info>`selectionDatesMode` 파라미터가 `'multiple-ranged'`로 설정되면, 성능 최적화를 위해 선택된 날짜 배열에는 시작 날짜와 종료 날짜만 포함됩니다. `enableEdgeDatesOnly`를 사용하면 이 최적화를 해제하고 선택된 날짜 전체 목록을 받을 수 있습니다.</Info>

<Sandbox example="type-multiple-ranged" vertically={false} height={680} />

```

### `docs/ko/learn/type-week.mdx`

```mdx
---
title: 주
new: true
description: "'week' 캘린더 타입으로 한 달 전체 대신 한 주만 보여 주는 방법과 화살표가 주 단위로 이동하는 방식을 알아보세요."
section: 2. 캘린더 타입
---

# 주

`'week'` 캘린더 타입은 한 달 전체 대신 한 주만 보여 줍니다. 예약 화면처럼 월 그리드가 선택에 필요한 것보다 더 많은 자리를 차지하는 곳에 잘 맞습니다.

스트립은 첫 번째 선택 날짜가 표시된 월에 속할 때 그 날짜가 있는 주에서 열립니다. 그렇지 않으면 오늘이 해당 월에 속할 때 오늘을 사용하고, 마지막으로 `selectedMonth`의 1일이 있는 주를 사용합니다.

<Sandbox example="type-week" height={300} />

화살표는 한 번에 한 주씩 이동하며 달의 경계를 넘어갑니다. 모든 날짜가 현재 기간의 날짜로 렌더링되므로 이전 달이나 다음 달의 날짜처럼 흐려지지 않고, 날짜를 눌러도 스트립이 움직이지 않습니다.

<Info>두 달에 걸친 주는 그 주를 소유한 달, 즉 네 번째 날이 속한 달의 이름으로 표시됩니다. ISO 주 번호를 정하는 규칙과 같습니다.</Info>

## 한 달을 한 주로 접기

`enableCollapse`는 그리드 아래에 월과 주를 전환하는 컨트롤을 추가해, 개발자가 아니라 방문자가 보기를 고르게 합니다. 자세한 내용은 [접기](/docs/learn/additional-features-collapse)를 참고하세요.

같은 컨트롤을 `inputMode`에서도 사용할 수 있습니다. 이 팝업은 주 보기로 열리고, `enableCollapse`로 전체 월을 펼치며, `enableSwipe`로 현재 보기를 넘깁니다.

<Sandbox example="type-week-in-input" height={470} input={true} />

## 코드로 전환하기

접기는 `type`을 바꾸므로, 두 보기를 직접 작성한 코드에서도 오갈 수 있습니다.

```ts
calendar.set({ type: 'week' }); // 한 주로 접기
calendar.set({ type: 'default' }); // 다시 월로
calendar.type; // 접혀 있는 동안에는 'week'
```

<Info>
  이 타입에서 `displayMonthsCount`는 `1`로 유지되며, 여러 주를 나란히 놓는 것은 지원하지 않습니다. 그리드가 여러 개 필요하다면 `type: 'multiple'`을 사용하세요.
</Info>

```

### `docs/ko/learn/type-year.mdx`

```mdx
---
title: 연
description: "'year' 캘린더 타입으로 연도 목록을 표시하고 연도와 월을 선택하는 방법을 알아보세요. 사용자의 선택을 연/월로 제한할 수 있습니다."
section: 2. 캘린더 타입
---

# 연

`'year'` 캘린더 타입은 연도 목록을 표시하여 목록에서 연도를, 해당 헤더에서 월을 선택할 수 있게 합니다. 특정 날짜를 선택하지 못하도록 하고 연도와 월만 선택하게 해야 할 때 유용합니다.

<Sandbox example="type-year" />

```

### `docs/ko/reference.mdx`

```mdx
---
title: 가이드 개요
description: 페이지 설명
---

# 가이드 개요

이 섹션은 **Vanilla Calendar Pro API** 사용에 대한 상세 문서를 제공합니다. 기능 소개가 필요하다면 [«학습»](/docs/learn) 섹션을 확인해 주세요.

Vanilla Calendar Pro API 문서는 다음과 같은 기능별 하위 섹션으로 구성됩니다:

1. **인스턴스 생성** — 캘린더 인스턴스를 생성하는 방법과 위치.
2. **유틸리티** — 날짜 포맷을 도와주는 함수들.
3. **메서드** — 캘린더 인스턴스를 다루기 위한 사용 가능한 메서드.
4. **설정** — 캘린더의 동작과 표시를 변경할 수 있는 모든 옵션.
5. **액션** — 캘린더와의 다양한 상호작용 데이터를 받고 처리하기 위한 이벤트 핸들러.
6. **팝업** — 특정 날짜를 선택하고 그날의 간단한 정보를 캘린더에서 바로(마우스 오버 시) 표시하는 팝업.
7. **레이아웃** — 캘린더의 DOM 구조를 실질적으로 변경하고 커스텀 HTML 요소를 추가할 수 있는 템플릿.
8. **스타일** — 캘린더 스타일링을 위한 CSS 클래스 객체. Tailwind CSS 같은 CSS 프레임워크나 커스텀 클래스를 사용할 수 있습니다.
9. **Aria-라벨** — `aria-label`을 위한 문자열 객체. 모든 캘린더 라벨을 로컬라이징하여 접근성을 보장합니다.

```

### `docs/ko/reference/actions.mdx`

```mdx
---
title: 액션
description: 날짜/주/월/연도/화살표 클릭, 시간 변경, 툴팁 표시 등 캘린더에서 설정할 수 있는 다양한 액션과 이벤트 핸들러를 알아보세요.
section: 5
---

# 액션

## onClickDate()

`Type: Function`

`Default: null`

`Options: onClickDate(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickDate(self, event) {},
});
```

캘린더에서 특정 날짜를 클릭한 뒤 실행됩니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `event` - 마우스 이벤트.

<Info>
  각 날짜 HTML 요소에는 `YYYY-MM-DD` 형식의 전체 날짜를 담은 data 속성이 포함되어 있습니다.
  일, 월, 연도를 별도로 얻고 싶다면 표준 JS 메서드를 사용할 수 있습니다.
  예: `new Date('2022-11-07').getDate()`는 `7`을 반환합니다.
</Info>

---

## onClickWeekDay()

`Type: Function`

`Default: null`

`Options: onClickWeekDay(self, day, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekDay(self, day, dateEls, event) {},
});
```

캘린더에서 요일을 클릭한 뒤 실행됩니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `day` - 요일;
- `dateEls` - 날짜 요소(HTML)의 배열;
- `event` - 마우스 이벤트.

---

## onClickWeekNumber()

`Type: Function`

`Default: null`

`Options: onClickWeekNumber(self, number, year, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekNumber(self, number, year, dateEls, event) {},
});
```

캘린더에서 주 번호를 클릭한 뒤 실행됩니다. 이 메서드가 동작하려면 `enableWeekNumbers` 파라미터가 `true`로 설정되어 있어야 합니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `number` - 주 번호;
- `year` - 해당 주의 연도;
- `dateEls` - 날짜 요소(HTML)의 배열;
- `event` - 마우스 이벤트.

---

## onClickTitle()

`Type: Function`

`Default: null`

`Options: onClickTitle(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickTitle(self, event) {},
});
```

캘린더에서 월 또는 연도 제목을 클릭한 뒤 실행됩니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `event` - 마우스 이벤트.

---

## onClickMonth()

`Type: Function`

`Default: null`

`Options: onClickMonth(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickMonth(self, event) {},
});
```

캘린더에서 월을 선택한 뒤 실행됩니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `event` - 마우스 이벤트.

---

## onClickYear()

`Type: Function`

`Default: null`

`Options: onClickYear(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickYear(self, event) {},
});
```

캘린더에서 연도를 선택한 뒤 실행됩니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `event` - 마우스 이벤트.

---

## onClickArrow()

`Type: Function`

`Default: null`

`Options: onClickArrow(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickArrow(self, event) {},
});
```

캘린더에서 화살표를 클릭한 뒤 실행됩니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `event` - 마우스 이벤트.

---

## onChangeTime()

`Type: Function`

`Default: null`

`Options: onChangeTime(self, event, isError) => void | null`

```ts
new Calendar('#calendar', {
  onChangeTime(self, event) {},
});
```

캘린더에서 시간이 변경된 뒤 실행됩니다. 다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `event` - 변경 이벤트;
- `isError` - 사용자가 잘못된 시간을 입력했으면 `true`를 반환합니다.

---

## onChangeToInput()

`Type: Function`

`Default: null`

`Options: onChangeToInput(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onChangeToInput(self, event) {},
});
```

이 메서드가 동작하려면 `inputMode` 파라미터가 `true`로 설정되어 있어야 합니다.
캘린더에서 날짜를 클릭하거나 어떤 방식으로든 시간이 변경된 뒤 실행됩니다.
다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `event` - 이벤트.

---

## onCreateDateRangeTooltip()

`Type: Function`

`Default: null`

`Options: onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) {},
});
```

날짜 범위 툴팁을 만들 수 있습니다. `selectionDatesMode` 파라미터가 `'multiple-ranged'`로 설정되어 있으면 날짜 클릭 및 호버 시 동작합니다.
다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조.
- `dateEl` - 날짜 HTML 요소;
- `tooltipEl` - 툴팁 HTML 요소;
- `dateElBCR` - 날짜 HTML 요소의 위치 및 크기에 대한 정보 객체;
- `mainElBCR` - 캘린더 메인 HTML 요소의 위치 및 크기에 대한 정보 객체.

---

## onCreateDateEls()

`Type: Function`

`Default: null`

`Options: onCreateDateEls(self, dateEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateEls(self, dateEl) {},
});
```

이 메서드는 캘린더 초기화 및 변경 시점에 실행됩니다. 각 날짜에 대한 정보에 접근할 수 있습니다.
다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `dateEl` - 날짜 HTML 요소.

---

## onCreateMonthEls()

`Type: Function`

`Default: null`

`Options: onCreateMonthEls(self, monthEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateMonthEls(self, monthEl) {},
});
```

이 메서드는 캘린더 타입이 `'month'`로 설정되었을 때 실행됩니다. 사용자가 월 제목을 클릭하거나, `type = 'month'`로 초기화했을 때도 캘린더 타입이 `'month'`가 됩니다. 각 월에 대한 정보에 접근할 수 있습니다.
다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `monthEl` - 월 HTML 요소.

---

## onCreateYearEls()

`Type: Function`

`Default: null`

`Options: onCreateYearEls(self, yearEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateYearEls(self, yearEl) {},
});
```

이 메서드는 캘린더 타입이 `'year'`로 설정되었을 때 실행됩니다. 사용자가 연도 제목을 클릭하거나, `type = 'year'`로 초기화했을 때도 캘린더 타입이 `'year'`가 됩니다. 각 연도에 대한 정보에 접근할 수 있습니다.
다음 파라미터를 받을 수 있습니다:
- `self` - 초기화된 캘린더에 대한 참조;
- `yearEl` - 연도 HTML 요소.

---

## onInit()

`Type: Function`

`Default: null`

`Options: onInit(self) => void | null`

```ts
new Calendar('#calendar', {
  onInit(self) {},
});
```

이 메서드는 캘린더 초기화 시 실행됩니다. `inputMode` 파라미터가 `true`인 경우, 캘린더가 처음 표시될 때 초기화되므로 그 시점에 실행됩니다.
- `self` - 초기화된 캘린더에 대한 참조.

---

## onUpdate()

`Type: Function`

`Default: null`

`Options: onUpdate(self) => void | null`

```ts
new Calendar('#calendar', {
  onUpdate(self) {},
});
```

이 메서드는 `.update()` 메서드로 캘린더를 업데이트/리셋할 때 실행됩니다.
- `self` - 초기화된 캘린더에 대한 참조.

---

## onDestroy()

`Type: Function`

`Default: null`

`Options: onDestroy(self) => void | null`

```ts
new Calendar('#calendar', {
  onDestroy(self) {},
});
```

이 메서드는 캘린더가 삭제될 때 실행됩니다.
- `self` - 초기화된 캘린더에 대한 참조.

---

## onShow()

`Type: Function`

`Default: null`

`Options: onShow(self) => void | null`

```ts
new Calendar('#calendar', {
  onShow(self) {},
});
```

이 메서드는 캘린더가 사용자에게 표시될 때 실행되며, `inputMode` 파라미터가 `true`인 경우에만 동작합니다.
- `self` - 초기화된 캘린더에 대한 참조.

---

## onHide()

`Type: Function`

`Default: null`

`Options: onHide(self) => void | null`

```ts
new Calendar('#calendar', {
  onHide(self) {},
});
```

이 메서드는 캘린더가 숨겨질 때 실행되며, `inputMode` 파라미터가 `true`인 경우에만 동작합니다.
- `self` - 초기화된 캘린더에 대한 참조.

```

### `docs/ko/reference/creating-an-instance.mdx`

```mdx
---
title: 인스턴스 생성
description: CSS 셀렉터 또는 HTML 요소로 Vanilla Calendar Pro 인스턴스를 생성하는 방법을 알아보세요. 요소 클릭 시 래퍼 또는 팝업에서 캘린더가 초기화되도록 설정할 수 있습니다.
section: 1
---

# 인스턴스 생성

`new Calendar()`는 **Vanilla Calendar Pro** 인스턴스를 생성합니다. 이 인스턴스는 캘린더와 그 설정, 메서드를 캡슐화합니다.

<Info>`<script>` 태그로 **Vanilla Calendar Pro**를 포함했다면, 객체는 전역 변수 **window.VanillaCalendarPro**로 사용할 수 있습니다.</Info>

`Calendar` 인스턴스는 두 개의 파라미터를 받습니다. 첫 번째 **필수** 파라미터는 **CSS 셀렉터** 또는 **HTML 요소**일 수 있습니다.

**CSS 셀렉터** 또는 **HTML 요소**는 캘린더가 초기화될 래퍼(컨테이너) 또는 **«Input»**을 의미합니다.

캘린더 래퍼는 캘린더 자체가 초기화될 `<div>` 태그입니다.

캘린더 래퍼에서의 초기화:

```html
<div id="calendar"></div>
```

```ts
new Calendar('#calendar');
// or
const calendarEl = document.querySelector('#calendar');
new Calendar(calendarEl);
```

이 캘린더에서 **«Input»**은 반드시 `<input>` 태그일 필요가 없으며, `<div>` 같은 어떤 HTML 요소라도 될 수 있습니다.

**«Input»**을 클릭하면 캘린더가 포함된 팝업이 표시됩니다.

**«Input»**에서의 초기화:

```html
<input type="text" id="input">
<!-- or -->
<div id="input"></div>
```

```ts
new Calendar('#input', { inputMode: true });
// or
const calendarInput = document.querySelector('#input');
new Calendar(calendarInput, {
  inputMode: true,
});
```

두 번째 **선택** 파라미터는 캘린더의 설정과 액션을 정의하는 객체입니다.

```ts
new Calendar('#calendar', {
  // Settings
});
```

```

### `docs/ko/reference/labels.mdx`

```mdx
---
title: Aria 라벨
description: Aria 라벨을 사용하면 접근성을 위해 캘린더의 모든 aria-label을 로컬라이징할 수 있습니다.
section: 9
---

# Aria 라벨

`labels`는 캘린더의 모든 aria-label을 로컬라이징할 수 있는 기능을 제공합니다.

아래는 모든 기본 aria-label 목록입니다.

```ts
new Calendar('#calendar', {
  labels: {
    application: 'Calendar',
    navigation: 'Calendar Navigation',
    arrowNext: {
      month: 'Next month',
      year: 'Next list of years',
      week: 'Next week',
    },
    arrowPrev: {
      month: 'Previous month',
      year: 'Previous list of years',
      week: 'Previous week',
    },
    month: 'Select month, current selected month:',
    months: 'List of months',
    year: 'Select year, current selected year:',
    years: 'List of years',
    week: 'Days of the week',
    weekNumber: 'Numbers of weeks in a year',
    collapse: 'Collapse to a single week',
    expand: 'Expand to the whole month',
    dates: 'Dates in the current month',
    selectingTime: 'Selecting a time ',
    inputHour: 'Hours',
    inputMinute: 'Minutes',
    rangeHour: 'Slider for selecting hours',
    rangeMinute: 'Slider for selecting minutes',
    btnKeeping: 'Switch AM/PM, current position:',
  },
});
```

```

### `docs/ko/reference/layouts.mdx`

```mdx
---
title: 레이아웃
description: 레이아웃을 사용하면 캘린더의 DOM 구조를 변경하고 자체 HTML 요소를 추가할 수 있습니다.
section: 7
---

# 레이아웃

레이아웃을 사용하면 캘린더의 DOM 구조를 거의 완전히 변경하고, 버튼과 같은 자체 HTML 요소를 추가할 수 있습니다. 각 캘린더 타입에는 기본 템플릿이 있으며, 각각을 커스터마이징할 수 있습니다.

<Info>
  **«#»** 기호를 포함하는 태그는 캘린더의 등록된 컴포넌트이며, 한 달을 감싸는 **\<#Multiple>\<#/Multiple>** 태그를 제외하고는 태그 끝에 닫는 슬래시가 있어야 합니다.
  모든 기본 템플릿에는 해당 템플릿에서 사용 가능한 모든 컴포넌트가 나열되어 있습니다.
</Info>

## layouts.default

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    default: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

한 달과 해당 날짜를 표시하기 위한 기본 템플릿입니다.

---

## layouts.multiple

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    multiple: `
      <div class="${self.styles.controls}" data-vc="controls" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.grid}" data-vc="grid">
        <#Multiple>
          <div class="${self.styles.column}" data-vc="column" role="group">
            <div class="${self.styles.header}" data-vc="header">
              <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
                <#Month />
                <#Year />
              </div>
            </div>
            <div class="${self.styles.wrapper}" data-vc="wrapper">
              <#WeekNumbers />
              <div class="${self.styles.content}" data-vc="content">
                <#Week />
                <#Dates />
              </div>
            </div>
          </div>
        <#/Multiple>
        <#DateRangeTooltip />
      </div>
      <#ControlTime />
    `,
  },
});
```

여러 달과 해당 날짜를 표시하기 위한 기본 템플릿입니다.

---

## layouts.month

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    month: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Months />
        </div>
      </div>
    `,
  },
});
```

월을 선택하기 위한 기본 템플릿입니다.

---

## layouts.year

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    year: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [year] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [year] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Years />
        </div>
      </div>
    `,
  },
});
```

연도를 선택하기 위한 기본 템플릿입니다.

---

## layouts.week

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    week: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [week] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [week] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

한 주를 위한 기본 템플릿입니다. 한 번에 한 주씩 이동하는 화살표를 제외하면 `layouts.default`와 동일합니다.

```

### `docs/ko/reference/methods.mdx`

```mdx
---
title: 메서드
description: 캘린더를 관리하는 메서드로, 초기화, 업데이트, 파라미터 설정, 삭제, 표시/숨김을 포함합니다.
section: 3
---

# 메서드

## init()

`init()` 메서드는 캘린더 초기화 프로세스를 시작하는 주요 인스턴스 메서드입니다.

```ts
const calendar = new Calendar(element, params);
calendar.init();
```

---

## update()

`update()` 메서드는 새로운 설정을 캘린더에 적용하고 리셋을 수행할 수 있습니다.
이 메서드는 리셋 동작을 제어하는 선택적 인자를 가진 객체를 받으며, 기본적으로 업데이트 후 사용자가 선택한 날짜/월/연도를 초기화합니다.

모든 인자의 기본값은 `true`입니다:

```ts
{
  year: boolean;
  month: boolean;
  dates: boolean | 'only-first';
  holidays: boolean;
  time: boolean;
}
```

- `true` - 설정에 지정된 파라미터로 초기화합니다;
- `false` - 리셋을 수행하지 않고 사용자가 선택한 값을 유지합니다;
- `'only-first'` - 선택된 날짜를 모두 초기화하고 가장 빠른 날짜만 남깁니다. 날짜 선택 타입이 `'multiple-ranged'`로 지정되어 있다면, 호버를 위한 `'mousemove'` 및 `'keydown'` 핸들러가 추가됩니다.

사용 예:

```ts
calendar.locale = 'de-AT';
calendar.firstWeekday = 0;

calendar.update({
  dates: true,
});
```

---

## set()

아직 초기화되지 않았거나 이미 초기화된 캘린더에 새로운 파라미터나 핸들러를 지정해야 한다면 `.set()` 메서드를 사용할 수 있습니다.
이 메서드는 새 파라미터 객체와, 리셋을 제어하는 선택적 인자 객체를 받으며, 기본적으로 업데이트 후 사용자가 선택한 날짜/월/연도를 초기화합니다.

사용 예:

```ts
calendar.set({
  locale: 'de-AT',
  firstWeekday: 0,
}, {
  dates: true,
});
```

이 메서드는 캘린더 인스턴스를 생성할 때 파라미터를 지정하는 것의 대안이 될 수 있습니다. 초기화 전에 이 메서드를 호출한다면 리셋 제어 객체를 지정하지 마세요.

```ts
const calendar = new Calendar(element);
calendar.set({ locale: 'de-AT', firstWeekday: 0 });
calendar.init();
```

---

## destroy()

캘린더 인스턴스를 완전히 삭제해야 한다면 `destroy()` 메서드를 사용합니다.

```ts
calendar.destroy();
```

---

## show()

`show()` 메서드는 숨겨진 캘린더를 다시 표시합니다.

```ts
calendar.show();
```

---

## hide()

`hide()` 메서드는 표시 중인 캘린더를 숨깁니다.

```ts
calendar.hide();
```

```

### `docs/ko/reference/popups.mdx`

```mdx
---
title: 팝업
description: 팝업을 사용하면 특정 날짜를 강조하고, 해당 날짜에 마우스를 올렸을 때 캘린더에서 바로 간단한 정보를 표시할 수 있습니다.
section: 6
---

# 팝업

팝업을 사용하면 특정 날짜를 강조하고, 해당 날짜에 마우스를 올렸을 때 캘린더에서 바로 간단한 정보를 표시할 수 있습니다.

## popups['date']

`Type: String`

`Default: null`

`Options: 'YYYY-MM-DD' | 'YYYY-MM-DD:YYYY-MM-DD' | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {},
    '2022-07-01:2022-07-05': {},
  }
});
```

`YYYY-MM-DD` 형식의 날짜가 키로 사용됩니다. 위 예제에서는 2022년 6월 28일에 팝업이 설정됩니다.

<Info>키는 `'YYYY-MM-DD:YYYY-MM-DD'` 형식의 날짜 범위일 수도 있습니다(두 날짜 사이에는 어떤 구분자를 사용해도 됩니다). 이 경우 동일한 팝업(`modifier`/`html`)이 해당 범위의 모든 날짜에 적용되어, 날짜마다 같은 항목을 반복해서 작성할 필요가 없습니다.</Info>

---

## popups['date'].modifier

`Type: String`

`Default: null`

`Options: CSS classes | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
    },
  }
});
```

`modifier`는 공백으로 구분된 임의의 CSS 클래스를 받습니다. 이 클래스를 이용해 날짜를 강조하거나 외형을 변경할 수 있습니다.

---

## popups['date'].html

`Type: String`

`Default: null`

`Options: '' | HTML | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
      html: `<div>
        <u><b>12:00 PM</b></u>
        <p style="margin: 5px 0 0;">Airplane in Las Vegas</p>
      </div>`,
      // or just text
      // html: 'Airplane in Las Vegas',
    },
  }
});
```

`html`은 팝업을 구성하기 위한 평문 또는 HTML 마크업을 받을 수 있습니다.
이 예제에서는 2022년 6월 28일에 마우스를 올리면 "Airplane in Las Vegas" 텍스트와 "12:00 PM" 시간이 표시되며, `bg-red`와 `color-pink` 클래스에 지정된 스타일이 적용됩니다.

```

### `docs/ko/reference/settings.mdx`

```mdx
---
title: 설정
description: 표시 타입, 입력 모드, 위치 지정, 로컬라이징, 날짜와 시간 등 캘린더 설정을 설명합니다.
new:
  - animation
  - enableCollapse
  - enableSwipe
section: 4
---

# 설정

## type

`Type: String`

`Default: 'default'`

`Options: 'default' | 'multiple' | 'month' | 'year' | 'week'`

```ts
new Calendar('#calendar', {
  type: 'default',
});
```

`type` 파라미터는 표시될 캘린더 타입을 정의합니다. `week` 타입은 한 달 전체가 아니라 한 주만 보여 줍니다. 단독으로 사용하거나 `enableCollapse`와 함께 사용해 방문자가 월 보기와 주 보기를 전환하게 할 수 있습니다.

---

## inputMode

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  inputMode: true,
});
```

`inputMode` 파라미터는 첫 번째 파라미터로 전달된 `mainElement`가 캘린더 래퍼가 아니라 입력 필드임을 나타냅니다.

---

## openOnFocus

`Type: Boolean | Function`

`Default: true`

`Options: true | false | () => false`

```ts
new Calendar('#calendar', {
  openOnFocus: false,
  // or with a callback
  openOnFocus: (self) => !self.context.isShowInInputMode,
});
```

`openOnFocus`가 `true`이거나 콜백이 `true`를 반환하면 입력 필드에 포커스가 들어올 때 캘린더가 열립니다. 이 동작을 제어하고 자체 포커스 핸들러를 구현하려면 `false` 또는 콜백을 사용하세요.

---

## positionToInput

`Type: String`

`Default: 'left'`

`Options: 'auto' | 'center' | 'left' | 'right' | ['bottom' | 'top', 'center' | 'left' | 'right']`

```ts
new Calendar('#calendar', {
  positionToInput: 'auto',
  // positionToInput: ['bottom', 'center'],
});
```

캘린더가 `inputMode` 파라미터로 초기화된 경우, 이 파라미터는 입력 필드에 대한 캘린더 위치를 정의합니다.

`positionToInput`은 `'left'`, `'center'`, `'right'` 중 하나의 문자열 또는 `[Y축, X축]` 배열을 받습니다. Y축은 `'bottom'` 또는 `'top'`, X축은 `'left'`, `'center'`, `'right'` 중 하나가 될 수 있습니다.
Y축이 지정되지 않으면 기본값 `'bottom'`이 사용됩니다.

`positionToInput: 'auto'`를 사용하면 뷰포트의 사용 가능한 공간을 기반으로 최적의 위치를 자동 계산합니다.
이 옵션은 4방향의 여유 공간을 계산한 뒤 기본 위치인 입력 필드 아래에 먼저 표시하려고 시도합니다.
아래 공간이 부족하면 다른 최적의 위치를 평가합니다.

---

## animation

`Type: Boolean | Object`

`Default: false`

`Options: true | false | { duration?: Number, easing?: String, slide?: Timing, fade?: Timing, collapse?: Timing }`

`Timing: { duration?: Number, easing?: String }`

```ts
new Calendar('#calendar', {
  animation: true,
  // animation: { duration: 400, easing: 'ease-out' },
  // animation: { slide: { duration: 400 }, fade: { duration: 120 }, collapse: { duration: 300 } },
});
```

뷰 전환에 애니메이션을 적용합니다. 화살표 탐색과 `enableSwipe`는 가로 슬라이드를 사용하고, 월·연도 선택 화면은 크로스페이드되며, `enableCollapse`는 월과 주 사이에서 캘린더 높이를 애니메이션합니다.

기본값은 전환마다 다릅니다. 슬라이드는 `250ms`, 크로스페이드는 `150ms`, 접기는 `300ms`이며 이징은 모두 `cubic-bezier(0.4, 0, 0.2, 1)`입니다. 객체를 전달하면 원하는 값을 덮어씁니다. `duration`은 밀리초 단위이며 `easing`에는 CSS easing 함수를 사용할 수 있습니다. 최상위 값은 모든 전환에 적용되고, `slide`(화살표와 `enableSwipe`), `fade`(선택 화면), `collapse`(`enableCollapse`) 아래에 중첩하면 해당 그룹에만 적용됩니다. 중첩된 값이 최상위 값보다 우선합니다.

<Info>
  방문자가 `prefers-reduced-motion: reduce`로 모션 최소화를 요청한 경우 정착 애니메이션은 실행되지 않습니다. 제스처는 계속 포인터를 따라가지만, 손을 떼면 즉시
  완료되거나 되돌아갑니다.
</Info>

기본값이 `false`인 것은 하위 호환성을 위해서입니다. 이 옵션은 나중에 추가되었고, 켜면 슬라이드와 크로스페이드 중 DOM 조회 결과가 달라집니다. 사라지는 내용은 `inert`가 지정된 `[data-vc-ghost]` 레이어 안에 남아 있어 날짜 요소가 잠시 두 번 존재할 수 있습니다. 직접 작성한 코드에서 날짜 요소를 조회한다면 이 레이어를 제외하세요. 접기는 고스트 레이어를 만들지 않습니다.

---

## firstWeekday

`Type: Number`

`Default: 1`

`Options: from 0 to 6`

```ts
new Calendar('#calendar', {
  firstWeekday: 1,
});
```

이 파라미터는 주의 시작 요일을 설정합니다. 0~6 사이의 숫자를 지정하며, 숫자는 요일 식별자를 의미합니다. JS 표준에 따라 요일은 0부터 시작하며 0은 일요일입니다.

---

## monthsToSwitch

`Type: Number`

`Default: 1`

`Options: from 1 to 12`

```ts
new Calendar('#calendar', {
  monthsToSwitch: 1,
});
```

`monthsToSwitch` 파라미터는 전환할 월의 개수를 제어합니다.

<Info>
  `monthsToSwitch`가 `1`보다 크면, 월 선택(month picker) 화면에서도 현재 선택된 월로부터 `monthsToSwitch` 간격으로 도달 가능한 월만 선택할 수 있으며, 나머지
  월은 비활성화되어 표시됩니다. 이는 설정된 이동 간격과 내비게이션을 일관되게 유지하기 위한 것입니다(특히 `type: 'multiple'`에서 `displayMonthsCount`와 함께
  사용할 때, 여러 개의 표시된 월을 서로 동기화된 상태로 유지하는 데 중요합니다).
</Info>

---

## themeAttrDetect

`Type: String | false`

`Default: 'html[data-theme]'`

`Options: string | false`

```ts
new Calendar('#calendar', {
  themeAttrDetect: 'html[data-theme]',
});
```

캘린더가 사이트 테마를 자동으로 추적하고 적용하도록 하려면, CSS 셀렉터 형태의 문자열 값을 전달할 수 있습니다.
대괄호는 테마 이름이 들어 있는 속성을 의미합니다.
기본적으로 `data-theme` 속성이 있는 `html` 태그를 추적하지만, 예를 들어 클래스 이름으로 테마를 설정하는 경우 `'html[class]'`처럼 다른 속성과 태그로 설정할 수 있습니다.
`false`로 설정하면 테마는 사용자 시스템 또는 `selectedTheme` 파라미터에 의해 결정됩니다.

---

## locale

`Type: String`

`Default: 'en'`

`Options: Language label | Array<locale>`

```ts
new Calendar('#calendar', {
  locale: 'en',
  // Or specify an object for your labels
  // locale: {
  //   months: {
  //     long: [],
  //     short: [],
  //   },
  //   weekday: {
  //     long: [],
  //     short: [],
  //   }
  // },
});
```

이 파라미터는 캘린더의 언어 로컬라이징을 설정합니다.

<a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry" target="_blank" rel="nofollow noreferrer">
  BCP 47
</a>
에 따른 언어 태그를 지정하거나, 월/요일 이름 배열을 제공할 수 있습니다. 자세한 내용은 [여기](/docs/learn/internationalization-locale)를 참고하세요.

---

## dateToday

`Type: Date object`

`Default: 'today'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateToday: 'today',
});
```

`dateToday` 파라미터는 캘린더에서 오늘로 간주할 날짜를 정의합니다.

---

## dateMin

`Type: String`

`Default: '1970-01-01'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMin: '1970-01-01',
});
```

`dateMin` 파라미터는 캘린더에서 허용되는 최소 날짜를 설정하며, 이 날짜보다 이전은 허용되지 않습니다.

---

## dateMax

`Type: String`

`Default: '2470-12-31'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMax: '2470-12-31',
});
```

`dateMax` 파라미터는 캘린더에서 허용되는 최대 날짜를 설정하며, 이 날짜보다 이후는 허용되지 않습니다.

---

## displayDateMin

`Type: String`

`Default: '1970-01-01'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMin: '2022-07-01',
});
```

이 파라미터는 사용자가 선택할 수 있는 최소 날짜를 설정합니다. 지정된 날짜보다 이전 날짜는 비활성화되어 선택할 수 없습니다.

<Info>`displayDateMin`과 `displayDateMax`는 범위 밖의 날짜를 비활성화하지만, `dateMin`과 `dateMax`는 아예 생성하지 않는다는 점에 유의하세요.</Info>

<Info>
  `.set()`에서 `displayDateMin`에 `null`을 전달하면 기본값으로 명시적으로 재설정됩니다. `undefined`를 전달하면(예: 해당 속성을 생략하면) 현재 값이 변경되지 않고
  유지됩니다.
</Info>

---

## displayDateMax

`Type: String`

`Default: '2470-12-31'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMax: '2024-07-01',
});
```

이 파라미터는 사용자가 선택할 수 있는 최대 날짜를 설정합니다. 지정된 날짜보다 이후 날짜는 비활성화되어 선택할 수 없습니다.

<Info>`displayDateMin`과 `displayDateMax`는 범위 밖의 날짜를 비활성화하지만, `dateMin`과 `dateMax`는 아예 생성하지 않는다는 점에 유의하세요.</Info>

<Info>
  `.set()`에서 `displayDateMax`에 `null`을 전달하면 기본값으로 명시적으로 재설정됩니다. `undefined`를 전달하면(예: 해당 속성을 생략하면) 현재 값이 변경되지 않고
  유지됩니다.
</Info>

---

## displayDatesOutside

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  displayDatesOutside: false,
});
```

이 파라미터로 이전/다음 달의 날짜를 표시할지 여부를 결정할 수 있습니다.

---

## displayDisabledDates

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  displayDisabledDates: false,
});
```

이 파라미터는 비활성 날짜를 포함한 모든 날짜를 표시할지 여부를 결정합니다.

---

## displayMonthsCount

`Type: Number`

`Default: 2`

`Options: from 2 to 12`

```ts
new Calendar('#calendar', {
  displayMonthsCount: 2,
});
```

`displayMonthsCount` 파라미터는 캘린더 타입이 `'multiple'`일 때 표시되는 월 수를 정의합니다.

---

## disableDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  disableDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

이 파라미터는 지정한 날짜를 범위와 무관하게 비활성화할 수 있습니다.

<Info>날짜 범위를 지정하려면 하나의 문자열 안에서 날짜 사이에 임의의 구분자를 사용하세요.</Info>

---

## disableAllDates

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableAllDates: true,
});
```

이 파라미터는 모든 날짜를 비활성화하며, `enableDates`와 함께 사용할 때 유용합니다.

---

## disableDatesPast

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableDatesPast: true,
});
```

이 파라미터는 과거의 모든 날짜를 비활성화합니다.

---

## disableDatesGaps

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableDatesGaps: true,
});
```

이 파라미터는 비활성 날짜가 포함된 범위 안에서의 날짜 선택을 막습니다. `selectionDatesMode`가 `'multiple-ranged'`로 설정된 경우에만 동작합니다.

---

## disableWeekdays

`Type: Number`

`Default: []`

`Options: from 0 to 6`

```ts
new Calendar('#calendar', {
  disableWeekdays: [0, 6],
});
```

이 파라미터는 특정 요일을 비활성화할 수 있습니다. 0~6의 숫자를 가진 배열을 지정하며, 숫자는 요일 식별자를 의미합니다. JS 표준에 따라 요일은 0부터 시작하며 0은 일요일입니다.

---

## disableToday

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableToday: true,
});
```

이 파라미터로 오늘 날짜 선택을 비활성화할 수 있습니다.

---

## enableDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  enableDates: ['2022-08-11:2022-08-16', '2022-08-20', 1722152977141, new Date()],
});
```

이 파라미터는 범위와 비활성 날짜 설정과 무관하게 지정한 날짜를 활성화할 수 있습니다.

<Info>날짜 범위를 지정하려면 하나의 문자열 안에서 날짜 사이에 임의의 구분자를 사용하세요.</Info>

---

## enableEdgeDatesOnly

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableEdgeDatesOnly: true,
});
```

이 파라미터는 사용자가 선택한 날짜 중 시작/종료 날짜만 가져오고, 중간 날짜를 무시하도록 합니다. `selectionDatesMode`가 `'multiple-ranged'`로 설정된 경우에만 동작합니다.

<Info>이 파라미터를 사용할 경우 날짜 범위 안의 비활성 날짜는 영향을 주지 않으므로, 시작/종료 날짜만 필요한 경우에만 사용하세요.</Info>

---

## enableDateToggle

`Type: Boolean | Function`

`Default: true`

`Options: true | false | () => false`

```ts
new Calendar('#calendar', {
  enableDateToggle: false,
  // or with a callback
  enableDateToggle: (self) => new Date(self.selectedDates[0]) < new Date(),
});
```

`enableDateToggle`이 `true`이거나 콜백이 `true`를 반환하면, 이미 선택된 날짜를 다시 클릭했을 때 선택이 해제됩니다.

---

## enableWeekNumbers

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableWeekNumbers: true,
});
```

이 파라미터로 연중 주 번호 표시 여부를 결정할 수 있습니다.

---

## enableMonthChangeOnDayClick

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableMonthChangeOnDayClick: false,
});
```

이 파라미터로 이전/다음 달의 날짜를 클릭했을 때 월이 전환될지 여부를 결정할 수 있습니다.

---

## enableJumpToSelectedDate

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableJumpToSelectedDate: true,
  selectedDates: ['2018-05-02'],
});
```

이 옵션이 활성화되어 있고 하나 이상의 선택된 날짜가 지정되었지만 `selectedMonth`와 `selectedYear`를 지정하지 않았다면, 캘린더는 첫 번째 선택된 날짜로 이동합니다. `false`로 설정하면 캘린더는 항상 현재 월/연도로 열립니다.

<Info>이 옵션은 `selectedMonth`와 `selectedYear`가 지정된 경우에는 영향을 주지 않습니다.</Info>

---

## enableCollapse

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableCollapse: true,
});
```

그리드 아래에 월을 한 주로 접거나 다시 펼치는 컨트롤을 추가합니다. 표시된 월에 속하는 첫 번째 선택 날짜가 있으면 그 날짜를 기준으로 하고, 없으면 해당 월에 속하는 오늘, 그마저 없으면 표시된 월의 1일을 기준으로 주를 정합니다. 마우스가 있는 기기에서는 셰브론으로, 터치 기기에서는 위아래로 끌 수 있는 그래버로 표시됩니다.

<Info>`enableCollapse`는 `enableSwipe`나 `animation`을 필요로 하지 않습니다. 접으면 `type`이 `'week'`로 바뀌므로 `calendar.type`으로 현재 상태를 알 수 있고, `set({ type: 'week' })`는 전환 없이 같은 결과를 냅니다. 이 옵션은 `default`와 `week` 유형에서만 지원되며, 다른 유형은 `init()`에서 오류를 발생시킵니다.</Info>

---

## enableSwipe

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableSwipe: true,
});
```

화살표로 이동할 수 있는 모든 뷰(`default`, `multiple`, `week`, 연도 목록)에서 캘린더 콘텐츠를 옆으로 끌어 다음 또는 이전 기간으로 이동할 수 있게 합니다. 이웃한 기간은 포인터를 따라가며, 손을 뗄 때의 거리와 속도에 따라 제자리에 자리 잡거나 원래대로 돌아갑니다.

<Info>
  `enableSwipe`는 `enableCollapse`나 `animation`을 필요로 하지 않으며, 애니메이션이 없으면 손을 뗄 때 즉시 정착합니다. 캘린더 위에서의 세로 스크롤은 페이지에
  맡깁니다. 스와이프는 해당 화살표가 보일 때만 가능하므로 `dateMin`, `dateMax`와 탐색 제한을 따릅니다. 끌기를 끝낸 위치의 날짜는 선택되지 않습니다.
</Info>

---

## selectionDatesMode

`Type: String | false`

`Default: 'single'`

`Options: 'single' | 'multiple' | 'multiple-ranged' | false`

```ts
new Calendar('#calendar', {
  selectionDatesMode: 'single',
});
```

이 파라미터는 단일/다중 날짜 선택을 허용할지, 혹은 날짜 선택을 완전히 비활성화할지 결정합니다.

---

## selectionMonthsMode

`Type: Boolean`

`Default: true`

`Options: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionMonthsMode: false,
});
```

이 파라미터는 월 선택을 비활성화하거나, 화살표로만 월 전환을 허용하거나, 어떤 방식으로든 월 전환을 허용할지 결정합니다.

---

## selectionYearsMode

`Type: Boolean`

`Default: true`

`Options: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionYearsMode: false,
});
```

이 파라미터는 연도 선택을 비활성화하거나, 화살표로만 연도 전환을 허용하거나, 어떤 방식으로든 연도 전환을 허용할지 결정합니다.

---

## selectionTimeMode

`Type: false | Number`

`Default: false`

`Options: false | 24 | 12`

```ts
new Calendar('#calendar', {
  selectionTimeMode: true,
});
```

이 파라미터는 시간 선택을 활성화합니다. 숫자로 24시간 또는 12시간 형식을 지정할 수도 있습니다.

---

## selectedDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  selectedDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

이 파라미터는 캘린더 초기화 시 선택될 날짜 목록을 지정할 수 있습니다.

<Info>날짜 범위를 지정하려면 하나의 문자열 안에서 날짜 사이에 임의의 구분자를 사용하세요.</Info>

---

## selectedMonth

`Type: Number`

`Default: null`

`Options: from 0 to 11 | null`

```ts
new Calendar('#calendar', {
  selectedMonth: 0,
});
```

이 파라미터는 캘린더 초기화 시 표시될 월을 정의합니다. JS 표준에 따라 월은 0~11로 번호가 매겨집니다. 첫 번째 선택된 날짜로 이동하려면 [enableJumpToSelectedDate](/docs/reference/settings#enablejumptoselecteddate)를 참고하세요.

---

## selectedYear

`Type: Number`

`Default: null`

`Options: Number (YYYY) | null`

```ts
new Calendar('#calendar', {
  selectedYear: 2022,
});
```

이 파라미터는 캘린더 초기화 시 표시될 연도를 정의합니다. 첫 번째 선택된 날짜로 이동하려면 [enableJumpToSelectedDate](/docs/reference/settings#enablejumptoselecteddate)를 참고하세요.

---

## selectedHolidays

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  selectedHolidays: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

이 파라미터는 공휴일로 간주될 날짜를 지정하며, 스타일링을 위한 추가 data 속성이 부여됩니다.

<Info>날짜 범위를 지정하려면 하나의 문자열 안에서 날짜 사이에 임의의 구분자를 사용하세요.</Info>

---

## selectedWeekends

`Type: Number`

`Default: [0, 6]`

`Options: number[0-6]`

```ts
new Calendar('#calendar', {
  selectedWeekends: [0, 6],
});
```

이 파라미터는 주말 요일을 지정할 수 있습니다. 0~6의 숫자 배열을 지정하며, 숫자는 요일 식별자를 의미합니다. JS 표준에 따라 요일은 0부터 시작하며 0은 일요일입니다.

---

## selectedTime

`Type: String`

`Default: null`

`Options: 'hh:mm aa' | null`

```ts
new Calendar('#calendar', {
  selectedTime: '03:44 AM',
});
```

이 파라미터는 캘린더 초기화 시 표시될 시간을 설정합니다. 시간은 `'hh:mm aa'` 형식이며, `'aa'`는 AM/PM 표시입니다. 24시간 형식을 사용할 때는 `'aa'` 표시가 필요 없습니다.

---

## selectedTheme

`Type: String`

`Default: 'system'`

`Options: string (custom theme) | 'light' | 'dark' | 'system'`

```ts
new Calendar('#calendar', {
  selectedTheme: 'system',
});
```

이 파라미터는 캘린더의 테마를 정의합니다. 기본적으로 테마는 사용자의 시스템 또는 사이트 설정에 따라 결정됩니다.

---

## timeMinHour

`Type: Number`

`Default: 0`

`Options: from 0 to 23`

```ts
new Calendar('#calendar', {
  timeMinHour: 0,
});
```

이 파라미터는 선택 가능한 최소 시간을 지정합니다.

---

## timeMaxHour

`Type: Number`

`Default: 23`

`Options: from 0 to 23`

```ts
new Calendar('#calendar', {
  timeMaxHour: 23,
});
```

이 파라미터는 선택 가능한 최대 시간을 지정합니다.

---

## timeMinMinute

`Type: Number`

`Default: 0`

`Options: from 0 to 59`

```ts
new Calendar('#calendar', {
  timeMinMinute: 0,
});
```

이 파라미터는 선택 가능한 최소 분을 지정합니다.

---

## timeMaxMinute

`Type: Number`

`Default: 59`

`Options: from 0 to 59`

```ts
new Calendar('#calendar', {
  timeMaxMinute: 59,
});
```

이 파라미터는 선택 가능한 최대 분을 지정합니다.

---

## timeControls

`Type: String`

`Default: 'all'`

`Options: 'all' | 'range'`

```ts
new Calendar('#calendar', {
  timeControls: 'all',
});
```

이 파라미터는 시간 선택 방법을 정의합니다: `'all'`(모든 방법) 또는 `'range'`(컨트롤러만).

---

## timeStepHour

`Type: Number`

`Default: 1`

`Options: from 1 to 23`

```ts
new Calendar('#calendar', {
  timeStepHour: 1,
});
```

이 파라미터는 시간 컨트롤러의 단계(step)를 설정합니다.

---

## timeStepMinute

`Type: Number`

`Default: 1`

`Options: from 1 to 59`

```ts
new Calendar('#calendar', {
  timeStepMinute: 1,
});
```

이 파라미터는 분 컨트롤러의 단계(step)를 설정합니다.

---

## sanitizerHTML

`Type: Function`

`Default: (html) => html`

```ts
import DOMPurify from 'dompurify';

new Calendar('#calendar', {
  sanitizerHTML: (html) => DOMPurify.sanitize(html),
});
```

`sanitizerHTML`은 HTML 템플릿을 정제해 CSP에 안전하도록 만들 수 있습니다.

<Info>
  예제는 서드파티 라이브러리{' '}
  <a href="https://www.npmjs.com/package/dompurify" target="_blank" rel="nofollow noreferrer">
    `dompurify`
  </a>
  를 사용합니다. `sanitizerHTML`은 캘린더 동작에 필수는 아닙니다.
</Info>

```

### `docs/ko/reference/styles.mdx`

```mdx
---
title: 스타일
description: styles 파라미터로 캘린더의 CSS 클래스를 커스터마이징하는 방법과 기본 클래스 목록을 안내합니다.
section: 8
---

# 스타일

`styles`는 캘린더의 어떤 CSS 클래스든 덮어쓸 수 있는 기능을 제공합니다. 각 값을 CSS 클래스 목록으로 교체할 수 있습니다.

아래는 모든 기본 클래스 목록입니다.

## CSS 클래스

```ts
new Calendar('#calendar', {
  styles: {
    // 기본
    calendar: 'vc',
    controls: 'vc-controls',
    grid: 'vc-grid',
    column: 'vc-column',

    // 헤더
    header: 'vc-header',
    headerContent: 'vc-header__content',
    month: 'vc-month',
    year: 'vc-year',
    arrowPrev: 'vc-arrow vc-arrow_prev',
    arrowNext: 'vc-arrow vc-arrow_next',

    // 월 / 연도 선택기
    wrapper: 'vc-wrapper',
    content: 'vc-content',
    months: 'vc-months',
    monthsRow: 'vc-months__row',
    monthsCell: 'vc-months__cell',
    monthsMonth: 'vc-months__month',
    years: 'vc-years',
    yearsRow: 'vc-years__row',
    yearsCell: 'vc-years__cell',
    yearsYear: 'vc-years__year',

    // 주 행 / 주 번호
    week: 'vc-week',
    weekDay: 'vc-week__day',
    weekDayBtn: 'vc-week__day-btn',
    weekNumbers: 'vc-week-numbers',
    weekNumbersTitle: 'vc-week-numbers__title',
    weekNumbersContent: 'vc-week-numbers__content',
    weekNumber: 'vc-week-number',

    // 날짜
    collapse: 'vc-collapse',
    dates: 'vc-dates',
    datesRow: 'vc-dates__row',
    date: 'vc-date',
    dateBtn: 'vc-date__btn',

    // 팝업 및 툴팁
    datePopup: 'vc-date__popup',
    dateRangeTooltip: 'vc-date-range-tooltip',

    // 시간 컨트롤
    time: 'vc-time',
    timeContent: 'vc-time__content',
    timeHour: 'vc-time__hour',
    timeMinute: 'vc-time__minute',
    timeKeeping: 'vc-time__keeping',
    timeRanges: 'vc-time__ranges',
    timeRange: 'vc-time__range',
  },
});
```

---

## CSS 변수

내장 테마(`light`, `dark`, `slate-light`)의 모든 색상은 CSS custom property로 정의되어 있으며, 기본값(fallback)은 각 테마의 원래 색상입니다. 즉, CSS 클래스를 건드리거나 테마 오버라이드가 제대로 적용되길 기다릴 필요 없이 몇 개의 변수만 설정하면 캘린더 스타일을 바꿀 수 있습니다.

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

변수를 설정하지 않으면 캘린더는 이전과 완전히 동일하게 렌더링됩니다 — 변수를 명시적으로 설정하기 전까지는 아무것도 바뀌지 않습니다.

<Info>`:root`에 변수를 설정하면 모든 테마에 한 번에 적용됩니다(light/dark/slate-light 모두 동일한 변수 이름을 사용합니다). 특정 테마 하나만 재정의하려면, 해당 테마의 셀렉터로 범위를 제한하세요. 예: `[data-vc-theme='dark'] { --vc-date-selected-bg: #7c3aed; }`.</Info>

### 기본

| 변수                       | light      | dark       | slate-light |
| -------------------------- | ---------- | ---------- | ----------- |
| `--vc-bg`                  | white      | slate-900  | slate-100   |
| `--vc-color`               | slate-900  | white      | gray-800    |
| `--vc-focus-outline-color` | orange-300 | orange-300 | blue-300    |

### 헤더 / 타이틀

| 변수                        | light     | dark      | slate-light |
| --------------------------- | --------- | --------- | ----------- |
| `--vc-header-color`         | slate-900 | white     | gray-800    |
| `--vc-title-color`          | slate-900 | white     | gray-800    |
| `--vc-title-color-hover`    | slate-500 | slate-500 | gray-600    |
| `--vc-title-color-disabled` | slate-300 | slate-700 | gray-400    |

### 월 / 연도 선택

| 변수                               | light     | dark      | slate-light |
| ---------------------------------- | --------- | --------- | ----------- |
| `--vc-months-years-bg`             | white     | slate-900 | slate-100   |
| `--vc-months-years-color`          | slate-500 | white     | gray-600    |
| `--vc-months-years-bg-hover`       | slate-100 | slate-800 | slate-200   |
| `--vc-months-years-color-disabled` | slate-300 | slate-700 | gray-400    |
| `--vc-months-years-bg-selected`    | cyan-500  | slate-500 | blue-500    |
| `--vc-months-years-color-selected` | white     | white     | white       |

### 접기 컨트롤

| 변수                  | light     | dark      | slate-light |
| --------------------- | --------- | --------- | ----------- |
| `--vc-collapse-color` | slate-300 | slate-600 | slate-300   |

### 요일 행 / 주 번호

| 변수                            | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-week-numbers-title-color` | slate-500 | white     | gray-600    |
| `--vc-week-number-color`        | slate-500 | white     | gray-600    |
| `--vc-week-number-color-hover`  | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-color`           | slate-500 | white     | gray-600    |
| `--vc-week-day-color-hover`     | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-off-color`       | rose-500  | rose-500  | red-500     |
| `--vc-week-day-off-color-hover` | rose-600  | rose-600  | red-600     |

### 날짜

| 변수                                         | light     | dark      | slate-light |
| -------------------------------------------- | --------- | --------- | ----------- |
| `--vc-date-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-color`                            | slate-900 | slate-400 | gray-800    |
| `--vc-date-color-hover` <sup>dark only</sup> | —         | slate-200 | —           |
| `--vc-date-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-edge-bg`                    | slate-200 | slate-700 | slate-300   |
| `--vc-date-disabled-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-outside-color`                    | slate-400 | slate-600 | gray-400    |
| `--vc-date-today-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-today-color`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-today-outside-color`              | slate-500 | slate-600 | gray-600    |
| `--vc-date-selected-bg`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-selected-color`                   | white     | white     | white       |
| `--vc-date-selected-outside-bg`              | slate-300 | slate-700 | slate-300   |
| `--vc-date-selected-outside-color`           | slate-500 | slate-300 | gray-600    |

### 주말 / 공휴일

| 변수                                                         | light     | dark      | slate-light |
| ------------------------------------------------------------ | --------- | --------- | ----------- |
| `--vc-date-weekend-color`                                    | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-bg-hover`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-bg`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-edge-bg`                            | rose-100  | slate-700 | slate-300   |
| `--vc-date-weekend-disabled-color`                           | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-today-color`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-today-disabled-color`                     | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-outside-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-weekend-outside-color`                            | slate-400 | slate-600 | gray-400    |
| `--vc-date-weekend-outside-color-hover` <sup>dark only</sup> | —         | slate-300 | —           |
| `--vc-date-weekend-outside-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-outside-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-today-outside-color`                      | slate-400 | slate-400 | gray-400    |
| `--vc-date-weekend-disabled-outside-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-selected-bg`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-selected-color`                           | white     | white     | white       |

### 선택된 범위 (`multiple-ranged`)

| 변수                                   | light           | dark            | slate-light     |
| -------------------------------------- | --------------- | --------------- | --------------- |
| `--vc-date-range-middle-bg`            | cyan-500 at 70% | cyan-500 at 80% | blue-500 at 80% |
| `--vc-date-range-middle-color`         | white           | white           | white           |
| `--vc-date-range-middle-outside-bg`    | slate-200       | slate-800       | slate-200       |
| `--vc-date-range-middle-outside-color` | slate-500       | slate-300       | gray-600        |
| `--vc-date-range-middle-weekend-bg`    | rose-500 at 70% | rose-500 at 80% | red-500 at 80%  |
| `--vc-date-range-middle-weekend-color` | white           | white           | white           |

### 팝업 & 툴팁

| 변수                            | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-date-popup-bg`            | white     | slate-800 | white       |
| `--vc-date-popup-color`         | slate-900 | white     | gray-800    |
| `--vc-date-range-tooltip-bg`    | slate-50  | slate-800 | slate-50    |
| `--vc-date-range-tooltip-color` | slate-500 | slate-400 | slate-500   |

### 시간 컨트롤

| 변수                                                 | light      | dark      | slate-light |
| ---------------------------------------------------- | ---------- | --------- | ----------- |
| `--vc-time-border-color`                             | slate-300  | slate-800 | gray-300    |
| `--vc-time-separator-color`                          | slate-900  | white     | gray-800    |
| `--vc-time-input-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-input-color`                              | slate-900  | white     | gray-800    |
| `--vc-time-input-bg-hover`                           | orange-100 | slate-700 | blue-100    |
| `--vc-time-keeping-color`                            | slate-500  | slate-500 | gray-600    |
| `--vc-time-keeping-color-hover` <sup>dark only</sup> | —          | slate-400 | —           |
| `--vc-time-range-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-range-track-color`                        | slate-300  | slate-600 | slate-300   |
| `--vc-time-range-thumb-bg`                           | white      | slate-800 | slate-100   |
| `--vc-time-range-thumb-border`                       | slate-300  | slate-600 | gray-300    |
| `--vc-time-range-thumb-border-hover`                 | slate-400  | slate-400 | gray-400    |

<Info>
  "dark only"로 표시된 세 변수는 dark 테마에만 light/slate-light 테마에는 없는 추가 hover 상태가 있기 때문에 존재합니다 — 다른 테마에서는 이 변수들을 재정의할
  대상 자체가 없습니다.
</Info>

```

### `docs/ko/reference/utilities.mdx`

```mdx
---
title: 유틸리티
description: Vanilla Calendar Pro가 제공하는 4가지 유용한 날짜 유틸리티를 알아보세요. 날짜 포맷팅, 변환, 주 번호 계산을 지원합니다.
section: 2
---

# 유틸리티

캘린더에는 날짜 포맷팅을 쉽게 처리할 수 있는 유틸리티가 포함되어 있습니다.

총 4개의 유틸리티가 있으며, 캘린더 없이도 코드 어디에서나 사용할 수 있는 함수들입니다.

1. **`parseDates(dates: string[])`** — `FormatDateString ('YYYY-MM-DD')` 형식의 문자열에서 날짜 사이에 구분자를 사용한 날짜 범위 배열을 받습니다. `FormatDateString ('YYYY-MM-DD')` 형식의 날짜 배열을 반환합니다.
```ts
import { parseDates } from 'vanilla-calendar-pro/utils';
parseDates(['2024-12-12:2024-12-15']); // return: ['2024-12-12', '2024-12-13', '2024-12-14', '2024-12-15']
```

2. **`getDateString(date: Date)`** — `Date` 타입의 날짜를 받습니다. `FormatDateString ('YYYY-MM-DD')` 형식의 문자열을 반환합니다.
```ts
import { getDateString } from 'vanilla-calendar-pro/utils';
getDateString(new Date('24.12.2024')); // return: 2024-12-24
```

3. **`getDate(date: FormatDateString)`** — `FormatDateString ('YYYY-MM-DD')` 형식의 문자열 날짜를 받습니다. `Date` 타입의 날짜를 반환합니다.
```ts
import { getDate } from 'vanilla-calendar-pro/utils';
getDate('2024-12-12'); // return: Tue Dec 24 2024 00:00:00 GMT
```

4. **`getWeekNumber(date: FormatDateString, weekStartDay: WeekDayID)`** — `FormatDateString ('YYYY-MM-DD')` 형식의 문자열 날짜와 주 시작 요일(0~6의 `number` 타입 `id`)을 받습니다. 인자로 전달한 날짜에 대해 `{ year: yearNumber, week: weekNumber }` 객체를 반환합니다.
```ts
import { getWeekNumber } from 'vanilla-calendar-pro/utils';
getWeekNumber('2024-12-12', 1); // return: {year: 2024, week: 50}
```

```

### `docs/ru/learn.mdx`

```mdx
---
title: Введение
description: Vanilla Calendar Pro — мощный и гибкий инструмент для работы с датами и временем. Узнайте о его основных особенностях и возможностях, включая легковесность, отсутствие зависимостей, простую локализацию и настраиваемость.
---

# Введение в Vanilla Calendar Pro

**Vanilla Calendar Pro** — это мощный, гибкий и легкий инструмент для работы с датами и временем, созданный для разработчиков, которым требуется функциональный и легко настраиваемый календарь для веб-приложений или сайтов. Он не зависит от внешних библиотек и имеет высокую производительность, что делает его отличным выбором для интеграции в любые проекты, где требуется календарь.

Этот календарь создан для разработчиков, работающих над разнообразными проектами, будь то личные сайты, корпоративные порталы или сложные веб-приложения. Vanilla Calendar Pro идеально подходит как для тех, кто ищет простое решение для отображения дат, так и для тех, кто требует более сложных функций, таких как выбор времени и поддержки интерактивных действий.

## Основные особенности

Vanilla Calendar Pro предоставляет богатый набор возможностей, которые позволяют создавать удобные и адаптивные календарные виджеты.

Среди ключевых возможностей:

- **Легковесность**: итоговый JavaScript-файл минифицирован и оптимизирован для быстрой загрузки.
- **Отсутствие зависимостей**: полностью автономен, не требует подключения дополнительных библиотек.
- **Простая локализация**: поддерживает легкую локализацию для любого языка.
- **Настраиваемость**: легко конфигурируется с помощью CSS и HTML-разметки.
- **Множество экземпляров**: позволяет размещать неограниченное количество календарей на одной странице.
- **Поддержка тем**: автоматически переключается между светлой и тёмной темами, а также поддерживает пользовательские темы.
- **Настройка начала недели**: позволяет выбрать любой день недели в качестве первого.
- **Настройка выходных**: позволяет задавать индивидуальные выходные дни на каждую неделю.
- **Отображение номеров недель**: можно отображать номера недель на протяжении всего года.
- **Не привязан к `<input>`**: в отличие от многих календарей, не ограничен использованием с элементом `<input>`.
- **Доступность**: включает ARIA-метки, `tabindex` и полную навигацию с клавиатуры, что улучшает доступность.
- **Выбор диапазона дат и времени**: поддерживает выбор диапазонов для дат и времени с минимальными и максимальными ограничениями.
- **Всплывающие окна и подсказки**: позволяет задавать всплывающие окна с пользовательской информацией и добавляет подсказки при выборе диапазонов дат.

## Попробуйте Vanilla Calendar Pro

Ниже представлен рабочий пример Vanilla Calendar Pro в JS песочнице. Вы можете изменить параметры и мгновенно увидеть, как календарь адаптируется под ваши настройки.

<Sandbox example="installation-and-usage" />

<Info>**Данный пример демонстрации** — один из многих, которые будут встречаться в этом разделе. Он поможет вам понять, как использовать Vanilla Calendar Pro и настроить его под свои нужды.</Info>

В следующих разделах вы найдете все необходимое для успешной интеграции и настройки Vanilla Calendar Pro.


```

### `docs/ru/learn/additional-features-animation.mdx`

```mdx
---
title: Анимация
new: true
description: Узнайте, как настраивать слайд, кроссфейд и сворачивание при переходах между представлениями календаря.
section: 6. Дополнительные возможности
---

# Анимация

Переходы между представлениями можно анимировать. Навигация стрелками и свайп едут по горизонтали, пикеры месяца и года используют кроссфейд, а сворачивание анимирует высоту календаря между месяцем и неделей.

<Info>
  По умолчанию анимация выключена ради обратной совместимости: опция появилась позже, а слайд и кроссфейд на короткое время меняют то, что видит поиск по DOM.
</Info>

<Sandbox example="additional-features-animation" height={400} />

## Один тайминг на всё

Объект вместо `true` переопределяет тайминг. Значения верхнего уровня достаются всем переходам.

<Sandbox example="additional-features-animation-shared" height={400} />

## Раздельные тайминги

Три группы переходов можно настроить независимо. Вложите значения в `slide` для стрелок и свайпа, в `fade` для пикеров или в `collapse` для сворачивания месяца до недели. Вложенные значения важнее заданных на верхнем уровне.

В примере ниже у слайда кривая с перелётом, а пикеры и сворачивание используют собственные более спокойные тайминги.

<Sandbox example="additional-features-animation-custom" height={400} />

<Info>
  Анимация завершения не проигрывается, если посетитель запросил уменьшение движения через `prefers-reduced-motion: reduce`. Жесты продолжают следовать за
  указателем и завершаются мгновенно после отпускания.
</Info>

## Поиск по календарю во время анимации

Во время слайда и кроссфейда уходящее содержимое остаётся в DOM внутри слоя `[data-vc-ghost]` с атрибутом `inert`, поэтому элементы дат могут на короткое время присутствовать дважды. Колбэки вроде `onClickArrow` и `onClickDate` вызываются внутри этого окна, так что исключайте слой, если обходите календарь из них. Сворачивание слой-призрак не создаёт.

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/ru/learn/additional-features-collapse.mdx`

```mdx
---
title: Сворачивание
new: true
description: Узнайте, как позволить пользователю свернуть месяц до одной недели и развернуть его обратно.
section: 6. Дополнительные возможности
---

# Сворачивание

`enableCollapse` добавляет под сеткой элемент управления. Клик по нему сворачивает месяц до одной недели, повторный клик разворачивает обратно. По умолчанию опция выключена и не требует `enableSwipe` или `animation`.

<Sandbox example="additional-features-collapse" height={420} />

Элемент подстраивается под устройство. С мышью это шеврон, на сенсорном экране — черточка, которую можно тянуть вверх и вниз, и календарь всё это время едет за пальцем. При медленной тяге нужно пройти четверть пути, а быстрый взмах может завершить переход раньше, потому что учитывается и скорость отпускания. В остальных случаях календарь возвращается назад.

Целевая неделя выбирается по первой выбранной дате, если она относится к отображаемому месяцу. Иначе календарь использует сегодняшний день, если он относится к этому месяцу, а в последнюю очередь — первое число отображаемого месяца.

В свёрнутом виде стрелки листают по одной неделе. При разворачивании календарь показывает месяц вокруг той же недели.

<Info>Сворачивание переключает `type` на `'week'`, поэтому `calendar.type` показывает текущее состояние, а `set({ type: 'week' })` делает то же самое без перехода. Опцию принимают только типы `default` и `week`; вместе с `multiple` она бросает ошибку на `init()`.</Info>

## Тайминги

Переход использует опцию [`animation`](/docs/reference/settings). Его тайминги можно настроить отдельно через группу `collapse`:

```ts
new Calendar('#calendar', {
  animation: { collapse: { duration: 450 } },
  enableCollapse: true,
});
```

<Info>
  Без `animation` или при запросе уменьшения движения через `prefers-reduced-motion: reduce` тяга всё так же следует за пальцем, но отпускание срабатывает
  мгновенно.
</Info>

```

### `docs/ru/learn/additional-features-layouts.mdx`

```mdx
---
title: Макеты
description: Макеты позволяют настраивать HTML-разметку календаря, добавляя собственные элементы, такие как кнопки. Узнайте, как кастомизировать заголовок календаря и добавлять элементы для различных типов календаря.
section: 6. Дополнительные возможности
---

# Макеты

Календарь предоставляет удобную возможность настраивать HTML-разметку с помощью параметра `layouts`. Это позволяет добавить собственные элементы, такие как кнопки или любой другой HTML-элемент, в календарь.

`layouts` принимает `type` календаря в качестве ключа и строку в качестве значения.

В следующем примере заголовок календаря кастомизирован для `type: 'default'`, и внутри календаря добавляется обычная кнопка.

<Sandbox example="additional-features-layouts" />

Теперь используем параметр `inputMode: true`. Добавим кнопку которая будет скрывать календарь при клике на нее.

<Sandbox example="additional-features-layouts-btn-close" input={true} />

```

### `docs/ru/learn/additional-features-popups-and-tooltip.mdx`

```mdx
---
title: Попапы и тултипы
description: Узнайте, как добавлять поп-апы с информацией для любого дня в календаре и использовать тултипы для выбора диапазонов дат.
section: 6. Дополнительные возможности
---

# Попапы и тултипы

## Попапы

Календарь позволяет добавлять поп-апы с информацией для любого дня, которые будут отображаться при наведении на этот день.

В приведенном примере выделен определенный день с использованием CSS-модификатора, и добавлена информация в поп-ап.

Дополнительные детали о поп-апах можно найти в справочнике.

<Sandbox example="additional-features-popups" />

## Тултипы

Тултипы можно использовать, когда для параметра `selectionDatesMode` установлено значение `'multiple-ranged'`. Используя `onCreateDateRangeTooltip`, вы можете создать полностью кастомизированный тултип.

<Sandbox example="additional-features-tooltips" />

```

### `docs/ru/learn/additional-features-styles.mdx`

```mdx
---
title: Стили
description: Настройте стили календаря, заменяя классы CSS своими собственными. Узнайте, как кастомизировать внешний вид календаря.
section: 6. Дополнительные возможности
---

# Стили

Все классы CSS, используемые в календаре, являются переменными, которые можно настроить, заменив их собственными значениями.

<Info>Заменяя классы CSS своими, вы должны иметь в виду, что вам придется самостоятельно создать этот класс в своем CSS и стилизовать его.</Info>

Ниже приведен пример замены класса для стрелок на собственный. Полный список классов можно найти в справочнике.

<Sandbox example="additional-features-styles" />

## CSS-переменные

Если нужно поменять только цвета, переопределять классы вообще не обязательно — каждый цвет во встроенных темах доступен как CSS custom property, с оригинальным цветом темы в качестве значения по умолчанию:

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

Ничего не изменится, пока вы явно не зададите переменную. Полный список переменных доступен в [справочнике](/docs/reference/styles).

```

### `docs/ru/learn/additional-features-swipe.mdx`

```mdx
---
title: Свайп
new: true
description: Узнайте, как позволить пользователю тянуть календарь в сторону для перехода к следующему или предыдущему периоду.
section: 6. Дополнительные возможности
---

# Свайп

`enableSwipe` позволяет тянуть содержимое календаря в сторону. По умолчанию опция выключена, работает независимо от `enableCollapse` и `animation` и может использоваться во всех представлениях, где есть стрелки: `default`, `multiple`, `week` и в списке годов. Жест шагает ровно на столько же, на сколько стрелки в текущем представлении.

<Sandbox example="additional-features-swipe" height={420} />

Соседний период рендерится сразу в начале жеста и едет вместе с указателем, поэтому во время тяги видно, куда календарь придёт, а не пустое место. При медленной тяге нужно пройти четверть ширины, а быстрый взмах может перелистнуть раньше, потому что учитывается и скорость отпускания. В остальных случаях содержимое уезжает обратно.

<Info>
  Жест забирает только горизонтальную ось, поэтому страница над календарём по-прежнему прокручивается вертикально. Свайп доступен, только пока видна
  соответствующая стрелка, поэтому учитывает `dateMin`, `dateMax` и ограничения навигации. Дата под указателем в момент отпускания не выбирается.
</Info>

## Тайминги

Жест использует группу `slide` опции [`animation`](/docs/reference/settings), то есть те же тайминги, что и навигация стрелками:

```ts
new Calendar('#calendar', {
  animation: { slide: { duration: 350 } },
  enableSwipe: true,
});
```

<Info>
  Без `animation` или при запросе уменьшения движения через `prefers-reduced-motion: reduce` тяга всё так же следует за указателем, но отпускание срабатывает
  мгновенно.
</Info>

## Поиск по календарю во время жеста

Свайп опирается на тот же слой-призрак, что и анимация стрелок, поэтому пока он идёт, уходящий период остаётся в DOM внутри элемента `[data-vc-ghost]` с атрибутом `inert`, и ячейки дат на это время присутствуют дважды. Исключайте этот слой, если обходите их из своего кода.

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/ru/learn/additional-features-themes.mdx`

```mdx
---
title: Темы
description: Календарь поддерживает пользовательские темы и по умолчанию имеет светлую и темную тему. Узнайте, как настроить темы и использовать системные настройки или собственные темы.
section: 6. Дополнительные возможности
---

# Темы

Календарь поддерживает пользовательские темы и по умолчанию имеет светлую и темную тему.

Если параметр `themeAttrDetect` установлен на `false`, тема будет определена системными настройками пользователя или параметром `selectedTheme`.

Календарь может автоматически определить и отслеживать тему сайта, исходя из установленного тега и атрибута. Дополнительные сведения об этом параметре можно найти в справочнике.

Если ваш сайт поддерживает только одну тему или вы хотите настроить внешний вид календаря по своему усмотрению, вы можете явно выбрать одну из доступных тем.

Пример ниже демонстрирует принудительное использование темной темы:

<Sandbox example="additional-features-themes-dark" themeDetection={false} />

А вот тот же пример, но с использованием светлой темы:

<Sandbox example="additional-features-themes-light" themeDetection={false} />

Как описано выше, вы можете использовать собственные темы, создавать их самостоятельно или импортировать из календаря, если они существуют.

<Sandbox example="additional-features-themes-slate-light" themeDetection={false} />

```

### `docs/ru/learn/components-for-libraries-angular.mdx`

```mdx
---
title: Angular компонент
description: Узнайте, как создать и использовать Angular компонент для Vanilla Calendar Pro. Подробное руководство по созданию компонента и его интеграции в приложение Angular.
section: 7. Компоненты для библиотек
---

# Angular компонент

<Info>
  Этот пример рассчитан на Angular 15+ (standalone-компоненты).
</Info>

Для демонстрации давайте создадим простой Angular компонент для Vanilla Calendar Pro. Создайте файл с именем `vanilla-calendar.component.ts` и скопируйте в него следующий код:

```ts
import { AfterViewInit, Component, ElementRef, Input, ViewChild } from '@angular/core';
import { Calendar, Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

@Component({
  selector: 'vanilla-calendar',
  standalone: true,
  template: `<div #calendarRef></div>`,
})
export class VanillaCalendarComponent implements AfterViewInit {
  @Input() config?: Options;
  @ViewChild('calendarRef') calendarRef!: ElementRef<HTMLDivElement>;

  ngAfterViewInit() {
    const calendar = new Calendar(this.calendarRef.nativeElement, this.config);
    calendar.init();
  }
}
```

Затем импортируйте созданный компонент `VanillaCalendarComponent` в компонент, где вы планируете отображать календарь.

```ts
// ...
import { VanillaCalendarComponent } from './vanilla-calendar.component';
// ...
```

Добавьте его в массив `imports` standalone-компонента и используйте в шаблоне.

```ts
@Component({
  // ...
  imports: [VanillaCalendarComponent],
  template: `
    <!-- -->
    <vanilla-calendar />
    <!-- -->
  `,
})
```

Компоненту `VanillaCalendarComponent` можно передать любые атрибуты HTML, поддерживаемые тегом `<div>` (Angular автоматически передаёт их на хост-элемент), а также параметр `config` для настройки календаря.

```ts
template: `
  <!-- -->
  <vanilla-calendar [config]="{ type: 'multiple' }" class="thisIsMyClass" />
  <!-- -->
`,
```

```

### `docs/ru/learn/components-for-libraries-react.mdx`

```mdx
---
title: React компонент
description: Узнайте, как создать и использовать React компонент для Vanilla Calendar Pro. Подробное руководство по созданию компонента и его интеграции в приложение React.
section: 7. Компоненты для библиотек
---

# React компонент

<Info>
  Этот пример рассчитан на React 16.8+ (функциональные компоненты с хуками). Если вы не используете TypeScript, используйте расширение `.jsx` вместо `.tsx` и удалите интерфейс `CalendarProps` из компонента.
</Info>

Для демонстрации давайте рассмотрим простейший компонент React для Vanilla Calendar Pro. Создайте файл с именем `VanillaCalendar.tsx` и скопируйте в него следующий код:

```tsx
import { useEffect, useRef, useState } from 'react';
import { Options, Calendar } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

interface CalendarProps extends React.HTMLAttributes<HTMLDivElement> {
  config?: Options,
}

function VanillaCalendar({ config, ...attributes }: CalendarProps) {
  const ref = useRef(null);
  const [calendar, setCalendar] = useState<Calendar | null>(null);

  useEffect(() => {
    if (!ref.current) return;
    setCalendar(new Calendar(ref.current, config));
  }, [ref, config])

  useEffect(() => {
    if (!calendar) return;
    calendar.init()
  }, [calendar])

  return (
    <div {...attributes} ref={ref}></div>
  )
}

export default VanillaCalendar;
```

Затем импортируйте созданный компонент `VanillaCalendar` в ваше приложение React, где вы планируете отображать календарь.

```tsx
import VanillaCalendar from './VanillaCalendar';
```

Используйте созданный компонент.

```tsx
// ...
<VanillaCalendar />
// ...
```

Компоненту `VanillaCalendar` можно передать любые атрибуты HTML, поддерживаемые тегом `<div>`, а также параметр `config` для настройки календаря.

```tsx
// ...
<VanillaCalendar config={{
    type: 'multiple',
  }} className="thisIsMyClass" />
// ...
```

```

### `docs/ru/learn/components-for-libraries-vue.mdx`

```mdx
---
title: Vue компонент
description: Узнайте, как создать и использовать Vue компонент для Vanilla Calendar Pro. Подробное руководство по созданию компонента и его интеграции в приложение Vue.
section: 7. Компоненты для библиотек
---

# Vue компонент

<Info>
  Этот пример рассчитан на Vue 3.2+ (Composition API с `<script setup>`).
</Info>

Для демонстрации давайте рассмотрим простейший компонент Vue для Vanilla Calendar Pro. Создайте файл с именем `VanillaCalendar.vue` и скопируйте в него следующий код:

```vue
<script setup lang="ts">
import { onMounted, ref, useAttrs } from 'vue';
import { Calendar, Options } from 'vanilla-calendar-pro';
import 'vanilla-calendar-pro/styles/index.css'

const calendarRef = ref(null);
const attributes = useAttrs();
const { config } = defineProps<{ config?: Options }>();

onMounted(() => {
  if (!calendarRef.value) return;
  const calendar = new Calendar(calendarRef.value, config);
  calendar.init();
});
</script>

<template>
  <div v-bind="attributes" ref="calendarRef"></div>
</template>
```

Затем импортируйте созданный компонент `VanillaCalendar` в ваше приложение Vue, где вы планируете отображать календарь.

```vue
<script setup lang="ts">
// ...
import VanillaCalendar from './VanillaCalendar.vue';
// ...
</script>
```

Используйте созданный компонент.

```vue
<template>
  <!-- -->
  <VanillaCalendar />
  <!-- -->
</template>
```

Компоненту `VanillaCalendar` можно передать любые атрибуты HTML, поддерживаемые тегом `<div>`, а также параметр `config` для настройки календаря.

```vue
<template>
  <!-- -->
  <VanillaCalendar :config="{ type: 'multiple' }" />
  <!-- -->
</template>
```

```

### `docs/ru/learn/components-for-libraries-web-component.mdx`

```mdx
---
title: Веб-компонент
description: Узнайте, как обернуть Vanilla Calendar Pro в нативный веб-компонент, а также опциональный вариант с Shadow DOM для полной изоляции стилей и DOM.
section: 7. Компоненты для библиотек
---

# Веб-компонент

<Info>
  Веб-компонент — это нативный кастомный HTML-элемент, не привязанный к конкретному фреймворку. После регистрации он одинаково работает в любом фреймворке или в обычном HTML — без обёрточных библиотек.
</Info>

## Обычный веб-компонент

Для демонстрации давайте рассмотрим простейший нативный веб-компонент, оборачивающий Vanilla Calendar Pro. Создайте файл с именем `VanillaCalendarElement.ts` и скопируйте в него следующий код:

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    this.calendar = new Calendar(this, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

Кастомный элемент рендерит календарь прямо в свой собственный (light) DOM — никакой дополнительной настройки не требуется, а `disconnectedCallback` вызывает `calendar.destroy()`, поэтому календарь корректно очищает за собой ресурсы при удалении кастомного элемента со страницы.

После регистрации используйте кастомный элемент где угодно в вашем HTML, в любом фреймворке или вообще без него:

```html
<vanilla-calendar-element></vanilla-calendar-element>
```

## Веб-компонент с Shadow DOM

Если вам нужна полная изоляция стилей и DOM — например, чтобы встроить календарь в компонент дизайн-системы так, чтобы его CSS не «протекал» наружу и не конфликтовал со стилями хост-страницы — можно вместо этого подключить Shadow DOM. Vanilla Calendar Pro полностью поддерживает инициализацию внутри Shadow DOM: всплывающее окно добавляется в правильный корневой узел, клики и фокус отслеживаются относительно границы shadow-дерева, а слушатель системной темы работает отдельно для каждого экземпляра. Никакая специальная опция для этого не требуется.

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    // the calendar's own CSS has to be loaded inside the shadow root too, since
    // styles in the outer document don't cross the shadow boundary
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css';
    shadow.appendChild(link);

    const container = document.createElement('div');
    shadow.appendChild(container);

    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    // pass the element directly rather than a string selector: a string selector is
    // resolved with document.querySelector, which can't reach inside a Shadow DOM
    this.calendar = new Calendar(container, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

Несколько важных моментов:

- Стили календаря подключаются через элемент `<link>`, добавленный прямо внутрь shadow root, поскольку стили, объявленные во внешнем документе, не пересекают границу shadow-дерева.
- Контейнер передаётся в `new Calendar(...)` как элемент, а не как строковый селектор: строковый селектор резолвится через `document.querySelector`, который не может заглянуть внутрь Shadow DOM.

```

### `docs/ru/learn/date-management-date-min-and-max.mdx`

```mdx
---
title: Максимальная и минимальная дата
description: Узнайте, как задать диапазон дат в календаре с помощью параметров dateMin и dateMax. Настройте минимальную и максимальную даты для ограничения допустимого диапазона.
section: 4. Управление датами и временем
---

# Максимальная и минимальная дата

Диапазон дат в календаре можно задать с помощью параметров `dateMin` и `dateMax`. Эти параметры указывают на допустимый диапазон дат в календаре.

По умолчанию минимальной датой является `'1970-01-01'`, что соответствует началу времени <a href="https://ru.wikipedia.org/wiki/Unix_time" rel="noopener noreferrer" target="_blank">UNIX</a>.
Максимальная дата по умолчанию установлена на `'2470-12-31'`, и она выбрана произвольно.

Если вам необходимо задать конкретный диапазон возможных дат, замените значения параметров `dateMin` и `dateMax` на нужные вам даты. Обратите внимание, что календарь не будет обрабатывать даты за пределами указанного диапазона.

<Sandbox example="date-management-date-min-and-max" />

```

### `docs/ru/learn/date-management-display-range-dates.mdx`

```mdx
---
title: Диапазон отображаемых дат
description: Узнайте, как задать диапазон отображаемых дат в календаре с помощью параметров displayDateMin и displayDateMax. Настройте отображение и выбор дат в заданном диапазоне.
section: 4. Управление датами и временем
---

# Диапазон отображаемых дат

Параметры `displayDateMin` и `displayDateMax` определяют диапазон дат, которые можно отображать в календаре, но не влияют на жизненный цикл календаря. Они лишь указывают, какие даты разрешено отображать и выбирать.

Например, если параметр `displayDisabledDates` установлен в значение `true`, то минимальный и максимальный год, доступные для просмотра пользователем, будут определены значениями параметров `dateMin` и `dateMax`.

<Sandbox example="date-management-display-range-dates" />

Изменение параметра `displayDisabledDates` позволяет контролировать доступные для просмотра и выбора даты в календаре.

```

### `docs/ru/learn/date-management-enable-or-disable-days.mdx`

```mdx
---
title: Включить или отключить дни
description: Узнайте, как отключить или включить определенные дни в календаре. Настройте доступность дней для выбора в зависимости от ваших потребностей.
section: 4. Управление датами и временем
---

# Включить или отключить дни

Вам может потребоваться отключить определенные дни, чтобы они не были доступны для выбора.

<Sandbox example="date-management-disable-dates" />

Иногда отключить все дни и включить определенные дни может быть проще, чем указать список отключенных дней.

<Sandbox example="date-management-enable-dates" />

```

### `docs/ru/learn/date-management-enable-time-picker.mdx`

```mdx
---
title: Включить возможность выбора времени
description: Узнайте, как включить и настроить выбор времени в календаре. Поддерживаются 12-часовой и 24-часовой форматы, установка начального времени, управление диапазоном и шагом времени.
section: 4. Управление датами и временем
---

# Включить возможность выбора времени

По умолчанию выбор времени отключен, но можно легко включить его и настроить в соответствии с вашими потребностями.

## 12-часовой день с AM/PM

Вы можете включить 12-часовой формат времени и добавить маркеры AM/PM.

<Sandbox example="date-management-enable-time-picker-12" height={400} />

## 24-часовой день

Если вам нужен 24-часовой формат времени без AM/PM, вы можете настроить его следующим образом.

<Sandbox example="date-management-enable-time-picker-24" height={400} />

## Установка собственного времени

Вы можете установить начальное время при инициализации календаря. Для 24-часового дня маркер AM/PM прописывать не нужно.

<Sandbox example="date-management-enable-time-picker-your-time" height={400} />


## Управление диапазоном времени

Вы можете установить возможный диапазон времени.

<Sandbox example="date-management-enable-time-picker-range" height={400} />


## Управление шагом времени

Помимо всего прочего, вы можете настроить шаг времени для минут и часов. Также можно отключить возможность ручного ввода времени в поле ввода.

<Sandbox example="date-management-enable-time-picker-control" height={400} />

```

### `docs/ru/learn/date-management-forbid-choice.mdx`

```mdx
---
title: Отключить возможность выбора дня, месяца и года
description: Узнайте, как отключить возможность выбора дня, месяца или года в календаре. Настройте календарь в соответствии с вашими потребностями.
section: 4. Управление датами и временем
---

# Отключить возможность выбора дня, месяца и года

Календарь позволяет легко отключить возможность выбора дня, месяца или года по отдельности.

<Sandbox example="date-management-forbid-choice" />

```

### `docs/ru/learn/date-management-other-today.mdx`

```mdx
---
title: Другое сегодня
description: Узнайте, как указать другой день в качестве сегодняшнего в календаре. Настройте календарь в соответствии с вашими потребностями.
section: 4. Управление датами и временем
---

# Другое сегодня

Календарь предоставляет возможность указать, какой день следует считать сегодняшним.

<Sandbox example="date-management-other-today" />

```

### `docs/ru/learn/date-management-selected-days-month-year.mdx`

```mdx
---
title: Выбранные дни, месяц, год при инициализации
description: Узнайте, как указать выбранные дни, месяц и год при инициализации календаря. Настройте календарь в соответствии с вашими потребностями.
section: 4. Управление датами и временем
---

# Выбранные дни, месяц, год при инициализации

Календарь позволяет явно указать выбранные дни при инициализации, а также месяц и год, которые будут отображаться независимо от текущей даты.

Это полезно, если вам необходимо предварительно выбрать определенные даты и установить определенный месяц и год.

<Sandbox example="date-management-selected-days-month-year" />

```

### `docs/ru/learn/handle-click-a-day.mdx`

```mdx
---
title: Обработка клика на день
description: Узнайте, как обрабатывать клики на дни в календаре с помощью действия onClickDate(). Настройте обработку выбора одного дня или диапазона дат.
section: 5. Обработчики действий
---

# Обработка клика на день

Для взаимодействия пользователя с календарем предусмотрены различные действия, одним из которых является `onClickDate()`. Это действие позволяет отслеживать момент, когда пользователь нажимает на конкретный день в календаре.

Пример с выводом выбранного дня в консоль:

<Sandbox example="handle-click-a-day" />

Заметьте, что выбранный день представлен в виде массива, так как пользователь может выбрать не только один день, но и диапазон дат, если это разрешено параметрами календаря.

<Sandbox example="handle-click-a-day-ranged" />

```

### `docs/ru/learn/handle-click-on-a-month-in-the-month-selection.mdx`

```mdx
---
title: Обработка клика на месяц в списке месяцев
description: Узнайте, как обрабатывать клики на месяцы в списке месяцев. Получите информацию о выбранном месяце и его порядковом номере.
section: 5. Обработчики действий
---

# Обработка клика на месяц в списке месяцев

При клике на месяц в списке всех месяцев вы можете обработать это событие и получить информацию о выбранном элементе и его порядковом номере.

<Info>Важно отметить, что по стандартам JS месяцы нумеруются с нуля, где январь соответствует нулевому месяцу, а декабрь - одиннадцатому.</Info>

<Sandbox example="handle-click-on-a-month-in-the-month-selection" />

```

### `docs/ru/learn/handle-click-on-the-arrows.mdx`

```mdx
---
title: Обработка клика на стрелки
description: Узнайте, как обрабатывать клики на стрелки для переключения месяца или года в календаре. Настройте обработку событий в соответствии с вашими потребностями.
section: 5. Обработчики действий
---

# Обработка клика на стрелки

При нажатии на любую из стрелок происходит событие переключения месяца или года в календаре. Это событие может быть использовано в соответствии с вашими потребностями.

<Sandbox example="handle-click-on-the-arrows" />

```

### `docs/ru/learn/handle-click-on-the-year-in-the-year-selection.mdx`

```mdx
---
title: Обработка клика на год в выборе года
description: Узнайте, как обрабатывать клики на год в списке годов. Получите информацию о выбранном годе и его номере.
section: 5. Обработчики действий
---

# Обработка клика на год в выборе года

Как и при выборе месяца, вы можете выбрать год, нажав на заголовок года в календаре.

При клике на год из списка, вы можете получить информацию о выбранном элементе, на который произошел клик, а также номер года.

<Sandbox example="handle-click-on-the-year-in-the-year-selection" />

```

### `docs/ru/learn/handle-click-on-weekday-and-the-week-number.mdx`

```mdx
---
title: Обработка клика на день недели и на номер недели
description: Узнайте, как обрабатывать клики на день недели и на номер недели в календаре. Настройте обработку событий для выбора всех дней месяца, относящихся к выбранному дню недели, или для выбора дат в выбранной неделе.
section: 5. Обработчики действий
---

# Обработка клика на день недели и на номер недели

## День недели

Вы можете перехватить клик по дню недели и, например, выбрать все дни месяца, относящиеся к этому дню недели.

<Sandbox example="handle-click-on-weekday" />

## Номер недели

Вы можете отобразить номера недель в календаре с помощью параметра `enableWeekNumbers` и обработать клики по ним. Имея информацию о датах в выбранной неделе, вы точно так же можете легко выбрать эти даты.

<Sandbox example="handle-click-on-the-week-number" />

```

### `docs/ru/learn/handle-get-and-change-every-day.mdx`

```mdx
---
title: Получение и изменение каждого дня
description: Узнайте, как получать и изменять каждый день в календаре. Выполняйте различные операции, добавляйте дополнительную информацию или вносите изменения в каждый день.
section: 5. Обработчики действий
---

# Получение и изменение каждого дня

При наличии доступа к каждому дню в календаре, вы можете выполнять различные операции, добавлять дополнительную информацию или вносить изменения в каждый день.

В качестве примера, вы можете добавить случайную стоимость или значение к каждому дню.

<Sandbox example="handle-get-and-change-every-day" height={370} />

```

### `docs/ru/learn/handle-select-and-change-of-time.mdx`

```mdx
---
title: Выбор и изменение времени
description: Узнайте, как активировать и обрабатывать выбор и изменение времени в календаре. Получайте данные при каждом изменении времени.
section: 5. Обработчики действий
---

# Выбор и изменение времени

Путем активации параметра `selectionTimeMode`, вы получаете возможность автоматически получать необходимые данные при каждом изменении времени.

<Sandbox example="handle-select-and-change-of-time" height={400} />

```

### `docs/ru/learn/installation-and-usage.mdx`

```mdx
---
title: Установка и использование
description: Узнайте, как установить и использовать Vanilla Calendar Pro. Интегрируйте календарь через пакетный менеджер или CDN, и настройте его в соответствии с вашими потребностями.
section: 1. Начало работы
---

# Установка и использование

Vanilla Calendar Pro легко интегрируется в любые проекты. Существует несколько способов установки, в зависимости от того, как вы предпочитаете управлять зависимостями и сборкой вашего проекта.

## Установка через пакетный менеджер

Самый распространенный способ установки Vanilla Calendar Pro — это использование пакетного менеджера. Этот метод идеально подходит для проектов с использованием Node.js и современных сборщиков.

1. Установите пакет:

```bash
npm install vanilla-calendar-pro
# or
yarn add vanilla-calendar-pro
# or
pnpm add vanilla-calendar-pro
```

2. Создайте HTML-элемент в теле вашего документа с произвольным CSS селектором:

```html
<html>
  <head>
  </head>
  <body>
    <div id="calendar"></div>
  </body>
</html>
```

<Info>В качестве демонстрации в этом разделе мы будем использовать `#calendar` в качестве селектора CSS, но вы можете создать и использовать любой другой селектор.</Info>

3. Импортируйте скрипт, создайте экземпляр календаря и инициализируйте его в вашем JavaScript или TypeScript файле.

```ts
import { Calendar } from 'vanilla-calendar-pro';

const calendar = new Calendar('#calendar', {
  // Ваши настройки
});
calendar.init();
```

4. Импортируйте стили в этом же файле. Файл `index.css` содержит в себе сетку для макета календаря, светлую и темную тему.

```ts
import 'vanilla-calendar-pro/styles/index.css';
```

Вы так же имеете возможность подключить стили для макета календаря и темы отдельно, вот так:

```ts
import 'vanilla-calendar-pro/styles/layout.css'; // Только скелет
import 'vanilla-calendar-pro/styles/themes/light.css'; // Светлая тема
import 'vanilla-calendar-pro/styles/themes/dark.css'; // Темная тема
// или любая другая пользовательская тема...
```

5. Полный пример простой инициализации без каких-либо пользовательских настроек:

<Sandbox example="installation-and-usage" />

<Info>Как вы, возможно, заметили в этом примере, мы используем плоский вид календаря без использования поля ввода **«Input»**, если вас интересует, как можно интегрировать календарь в **«Input»**, посмотрите [этот пример](/ru/docs/learn/type-default#s-input).</Info>

## Локально или CDN

Если вам нужно быстро интегрировать Vanilla Calendar Pro без использования сборщиков или пакетных менеджеров, вы можете подключить его через CDN или <a href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro@latest/package.zip" rel="noopener noreferrer" target="_blank">скачать архив</a> с актуальной версий и подключить локально.

```html
<html>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/index.js" defer></script>
  </head>
  <body style="display: flex; align-items: start">
    <div id="calendar"></div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        // Деструктуризация конструктора Calendar
        const { Calendar } = window.VanillaCalendarPro;
        // Создайте экземпляр календаря и инициализируйте его.
        const calendar = new Calendar('#calendar');
        calendar.init();
      });
    </script>
  </body>
</html>
```

```

### `docs/ru/learn/internationalization-locale.mdx`

```mdx
---
title: Локализация
description: Узнайте, как локализовать календарь с помощью параметра locale или установить локаль вручную, предоставив массивы названий месяцев и недель.
section: 3. Интернационализация
---

# Локализация

Если ваша локаль поддерживается методом <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString" rel="noopener noreferrer" target="_blank">`.toLocaleString()`</a>, вы можете просто передать её в параметр `locale` для локализации календаря.

<Sandbox example="internationalization-locale" />

Если локаль не поддерживается или переведена неправильно, вы всегда можете установить локаль вручную. Для этого вам необходимо предоставить массивы названий месяцев и недель вместо языковой метки.

<Sandbox example="internationalization-assign-manually" />

```

### `docs/ru/learn/internationalization-week-numbers.mdx`

```mdx
---
title: Номера недель
description: Узнайте, как включить отображение номеров недель в календаре, установив параметр enableWeekNumbers в true.
section: 3. Интернационализация
---

# Номера недель

В некоторых странах используют номера недель для обозначения дат.
Вы можете включить отображение номеров недель в календаре, установив параметр `enableWeekNumbers` в `true`.

<Sandbox example="internationalization-week-numbers" />

```

### `docs/ru/learn/internationalization-weekday-first-and-weekdays.mdx`

```mdx
---
title: Первый день недели и выходные
description: Узнайте, как настроить первый день недели и выходные в календаре. Измените стандарт ISO 8601 и назначьте любые дни недели выходными или отключите их.
section: 3. Интернационализация
---

# Первый день недели и выходные

По умолчанию календарь основан на европейском стандарте **ISO 8601**. Это означает, что первый день недели — понедельник.

Используя отдельные параметры для определения первого дня недели и отображаемых выходных, вы можете определить любой день как первый день недели и назначить любые дни недели выходными или полностью отключить их, указав пустой массив.

<Sandbox example="internationalization-weekday-first-and-weekdays" />

```

### `docs/ru/learn/internationalization-weekends-and-holidays.mdx`

```mdx
---
title: Дополнительные выходные и праздники
description: Узнайте, как указать дополнительные выходные и праздничные дни в календаре. Отметьте эти дни красным цветом, установив их вручную.
section: 3. Интернационализация
---

# Дополнительные выходные и праздники

В календаре можно указать дополнительные выходные или праздничные дни, которые будут отмечены красным цветом. Эти дни должны быть установлены вручную.

<Sandbox example="internationalization-weekends-and-holidays" />

```

### `docs/ru/learn/type-default.mdx`

```mdx
---
title: По умолчанию (Одиночный)
description: Узнайте, как использовать тип календаря 'default' для отображения одного месяца и выбора дней. Настройте календарь для отображения при клике на элемент с параметром inputMode.
section: 2. Типы календарей
---

# По умолчанию (Одиночный)

## Статичный

Тип календаря `'default'` отображает один месяц, позволяет выбирать дни, перемещаться между месяцами с помощью стрелок и выбирать месяц и год из соответствующих заголовков. Это стандартный режим отображения календаря.

<Sandbox example="type-default" />

## С Input

Если вам необходимо отображать календарь при клике на **«Input»**, вы можете легко настроить его, инициализировав с параметром `inputMode: true`.

<Info>
  Важно отметить, что **«Input»** в контексте этого календаря не обязательно является тегом `<input>`. Это может быть любой HTML-элемент, например `<div>`. В **«Input»** можно инициализировать любой тип календаря.
</Info>

По умолчанию календарь не записывает никаких значений в поле **«Input»**, что дает вам уникальный контроль над тем, что вы хотите видеть в `value`.

<Sandbox example="type-default-in-input" height={470} input={true} />

```

### `docs/ru/learn/type-month.mdx`

```mdx
---
title: Месяц
description: Узнайте, как использовать тип календаря 'month' для отображения списка месяцев и выбора месяцев и года. Ограничьте выбор пользователя только месяцем и годом.
section: 2. Типы календарей
---

# Месяц

Тип календаря `'month'` отображает список месяцев, и позволяет пользователю выбирать месяцы и год из соответствующих заголовков.
Этот режим полезен, если вам нужно ограничить выбор пользователя только месяцем и годом, без возможности выбора конкретных дней.

<Sandbox example="type-month" />

```

### `docs/ru/learn/type-multiple.mdx`

```mdx
---
title: Несколько
description: Узнайте, как использовать тип календаря 'multiple' для отображения нескольких месяцев и выбора дат. Настройте выбор диапазонов дат с параметром selectionDatesMode.
section: 2. Типы календарей
---

# Несколько

Тип календаря `'multiple'` отображает несколько месяцев, позволяя выбирать дни в каждом из них.
Этот тип календаря полезен, когда пользователю нужно выбирать несколько дат в разных месяцах, но для этого вам необходимо использовать параметр `selectionDatesMode` и установить его значение на `'multiple'`.

Пример кода для создания календаря с типом `'multiple'`:

<Sandbox example="type-multiple" vertically={false} height={680} />

Если вам нужно выбирать диапазоны дат, вы можете использовать параметр `selectionDatesMode` и установить его значение на `'multiple-ranged'`. Это позволит вам выбирать диапазоны дат, а не только отдельные дни.

<Info>Когда для параметра `selectionDatesMode` установлено значение `'multiple-ranged'`, для оптимизации производительности календаря массив выбранных дат содержит только дату начала и окончания. Вы можете отключить это и получить полный список выбранных дат, используя `enableEdgeDatesOnly`.</Info>

<Sandbox example="type-multiple-ranged" vertically={false} height={680} />

```

### `docs/ru/learn/type-week.mdx`

```mdx
---
title: Неделя
new: true
description: Узнайте, как использовать тип календаря 'week', чтобы показывать одну неделю вместо целого месяца, и как стрелки листают недели.
section: 2. Типы календарей
---

# Неделя

Тип календаря `'week'` показывает одну неделю вместо целого месяца. Он подходит для записи на приём и любых экранов, где сетка месяца занимает больше места, чем того стоит выбор.

Полоса открывается на неделе с первой выбранной датой, если эта дата относится к отображаемому месяцу. Иначе берётся сегодняшний день, если он относится к этому месяцу, а в последнюю очередь — неделя с первым днём `selectedMonth`.

<Sandbox example="type-week" height={300} />

Стрелки листают по одной неделе и переносят полосу через границы месяцев. Все дни рендерятся как дни текущего периода, поэтому ничего не гасится как дата вне месяца, а клик по дню никогда не сдвигает полосу.

<Info>
  Неделя на стыке двух месяцев подписывается тем месяцем, которому принадлежит, — тем, где лежит её четвёртый день. По тому же правилу определяется её номер по
  ISO.
</Info>

## Сворачивание месяца до недели

`enableCollapse` добавляет под сеткой элемент управления, который переключает месяц и неделю, — представление выбирает посетитель, а не вы. Подробности в разделе [Сворачивание](/docs/learn/additional-features-collapse).

Те же элементы управления работают в `inputMode`. Этот попап открывается в режиме недели, раскрывается до полного месяца с помощью `enableCollapse` и листает текущее представление с помощью `enableSwipe`:

<Sandbox example="type-week-in-input" height={470} input={true} />

## Программное переключение

Сворачивание задаёт `type`, поэтому оба представления доступны и из вашего кода:

```ts
calendar.set({ type: 'week' }); // свернуть до недели
calendar.set({ type: 'default' }); // обратно к месяцу
calendar.type; // 'week', пока календарь свёрнут
```

<Info>
  `displayMonthsCount` для этого типа остаётся равным `1`, несколько недель рядом не поддерживаются. Если нужно больше одной сетки, используйте `type:
  'multiple'`.
</Info>

```

### `docs/ru/learn/type-year.mdx`

```mdx
---
title: Год
description: Узнайте, как использовать тип календаря 'year' для отображения списка лет и выбора года и месяца. Ограничьте выбор пользователя только годом и месяцем.
section: 2. Типы календарей
---

# Год

Тип календаря `'year'` отображает список лет, позволяя пользователю выбирать год из списка, и выбирать месяц из соответствующего заголовка.
Этот режим полезен, если вам необходимо ограничить выбор пользователю только годом и месяцем, и исключить возможность выбора конкретных дней.

<Sandbox example="type-year" />

```

### `docs/ru/reference.mdx`

```mdx
---
title: Обзор справочника
description: Обзор справочника по API Vanilla Calendar Pro. Узнайте, как создать экземпляр календаря, использовать методы, настройки, обработчики событий, попапы, макеты, стили и aria-подписи.
---

# Обзор справочника

В этом разделе представлена подробная документация по работе с **API Vanilla Calendar Pro**. Если вы ищете введение в возможности, пожалуйста, ознакомьтесь с разделом [«Изучать»](/ru/docs/learn).

Документация API Vanilla Calendar Pro разделена на несколько функциональных подразделов:

1. **Создание экземпляра** — как и где создать экземпляр календаря.
2. **Утилиты** — функции которые позволяют форматировать даты.
3. **Методы** — доступные методы для работы с экземпляром календаря.
4. **Настройки** — все опции, которые можно передать для изменения поведения и отображения календаря.
5. **Действия** — обработчики событий, которые позволяют получать и обрабатывать различные данные взаимодействия с календарем.
6. **Попапы** — всплывающие окна, позволяют выбрать любой день и отобразить краткую информацию о нем прямо в календаре при наведении на этот день.
7. **Макеты** — это шаблоны, которые позволяют практически полностью изменить структуру DOM календаря и добавить свои собственные HTML-элементы.
8. **Стили** — объект классов CSS для стилизации календаря. Позволяет использовать любой CSS фреймворк, например, Tailwind CSS или собственные классы.
9. **Aria-подписи** — объект строк для `aria-label`. Позволяет локализовать все подписи календаря для обеспечения доступности.

```

### `docs/ru/reference/actions.mdx`

```mdx
---
title: Действия
description: Узнайте о различных действиях, которые можно настроить для календаря, включая обработчики событий для кликов на даты, недели, месяцы, годы и стрелки, а также для изменения времени и отображения подсказок.
section: 5
---

# Действия

## onClickDate()

`Type: Function`

`Default: null`

`Options: onClickDate(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickDate(self, event) {},
});
```

Этот метод срабатывает после нажатия на день в календаре. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `event` - событие мыши.

<Info>
  Важно знать, что каждый HTML-элемент дня, содержит data-атрибут, внутри которого находится полная дата в формате `YYYY-MM-DD`.
  Если вам нужно получить день, месяц, год отдельно, то вы можете использовать стандартные методы JS.
  В качестве примера: `new Date('2022-11-07').getDate()` вернет `7`.
</Info>

---

## onClickWeekDay()

`Type: Function`

`Default: null`

`Options: onClickWeekDay(self, day, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekDay(self, day, dateEls, event) {},
});
```

Этот метод срабатывает после нажатия на день недели в календаре. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `day` - день недели;
- `dateEls` - массив дней (html-элементов);
- `event` - событие мыши.

---

## onClickWeekNumber()

`Type: Function`

`Default: null`

`Options: onClickWeekNumber(self, number, year, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekNumber(self, number, year, dateEls, event) {},
});
```

Этот метод срабатывает после нажатия на номер недели в календаре, но для его работы необходим параметр `enableWeekNumbers` со значением `true`. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `number` - номер недели;
- `year` - год недели;
- `dateEls` - массив дней (html-элементов);
- `event` - событие мыши.

---

## onClickTitle()

`Type: Function`

`Default: null`

`Options: onClickTitle(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickTitle(self, event) {},
});
```

Этот метод срабатывает после нажатия на заголовок месяца или года в календаре. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `event` - событие мыши.

---

## onClickMonth()

`Type: Function`

`Default: null`

`Options: onClickMonth(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickMonth(self, event) {},
});
```

Этот метод срабатывает после выбора месяца в календаре. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `event` - событие мыши.

---

## onClickYear()

`Type: Function`

`Default: null`

`Options: onClickYear(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickYear(self, event) {},
});
```

Этот метод срабатывает после выбора года в календаре. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `event` - событие мыши.

---

## onClickArrow()

`Type: Function`

`Default: null`

`Options: onClickArrow(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickArrow(self, event) {},
});
```

Этот метод срабатывает после клика на стрелочку в календаре. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `event` - событие мыши.

---

## onChangeTime()

`Type: Function`

`Default: null`

`Options: onChangeTime(self, event, isError) => void | null`

```ts
new Calendar('#calendar', {
  onChangeTime(self, event) {},
});
```

Этот метод срабатывает после изменения времени в календаре. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `event` - событие change;
- `isError` - возвращает true, если пользователь ввел неверное время.

---

## onChangeToInput()

`Type: Function`

`Default: null`

`Options: onChangeToInput(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onChangeToInput(self, event) {},
});
```

Для работы этого метода необходим параметр `inputMode` с значением `true`.
Этот метод срабатывает после нажатия на день в календаре или изменения времени любым способом.
Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `event` - событие.

---

## onCreateDateRangeTooltip()

`Type: Function`

`Default: null`

`Options: onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) {},
});
```

Позволяет создать подсказку для диапазона дат. Срабатывает при нажатии и наведении курсора мыши на день, если для параметра `selectionDatesMode` установлено значание `'multiple-ranged'`.
Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь.
- `dateEl` - HTML элемент даты;
- `tooltipEl` - HTML элемент подсказки;
- `dateElBCR` - объект с информацией о положении и размере HTML элемента даты;
- `mainElBCR` - объект с информацией о положении и размере основного HTML элемента календаря.

---

## onCreateDateEls()

`Type: Function`

`Default: null`

`Options: onCreateDateEls(self, dateEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateEls(self, dateEl) {},
});
```

Этот метод срабатывает при инициализации календаря и при любых изменениях. Он предоставляет доступ к информации о каждом дне. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `dateEl` - HTML элемент даты.

---

## onCreateMonthEls()

`Type: Function`

`Default: null`

`Options: onCreateMonthEls(self, monthEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateMonthEls(self, monthEl) {},
});
```

Этот метод срабатывает, когда тип календаря установлен на `'month'`. Тип календаря также становится `'month'`, когда пользователь кликает на заголовок месяца или при инициализации с параметром `type = 'month'`. Он предоставляет доступ к информации о каждом месяце. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `monthEl` - HTML элемент месяца.

---

## onCreateYearEls()

`Type: Function`

`Default: null`

`Options: onCreateYearEls(self, yearEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateYearEls(self, yearEl) {},
});
```

Этот метод срабатывает, когда тип календаря установлен на `'year'`. Тип календаря становится `'year'`, когда пользователь кликает на заголовок года или при инициализации с параметром `type = 'year'`. Он предоставляет доступ к информации о каждом годе. Вы можете получить следующие параметры:
- `self` - ссылка на инициализированный календарь;
- `yearEl` - HTML элемент года.

---

## onInit()

`Type: Function`

`Default: null`

`Options: onInit(self) => void | null`

```ts
new Calendar('#calendar', {
  onInit(self) {},
});
```

Этот метод срабатывает при инициализации календаря. Если для параметра `inputMode` установлено значение `true`, то метод отработает при первом отображении календаря, поскольку в этот момент инициализируется календарь.
- `self` - ссылка на инициализированный календарь.

---

## onUpdate()

`Type: Function`

`Default: null`

`Options: onUpdate(self) => void | null`

```ts
new Calendar('#calendar', {
  onUpdate(self) {},
});
```

Этот метод срабатывает при обновлении/сбросе календаря с помощью метода `.update()`.
- `self` - ссылка на инициализированный календарь.

---

## onDestroy()

`Type: Function`

`Default: null`

`Options: onDestroy(self) => void | null`

```ts
new Calendar('#calendar', {
  onDestroy(self) {},
});
```

Этот метод срабатывает при уничтожении календаря.
- `self` - ссылка на инициализированный календарь.

---

## onShow()

`Type: Function`

`Default: null`

`Options: onShow(self) => void | null`

```ts
new Calendar('#calendar', {
  onShow(self) {},
});
```

Этот метод срабатывает при отображении календаря пользователю, но только если для параметра `inputMode` установлено значение `true`.
- `self` - ссылка на инициализированный календарь.

---

## onHide()

`Type: Function`

`Default: null`

`Options: onHide(self) => void | null`

```ts
new Calendar('#calendar', {
  onHide(self) {},
});
```

Этот метод срабатывает при скрытии календаря, но только если для параметра `inputMode` установлено значение `true`.
- `self` - ссылка на инициализированный календарь.

```

### `docs/ru/reference/creating-an-instance.mdx`

```mdx
---
title: Создание экземпляра
description: Узнайте, как создать экземпляр Vanilla Calendar Pro, используя CSS-селектор или HTML-элемент. Настройте календарь для инициализации в оболочке или всплывающем окне при клике на элемент.
section: 1
---

# Создание экземпляра

`new Calendar()` - создает экземпляр **Vanilla Calendar Pro**, представляющий собой инкапсуляцию календаря, его настройки и методы.

<Info>Если вы подключили **Vanilla Calendar Pro** с помощью тега `<script>`, объект доступен как глобальная переменная **window.VanillaCalendarPro**.</Info>

Экземпляр `Calendar`, принимает два параметра. Первым **обязательный** параметр может быть **CSS-селектором** или **HTML-элементом**.

**CSS-селектор** или **HTML-элемент** может представлять собой оболочку для календаря, в которой будет произведена инициализация календаря, или **«Input»**.

Оболочка для календаря - это тег `<div>`, внутри которого будет инициализирован сам календарь.

Инициализация в оболочке календаря:

```html
<div id="calendar"></div>
```

```ts
new Calendar('#calendar');
// или
const calendarEl = document.querySelector('#calendar');
new Calendar(calendarEl);
```

**«Input»** в контексте этого календаря не обязательно означает тег `<input>`, это может быть любой HTML-элемент, например, `<div>`.

При клике на **«Input»** появится всплывающее окно с календарем.

Инициализация в **«Input»**:

```html
<input type="text" id="input">
<!-- или -->
<div id="input"></div>
```

```ts
new Calendar('#input', { inputMode: true });
// или
const calendarInput = document.querySelector('#input');
new Calendar(calendarInput, {
  inputMode: true,
});
```

Второй **необязательный** параметр — это объект, определяющий настройки и действия календаря.

```ts
new Calendar('#calendar', {
  // Настройки
});
```

```

### `docs/ru/reference/labels.mdx`

```mdx
---
title: Aria-подписи
description: Aria-подписи позволяют локализовать все aria-label в календаре для доступности.
section: 9
---

# Aria-подписи

`labels` предоставляет возможность локализовать все aria-label в календаре для доступности.

Ниже приведен список всех aria-label по умолчанию.

```ts
new Calendar('#calendar', {
  labels: {
    application: 'Calendar',
    navigation: 'Calendar Navigation',
    arrowNext: {
      month: 'Next month',
      year: 'Next list of years',
      week: 'Next week',
    },
    arrowPrev: {
      month: 'Previous month',
      year: 'Previous list of years',
      week: 'Previous week',
    },
    month: 'Select month, current selected month:',
    months: 'List of months',
    year: 'Select year, current selected year:',
    years: 'List of years',
    week: 'Days of the week',
    weekNumber: 'Numbers of weeks in a year',
    collapse: 'Collapse to a single week',
    expand: 'Expand to the whole month',
    dates: 'Dates in the current month',
    selectingTime: 'Selecting a time ',
    inputHour: 'Hours',
    inputMinute: 'Minutes',
    rangeHour: 'Slider for selecting hours',
    rangeMinute: 'Slider for selecting minutes',
    btnKeeping: 'Switch AM/PM, current position:',
  },
});
```

```

### `docs/ru/reference/layouts.mdx`

```mdx
---
title: Макеты
description: Макеты позволяют изменять структуру DOM календаря и добавлять собственные HTML-элементы.
section: 7
---

# Макеты

Макеты позволяют вам почти полностью изменить структуру DOM календаря и добавить собственные HTML-элементы, такие как кнопки. Каждый тип календаря имеет свой собственный шаблон по умолчанию, и вы можете настроить каждый из них.

<Info>
  Теги, содержащие символ **«#»**, являются зарегистрированными компонентами календаря и должны содержать закрывающую косую черту в конце тега, за исключением тега **\<#Multiple>\<#/Multiple>**, который оборачивает один месяц.
  Во всех шаблонах по умолчанию перечислены все возможные компоненты для этого шаблона.
</Info>

## layouts.default

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    default: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

Это шаблон по умолчанию для отображения одного месяца и его дат.

---

## layouts.multiple

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    multiple: `
      <div class="${self.styles.controls}" data-vc="controls" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.grid}" data-vc="grid">
        <#Multiple>
          <div class="${self.styles.column}" data-vc="column" role="group">
            <div class="${self.styles.header}" data-vc="header">
              <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
                <#Month />
                <#Year />
              </div>
            </div>
            <div class="${self.styles.wrapper}" data-vc="wrapper">
              <#WeekNumbers />
              <div class="${self.styles.content}" data-vc="content">
                <#Week />
                <#Dates />
              </div>
            </div>
          </div>
        <#/Multiple>
        <#DateRangeTooltip />
      </div>
      <#ControlTime />
    `,
  },
});
```

Это шаблон по умолчанию для отображения нескольких месяцев и их дат.

---

## layouts.month

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    month: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Months />
        </div>
      </div>
    `,
  },
});
```

Это шаблон по умолчанию для выбора месяца.

---

## layouts.year

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    year: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [year] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [year] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Years />
        </div>
      </div>
    `,
  },
});
```

Это шаблон по умолчанию для выбора года.

---

## layouts.week

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    week: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [week] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [week] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

Это шаблон по умолчанию для одной недели. Он совпадает с `layouts.default`, кроме стрелок, которые шагают по неделе за раз.

```

### `docs/ru/reference/methods.mdx`

```mdx
---
title: Методы
description: Методы для управления календарем, включая инициализацию, обновление, установку параметров, удаление, показ и скрытие календаря.
section: 3
---

# Методы

## init()

Метод `init()` является основным методом экземпляра, который запускает процесс инициализации календаря.

```ts
const calendar = new Calendar(element, params);
calendar.init();
```

---

## update()

Метод `update()` позволяет применить к календарю новые настройки и выполнять сброс.
Этот метод принимает объект с необязательными аргументами для управления сбросом, по умолчанию сбрасывая выбранную пользователем дату, месяц и год после обновления.

Все aгрументы, по умолчанию `true`:

```ts
{
  year: boolean;
  month: boolean;
  dates: boolean | 'only-first';
  holidays: boolean;
  time: boolean;
}
```

- `true` - сбросится до параметров, указанных в настройках;
- `false` - не выполнит сброс, оставит параметры выбранные пользователем;
- `'only-first'` - сбрасывает все выбранные даты, оставляя самую раннюю. Если тип выбора даты указан как `'multiple-ranged'`, добавляется обработчик `'mousemove'` и `'keydown'` для наведения.

Пример использования:

```ts
calendar.locale = 'de-AT';
calendar.firstWeekday = 0;

calendar.update({
  dates: true,
});
```

---

## set()

Если вам нужно указать новые параметры или обработчики для календаря, который еще не инициализирован или уже инициализирован, вы можете использовать метод `.set()`.
Этот метод принимает объект с новыми параметрами и объект с необязательными аргументами для управления сбросом, по умолчанию сбрасывая выбранную пользователем дату, месяц и год после обновления.

Пример использования:

```ts
calendar.set({
  locale: 'de-AT',
  firstWeekday: 0,
}, {
  dates: true,
});
```

Этот метод может быть альтернативой указанию параметров при создании экземпляра календаря. Если вы вызываете этот метод перед инициализацией, не указывайте объект для управления сбросом.

```ts
const calendar = new Calendar(element);
calendar.set({ locale: 'de-AT', firstWeekday: 0 });
calendar.init();
```

---

## destroy()

Eсли вам нужно полностью удалить экземпляр календаря, вы можете использовать метод `destroy()`.

```ts
calendar.destroy();
```

---

## show()

Метод `show()` позволяет показать календарь, если он был скрыт.

```ts
calendar.show();
```

---

## hide()

Метод `hide()` позволяет скрыть календарь, если он был показан.

```ts
calendar.hide();
```

```

### `docs/ru/reference/popups.mdx`

```mdx
---
title: Попапы
description: Попапы позволяют выделить любой день и выводить краткую информацию о нем прямо в календаре при наведении курсора.
section: 6
---

# Попапы

Попапы позволяют выделить любой день и выводить краткую информацию о нем прямо в календаре при наведении курсора на этот день.

## popups['date']

`Type: String`

`Default: null`

`Options: 'YYYY-MM-DD' | 'YYYY-MM-DD:YYYY-MM-DD' | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {},
    '2022-07-01:2022-07-05': {},
  }
});
```

В качестве ключа используются даты в формате `YYYY-MM-DD`. В приведенном примере установлен поп-ап для 28 июня 2022 года.

<Info>Ключом также может быть диапазон дат в формате `'YYYY-MM-DD:YYYY-MM-DD'` (между датами можно использовать любой разделитель). Один и тот же поп-ап (`modifier`/`html`) применится ко всем дням этого диапазона — не нужно дублировать одинаковую запись для каждой даты.</Info>

---

## popups['date'].modifier

`Type: String`

`Default: null`

`Options: CSS classes | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
    },
  }
});
```

`modifier`  принимает произвольные CSS-классы, разделенные пробелами. С помощью этих классов вы можете стилизовать дату, чтобы сделать ее выделенной или изменить ее внешний вид.

---

## popups['date'].html

`Type: String`

`Default: null`

`Options: '' | HTML | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
      html: `<div>
        <u><b>12:00 PM</b></u>
        <p style="margin: 5px 0 0;">Airplane in Las Vegas</p>
      </div>`,
      // or just text
      // html: 'Airplane in Las Vegas',
    },
  }
});
```

`html` принимает обычный текст или HTML-разметку для оформления всплывающего окна.
В данном примере, при наведении курсора на 28 июня 2022 года, будет показано всплывающее окно с текстом "Airplane in Las Vegas" и временем "12:00 PM", а также применены стили, указанные в классах `bg-red` и `color-pink`.

```

### `docs/ru/reference/settings.mdx`

```mdx
---
title: Настройки
description: Настройки календаря, включая тип отображения, режим ввода, позиционирование, локализацию, даты и временные параметры.
new:
  - animation
  - enableCollapse
  - enableSwipe
section: 4
---

# Настройки

## type

`Type: String`

`Default: 'default'`

`Options: 'default' | 'multiple' | 'month' | 'year' | 'week'`

```ts
new Calendar('#calendar', {
  type: 'default',
});
```

Параметр `type` определяет тип отображаемого календаря. Тип `week` показывает одну неделю вместо целого месяца. Он работает самостоятельно или вместе с `enableCollapse`, позволяя посетителю переключаться между месяцем и неделей.

---

## inputMode

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  inputMode: true,
});
```

Параметр `inputMode` указывает, что `mainElement`, переданный как первый параметр, представляет собой поле ввода, а не обертку для календаря.

---

## openOnFocus

`Type: Boolean | Function`

`Default: true`

`Options: true | false | () => false`

```ts
new Calendar('#calendar', {
  openOnFocus: false,
  // или с callback
  openOnFocus: (self) => !self.context.isShowInInputMode,
});
```

Если параметр `openOnFocus` равен `true` или обратный вызов возвращает `true`, то фокус на input откроет календарь. Используйте `false` или колбэк, чтобы контролировать это поведение и реализовать свой обработчик фокуса.

---

## positionToInput

`Type: String`

`Default: 'left'`

`Options: 'auto' | 'center' | 'left' | 'right' | ['bottom' | 'top', 'center' | 'left' | 'right']`

```ts
new Calendar('#calendar', {
  positionToInput: 'auto',
  // positionToInput: ['bottom', 'center'],
});
```

Этот параметр определяет положение календаря относительно input, если календарь инициализирован с параметром `inputMode`.

`positionToInput` принимает строку со значением `'left'`, `'center'` или `'right'`, либо массив значений `[ось Y, ось X]`, где ось Y может быть `'bottom'` или `'top'`, а ось X может быть `'left'`, `'center'` или `'right'`.
Если ось Y не указана, то используется значение по умолчанию - `'bottom'`.

Вы можете использовать значение `positionToInput: 'auto'` для автоматического определения наилучшей позиции в зависимости от доступного места в области просмотра.
Опция позволяет рассчитать доступное пространство со всех 4 сторон и сначала попытается отобразить календарь внизу относительно input, это позиция по умолчанию.
Если внизу недостаточно места, он оценит другую лучшую доступную позицию.

---

## animation

`Type: Boolean | Object`

`Default: false`

`Options: true | false | { duration?: Number, easing?: String, slide?: Timing, fade?: Timing, collapse?: Timing }`

`Timing: { duration?: Number, easing?: String }`

```ts
new Calendar('#calendar', {
  animation: true,
  // animation: { duration: 400, easing: 'ease-out' },
  // animation: { slide: { duration: 400 }, fade: { duration: 120 }, collapse: { duration: 300 } },
});
```

Анимирует переходы между представлениями. Навигация стрелками и `enableSwipe` используют горизонтальный слайд, пикеры месяца и года — кроссфейд, а `enableCollapse` анимирует высоту календаря между месяцем и неделей.

Значения по умолчанию разные для разных переходов — `250ms` для слайдов, `150ms` для кроссфейда и `300ms` для сворачивания, все с `cubic-bezier(0.4, 0, 0.2, 1)`. Объект переопределяет любое из значений: `duration` указывается в миллисекундах, а `easing` принимает CSS-функцию плавности. Значения верхнего уровня действуют на все переходы; вложите их в `slide` (стрелки и `enableSwipe`), `fade` (пикеры) или `collapse` (`enableCollapse`), чтобы задать одну группу. Вложенные значения важнее верхнеуровневых.

<Info>
  Анимация завершения не проигрывается, если посетитель запросил уменьшение движения через `prefers-reduced-motion: reduce`. Жесты продолжают следовать за
  указателем, но после отпускания сразу завершаются или возвращаются назад.
</Info>

По умолчанию `false` ради обратной совместимости: опция появилась позже, а её включение меняет то, что видит поиск по DOM во время слайда и кроссфейда. Уходящее содержимое остаётся в DOM внутри слоя `[data-vc-ghost]` с атрибутом `inert`, поэтому элементы дат могут на короткое время присутствовать дважды. Исключайте этот слой, если ваш код их ищет; сворачивание слой-призрак не создаёт.

---

## firstWeekday

`Type: Number`

`Default: 1`

`Options: от 0 до 6`

```ts
new Calendar('#calendar', {
  firstWeekday: 1,
});
```

Этот параметр устанавливает первый день недели. Укажите число от 0 до 6, число представляет собой идентификатор дня недели. По стандартам JS дни недели начинаются с 0 и 0 это воскресенье.

---

## monthsToSwitch

`Type: Number`

`Default: 1`

`Options: от 1 до 12`

```ts
new Calendar('#calendar', {
  monthsToSwitch: 1,
});
```

Параметр `monthsToSwitch` управляет количеством переключаемых месяцев.

<Info>
  Если `monthsToSwitch` больше `1`, то в режиме выбора месяца (month picker) будут доступны для выбора только те месяцы, которые достижимы от текущего
  выбранного месяца с шагом `monthsToSwitch` — остальные будут отображаться отключёнными. Это нужно для согласованности навигации с заданным шагом (особенно
  актуально вместе с `displayMonthsCount` при `type: 'multiple'`, где это удерживает несколько видимых месяцев синхронизированными).
</Info>

---

## themeAttrDetect

`Type: String | false`

`Default: 'html[data-theme]'`

`Options: string | false`

```ts
new Calendar('#calendar', {
  themeAttrDetect: 'html[data-theme]',
});
```

Для того чтобы календарь автоматически отслеживал и применял тему сайта, вы можете передать строковое значение в виде CSS-селектора.
Квадратные скобки указывают на атрибут, содержащий название темы.
По умолчанию отслеживается тег `html` с атрибутом `data-theme`, но вы можете настроить любой другой атрибут и тег, например, `class`, если имя класса используется для задания темы: `'html[class]'`.
Если установить значение `false`, тема будет определяться системой пользователя или параметром `selectedTheme`.

---

## locale

`Type: String`

`Default: 'en'`

`Options: Language label | Array<locale>`

```ts
new Calendar('#calendar', {
  locale: 'en',
  // Or specify an object for your labels
  // locale: {
  //   months: {
  //     long: [],
  //     short: [],
  //   },
  //   weekday: {
  //     long: [],
  //     short: [],
  //   }
  // },
});
```

Этот параметр задает языковую локализацию календаря.
Вы можете указать метку языка согласно <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry" target="_blank" rel="nofollow noreferrer">BCP 47</a> или предоставить массивы названий месяцев и недель, подробнее см. [тут](/ru/docs/learn/internationalization-locale).

---

## dateToday

`Type: Date object`

`Default: 'today'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateToday: 'today',
});
```

Параметр `dateToday` определяет, какой день будет считаться сегодняшним для календаря.

---

## dateMin

`Type: String`

`Default: '1970-01-01'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMin: '1970-01-01',
});
```

Параметр `dateMin` устанавливает минимально допустимую дату, которую календарь будет учитывать, и которая не может быть меньше этой даты.

---

## dateMax

`Type: String`

`Default: '2470-12-31'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMax: '2470-12-31',
});
```

Параметр `dateMax` устанавливает максимально допустимую дату, которую календарь будет учитывать, и которая не может быть больше этой даты.

---

## displayDateMin

`Type: String`

`Default: '1970-01-01'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMin: '2022-07-01',
});
```

Этот параметр устанавливает минимальную дату, которую пользователь может выбрать. Даты, меньшие указанной, будут отключены и недоступны для выбора.

<Info>
  Важно отметить, что `displayDateMin` и `displayDateMax` отключают даты, выходящие за пределы диапазона, в то время как `dateMin` и `dateMax` вообще их не
  создают.
</Info>

<Info>
  Передача `null` в `displayDateMin` через `.set()` явно сбрасывает значение обратно к дефолтному. Передача `undefined` (например, отсутствие этого свойства)
  оставляет текущее значение без изменений.
</Info>

---

## displayDateMax

`Type: String`

`Default: '2470-12-31'`

`Options: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMax: '2024-07-01',
});
```

Этот параметр устанавливает максимальную дату, которую пользователь может выбрать. Даты, большие указанной, будут отключены и недоступны для выбора.

<Info>
  Важно отметить, что `displayDateMin` и `displayDateMax` отключают даты, выходящие за пределы диапазона, в то время как `dateMin` и `dateMax` вообще их не
  создают.
</Info>

<Info>
  Передача `null` в `displayDateMax` через `.set()` явно сбрасывает значение обратно к дефолтному. Передача `undefined` (например, отсутствие этого свойства)
  оставляет текущее значение без изменений.
</Info>

---

## displayDatesOutside

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  displayDatesOutside: false,
});
```

С помощью этого параметра вы можете решить, будут ли отображаться дни из прошлого и следующего месяца.

---

## displayDisabledDates

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  displayDisabledDates: false,
});
```

Этот параметр определяет, будут ли отображаться все дни, включая отключенные дни.

---

## displayMonthsCount

`Type: Number`

`Default: 2`

`Options: от 2 до 12`

```ts
new Calendar('#calendar', {
  displayMonthsCount: 2,
});
```

Параметр `displayMonthsCount` определяет количество отображаемых месяцев, если тип календаря установлен как `'multiple'`.

---

## disableDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  disableDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

Этот параметр позволяет отключить указанные даты, независимо от указанного диапазона.

<Info>Чтобы указать диапазон дат, используйте любой разделитель между датами в пределах одной строки.</Info>

---

## disableAllDates

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableAllDates: true,
});
```

Этот параметр отключает все дни и может быть полезен при использовании `enableDates`.

---

## disableDatesPast

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableDatesPast: true,
});
```

Этот параметр отключает все прошедшие дни.

---

## disableDatesGaps

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableDatesGaps: true,
});
```

Этот параметр отключает выбор дней в диапазоне с отключенными датами. Работает только если для параметра `selectionDatesMode` установлено значение `'multiple-ranged'`.

---

## disableWeekdays

`Type: Number`

`Default: []`

`Options: от 0 до 6`

```ts
new Calendar('#calendar', {
  disableWeekdays: [0, 6],
});
```

Этот параметр позволяет отключить указанные дни недели. Укажите массив с числами от 0 до 6, где каждое число представляет собой идентификатор дня недели. По стандартам JS дни недели начинаются с 0 и 0 это воскресенье.

---

## disableToday

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  disableToday: true,
});
```

С помощью этого параметра вы можете отключить выделение сегодняшнего дня в календаре.

---

## enableDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  enableDates: ['2022-08-11:2022-08-16', '2022-08-20', 1722152977141, new Date()],
});
```

Этот параметр позволяет включить указанные даты, независимо от диапазона и отключенных дат.

<Info>Чтобы указать диапазон дат, используйте любой разделитель между датами в пределах одной строки.</Info>

---

## enableEdgeDatesOnly

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableEdgeDatesOnly: true,
});
```

Этот параметр позволяет получить только начальную и конечную выбранную пользователем дату, игнорируя промежуточные даты. Этот параметр работает только в том случае, если для `selectionDatesMode` установлено значение `'multiple-ranged'`.

<Info>
  Важно отметить, что при использовании этого параметра отключенные даты в диапазоне дат не будут иметь никакого эффекта. Поэтому используйте эту опцию только в
  том случае, если вас интересуют только выбранные пользователем даты начала и окончания.
</Info>

---

## enableDateToggle

`Type: Boolean | Function`

`Default: true`

`Options: true | false | () => false`

```ts
new Calendar('#calendar', {
  enableDateToggle: false,
  // or with a callback
  enableDateToggle: (self) => new Date(self.selectedDates[0]) < new Date(),
});
```

Если параметр `enableDateToggle` имеет значение `true` или обратный вызов возвращает `true`, то повторный клик на выбранную дату отменяет выбор.

---

## enableWeekNumbers

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableWeekNumbers: true,
});
```

С помощью этого параметра вы можете решить, будут ли отображаться номера недель в году.

---

## enableMonthChangeOnDayClick

`Type: Boolean`

`Default: true`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableMonthChangeOnDayClick: false,
});
```

С помощью этой параметра вы можете решить, будет ли месяц переключаться по клику на день из предыдущего или следующего месяца.

---

## enableJumpToSelectedDate

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableJumpToSelectedDate: true,
  selectedDates: ['2018-05-02'],
});
```

Если эта опция включена и указаны одна или несколько выбранных дат, но без указания `selectedMonth` и `selectedYear`, календарь перейдет к первой выбранной дате. Если установлено значение `false`, календарь всегда будет открываться для текущего месяца и года.

<Info>Эта опция не имеет эффекта, если указаны `selectedMonth` и `selectedYear`.</Info>

---

## enableCollapse

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableCollapse: true,
});
```

Добавляет под сеткой элемент управления, который сворачивает месяц до одной недели и разворачивает обратно. Неделя выбирается по первой выбранной дате, если она относится к отображаемому месяцу; иначе по сегодняшнему дню, если он относится к этому месяцу; иначе по первому числу отображаемого месяца. На устройствах с мышью элемент выглядит как шеврон, на сенсорных — как черточка, которую можно тянуть вверх и вниз.

<Info>`enableCollapse` не требует `enableSwipe` или `animation`. Сворачивание переключает `type` на `'week'`, поэтому `calendar.type` показывает текущее состояние, а `set({ type: 'week' })` делает то же самое без перехода. Опцию поддерживают только типы `default` и `week`; другие типы вызывают ошибку при `init()`.</Info>

---

## enableSwipe

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableSwipe: true,
});
```

Позволяет посетителю тянуть содержимое календаря в сторону, чтобы перейти к следующему или предыдущему периоду, во всех представлениях, где работают стрелки: `default`, `multiple`, `week` и список годов. Соседний период следует за указателем. Расстояние и скорость в момент отпускания определяют, встанет он на место или вернётся назад.

<Info>
  `enableSwipe` не требует `enableCollapse` или `animation`; без анимации отпускание срабатывает мгновенно. Вертикальная прокрутка над календарём остаётся за
  страницей, а свайп доступен, только пока видна соответствующая стрелка, поэтому учитывает `dateMin`, `dateMax` и ограничения навигации. Дата, на которой
  закончилась тяга, не выбирается.
</Info>

---

## selectionDatesMode

`Type: String | false`

`Default: 'single'`

`Options: 'single' | 'multiple' | 'multiple-ranged' | false`

```ts
new Calendar('#calendar', {
  selectionDatesMode: 'single',
});
```

Этот параметр определяет, разрешено ли выбирать один или несколько дней, либо выбор дней полностью отключен.

---

## selectionMonthsMode

`Type: Boolean`

`Default: true`

`Options: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionMonthsMode: false,
});
```

Этот параметр позволяет отключить выбор месяца, разрешить переключение месяцев только с помощью стрелок или разрешить переключение месяцев любым способом.

---

## selectionYearsMode

`Type: Boolean`

`Default: true`

`Options: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionYearsMode: false,
});
```

Этот параметр позволяет отключить выбор года, разрешить переключение года только с помощью стрелок или разрешить переключение года любым способом.

---

## selectionTimeMode

`Type: false | Number`

`Default: false`

`Options: false | 24 | 12`

```ts
new Calendar('#calendar', {
  selectionTimeMode: true,
});
```

Этот параметр включает выбор времени. Вы также можете указать формат времени, используя число: 24-часовой или 12-часовой формат.

---

## selectedDates

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  selectedDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

Этот параметр позволяет указать список дат, которые будут выбраны при инициализации календаря.

<Info>Чтобы указать диапазон дат, используйте любой разделитель между датами в пределах одной строки.</Info>

---

## selectedMonth

`Type: Number`

`Default: null`

`Options: от 0 до 11 | null`

```ts
new Calendar('#calendar', {
  selectedMonth: 0,
});
```

Этот параметр определяет месяц, который будет отображаться при инициализации календаря. По стандартам JS месяцы нумеруются с 0 до 11. Смотрите [enableJumpToSelectedDate](/ru/docs/reference/settings#enablejumptoselecteddate), чтобы установить по умолчанию первую выбранную дату.

---

## selectedYear

`Type: Number`

`Default: null`

`Options: Number (YYYY) | null`

```ts
new Calendar('#calendar', {
  selectedYear: 2022,
});
```

Этот параметр определяет год, который будет отображаться при инициализации календаря. Смотрите [enableJumpToSelectedDate](/ru/docs/reference/settings#enablejumptoselecteddate), чтобы установить по умолчанию первую выбранную дату.

---

## selectedHolidays

`Type: String[] | Number[] | Date[]`

`Default: null`

`Options: ['YYYY-MM-DD'] | [Number] | [Date] | null`

```ts
new Calendar('#calendar', {
  selectedHolidays: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

Этот параметр позволяет указать даты, которые будут считаться праздничными и получат дополнительный атрибут данных для стилизации.

<Info>Чтобы указать диапазон дат, используйте любой разделитель между датами в пределах одной строки.</Info>

---

## selectedWeekends

`Type: Number`

`Default: [0, 6]`

`Options: number[0-6]`

```ts
new Calendar('#calendar', {
  selectedWeekends: [0, 6],
});
```

Этот параметр позволяет указать выходные дни недели. Укажите массив с числами от 0 до 6, где каждое число представляет собой идентификатор дня недели. По стандартам JS дни недели начинаются с 0 и 0 это воскресенье.

---

## selectedTime

`Type: String`

`Default: null`

`Options: 'hh:mm aa' | null`

```ts
new Calendar('#calendar', {
  selectedTime: '03:44 AM',
});
```

Этот параметр позволяет задать время, которое будет отображаться при инициализации календаря. Время задается в формате `'hh:mm aa'`, где `'aa'` - это маркер AM/PM. Если используется 24-часовой формат, маркер `'aa'` указывать не требуется.

---

## selectedTheme

`Type: String`

`Default: 'system'`

`Options: string (custom theme) | 'light' | 'dark' | 'system'`

```ts
new Calendar('#calendar', {
  selectedTheme: 'system',
});
```

Этот параметр определяет тему календаря. По умолчанию тема определяется системой пользователя или настройками сайта.

---

## timeMinHour

`Type: Number`

`Default: 0`

`Options: от 0 до 23`

```ts
new Calendar('#calendar', {
  timeMinHour: 0,
});
```

Этот параметр указывает, какой час будет минимальным для выбора.

---

## timeMaxHour

`Type: Number`

`Default: 23`

`Options: от 0 до 23`

```ts
new Calendar('#calendar', {
  timeMaxHour: 23,
});
```

Этот параметр указывает, какой час будет максимальным для выбора.

---

## timeMinMinute

`Type: Number`

`Default: 0`

`Options: от 0 до 59`

```ts
new Calendar('#calendar', {
  timeMinMinute: 0,
});
```

Этот параметр указывает, какая минута будет минимальной для выбора.

---

## timeMaxMinute

`Type: Number`

`Default: 59`

`Options: от 0 до 59`

```ts
new Calendar('#calendar', {
  timeMaxMinute: 59,
});
```

Этот параметр указывает, какая минута будет максимальной для выбора.

---

## timeControls

`Type: String`

`Default: 'all'`

`Options: 'all' | 'range'`

```ts
new Calendar('#calendar', {
  timeControls: 'all',
});
```

Этот параметр определяет способ выбора времени: `'all'` (любым способом) или `'range'` (только с помощью контроллера).

---

## timeStepHour

`Type: Number`

`Default: 1`

`Options: от 1 до 23`

```ts
new Calendar('#calendar', {
  timeStepHour: 1,
});
```

Этот параметр устанавливает шаг для контроллера часов.

---

## timeStepMinute

`Type: Number`

`Default: 1`

`Options: от 1 до 59`

```ts
new Calendar('#calendar', {
  timeStepMinute: 1,
});
```

Этот параметр устанавливает шаг для контроллера минут.

---

## sanitizerHTML

`Type: Function`

`Default: (html) => html`

```ts
import DOMPurify from 'dompurify';

new Calendar('#calendar', {
  sanitizerHTML: (html) => DOMPurify.sanitize(html),
});
```

`sanitizerHTML` может очищать HTML-шаблоны, чтобы они были безопасными для CSP.

<Info>
  Обратите внимание, что в качестве примера используется сторонняя библиотека{' '}
  <a href="https://www.npmjs.com/package/dompurify" target="_blank" rel="nofollow noreferrer">
    `dompurify`
  </a>
  . `sanitizerHTML` не является обязательным для работы календаря.
</Info>

```

### `docs/ru/reference/styles.mdx`

```mdx
---
title: Стили
description: Полное руководство по кастомизации CSS-классов в календаре с помощью параметра styles, включая список классов по умолчанию и их замену.
section: 8
---

# Стили

`styles` предоставляет возможность переопределить любой CSS-класс в календаре. Вы можете заменить любые значения на список из CSS классов.

Ниже приведен список всех классов по умолчанию.

## CSS-классы

```ts
new Calendar('#calendar', {
  styles: {
    // Базовые
    calendar: 'vc',
    controls: 'vc-controls',
    grid: 'vc-grid',
    column: 'vc-column',

    // Заголовок / шапка
    header: 'vc-header',
    headerContent: 'vc-header__content',
    month: 'vc-month',
    year: 'vc-year',
    arrowPrev: 'vc-arrow vc-arrow_prev',
    arrowNext: 'vc-arrow vc-arrow_next',

    // Выбор месяца / года
    wrapper: 'vc-wrapper',
    content: 'vc-content',
    months: 'vc-months',
    monthsRow: 'vc-months__row',
    monthsCell: 'vc-months__cell',
    monthsMonth: 'vc-months__month',
    years: 'vc-years',
    yearsRow: 'vc-years__row',
    yearsCell: 'vc-years__cell',
    yearsYear: 'vc-years__year',

    // Строка недели / номера недель
    week: 'vc-week',
    weekDay: 'vc-week__day',
    weekDayBtn: 'vc-week__day-btn',
    weekNumbers: 'vc-week-numbers',
    weekNumbersTitle: 'vc-week-numbers__title',
    weekNumbersContent: 'vc-week-numbers__content',
    weekNumber: 'vc-week-number',

    // Даты
    collapse: 'vc-collapse',
    dates: 'vc-dates',
    datesRow: 'vc-dates__row',
    date: 'vc-date',
    dateBtn: 'vc-date__btn',

    // Попапы и тултип
    datePopup: 'vc-date__popup',
    dateRangeTooltip: 'vc-date-range-tooltip',

    // Управление временем
    time: 'vc-time',
    timeContent: 'vc-time__content',
    timeHour: 'vc-time__hour',
    timeMinute: 'vc-time__minute',
    timeKeeping: 'vc-time__keeping',
    timeRanges: 'vc-time__ranges',
    timeRange: 'vc-time__range',
  },
});
```

---

## CSS-переменные

Каждый цвет во встроенных темах (`light`, `dark`, `slate-light`) задан через CSS custom property с оригинальным цветом темы в качестве значения по умолчанию (fallback). Это значит, что внешний вид календаря можно поменять, задав несколько переменных — без переопределения CSS-классов и без риска, что переопределение темы не сработает как ожидается.

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

Если переменная не задана, календарь рендерится ровно как раньше — ничего не меняется, пока вы явно не зададите переменную.

<Info>Если задать переменную на `:root`, она применится сразу ко всем темам (light/dark/slate-light используют одни и те же имена переменных). Чтобы переопределить только одну тему, ограничьте область действия селектором этой темы, например: `[data-vc-theme='dark'] { --vc-date-selected-bg: #7c3aed; }`.</Info>

### Базовые

| Переменная                 | light      | dark       | slate-light |
| -------------------------- | ---------- | ---------- | ----------- |
| `--vc-bg`                  | white      | slate-900  | slate-100   |
| `--vc-color`               | slate-900  | white      | gray-800    |
| `--vc-focus-outline-color` | orange-300 | orange-300 | blue-300    |

### Заголовок / шапка

| Переменная                  | light     | dark      | slate-light |
| --------------------------- | --------- | --------- | ----------- |
| `--vc-header-color`         | slate-900 | white     | gray-800    |
| `--vc-title-color`          | slate-900 | white     | gray-800    |
| `--vc-title-color-hover`    | slate-500 | slate-500 | gray-600    |
| `--vc-title-color-disabled` | slate-300 | slate-700 | gray-400    |

### Выбор месяца / года

| Переменная                         | light     | dark      | slate-light |
| ---------------------------------- | --------- | --------- | ----------- |
| `--vc-months-years-bg`             | white     | slate-900 | slate-100   |
| `--vc-months-years-color`          | slate-500 | white     | gray-600    |
| `--vc-months-years-bg-hover`       | slate-100 | slate-800 | slate-200   |
| `--vc-months-years-color-disabled` | slate-300 | slate-700 | gray-400    |
| `--vc-months-years-bg-selected`    | cyan-500  | slate-500 | blue-500    |
| `--vc-months-years-color-selected` | white     | white     | white       |

### Управление сворачиванием

| Переменная            | light     | dark      | slate-light |
| --------------------- | --------- | --------- | ----------- |
| `--vc-collapse-color` | slate-300 | slate-600 | slate-300   |

### Строка недели / номера недель

| Переменная                      | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-week-numbers-title-color` | slate-500 | white     | gray-600    |
| `--vc-week-number-color`        | slate-500 | white     | gray-600    |
| `--vc-week-number-color-hover`  | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-color`           | slate-500 | white     | gray-600    |
| `--vc-week-day-color-hover`     | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-off-color`       | rose-500  | rose-500  | red-500     |
| `--vc-week-day-off-color-hover` | rose-600  | rose-600  | red-600     |

### Даты

| Переменная                                   | light     | dark      | slate-light |
| -------------------------------------------- | --------- | --------- | ----------- |
| `--vc-date-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-color`                            | slate-900 | slate-400 | gray-800    |
| `--vc-date-color-hover` <sup>dark only</sup> | —         | slate-200 | —           |
| `--vc-date-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-edge-bg`                    | slate-200 | slate-700 | slate-300   |
| `--vc-date-disabled-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-outside-color`                    | slate-400 | slate-600 | gray-400    |
| `--vc-date-today-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-today-color`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-today-outside-color`              | slate-500 | slate-600 | gray-600    |
| `--vc-date-selected-bg`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-selected-color`                   | white     | white     | white       |
| `--vc-date-selected-outside-bg`              | slate-300 | slate-700 | slate-300   |
| `--vc-date-selected-outside-color`           | slate-500 | slate-300 | gray-600    |

### Выходные / праздники

| Переменная                                                   | light     | dark      | slate-light |
| ------------------------------------------------------------ | --------- | --------- | ----------- |
| `--vc-date-weekend-color`                                    | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-bg-hover`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-bg`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-edge-bg`                            | rose-100  | slate-700 | slate-300   |
| `--vc-date-weekend-disabled-color`                           | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-today-color`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-today-disabled-color`                     | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-outside-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-weekend-outside-color`                            | slate-400 | slate-600 | gray-400    |
| `--vc-date-weekend-outside-color-hover` <sup>dark only</sup> | —         | slate-300 | —           |
| `--vc-date-weekend-outside-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-outside-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-today-outside-color`                      | slate-400 | slate-400 | gray-400    |
| `--vc-date-weekend-disabled-outside-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-selected-bg`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-selected-color`                           | white     | white     | white       |

### Выбранные диапазоны (`multiple-ranged`)

| Переменная                             | light           | dark            | slate-light     |
| -------------------------------------- | --------------- | --------------- | --------------- |
| `--vc-date-range-middle-bg`            | cyan-500 at 70% | cyan-500 at 80% | blue-500 at 80% |
| `--vc-date-range-middle-color`         | white           | white           | white           |
| `--vc-date-range-middle-outside-bg`    | slate-200       | slate-800       | slate-200       |
| `--vc-date-range-middle-outside-color` | slate-500       | slate-300       | gray-600        |
| `--vc-date-range-middle-weekend-bg`    | rose-500 at 70% | rose-500 at 80% | red-500 at 80%  |
| `--vc-date-range-middle-weekend-color` | white           | white           | white           |

### Попапы и тултип

| Переменная                      | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-date-popup-bg`            | white     | slate-800 | white       |
| `--vc-date-popup-color`         | slate-900 | white     | gray-800    |
| `--vc-date-range-tooltip-bg`    | slate-50  | slate-800 | slate-50    |
| `--vc-date-range-tooltip-color` | slate-500 | slate-400 | slate-500   |

### Управление временем

| Переменная                                           | light      | dark      | slate-light |
| ---------------------------------------------------- | ---------- | --------- | ----------- |
| `--vc-time-border-color`                             | slate-300  | slate-800 | gray-300    |
| `--vc-time-separator-color`                          | slate-900  | white     | gray-800    |
| `--vc-time-input-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-input-color`                              | slate-900  | white     | gray-800    |
| `--vc-time-input-bg-hover`                           | orange-100 | slate-700 | blue-100    |
| `--vc-time-keeping-color`                            | slate-500  | slate-500 | gray-600    |
| `--vc-time-keeping-color-hover` <sup>dark only</sup> | —          | slate-400 | —           |
| `--vc-time-range-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-range-track-color`                        | slate-300  | slate-600 | slate-300   |
| `--vc-time-range-thumb-bg`                           | white      | slate-800 | slate-100   |
| `--vc-time-range-thumb-border`                       | slate-300  | slate-600 | gray-300    |
| `--vc-time-range-thumb-border-hover`                 | slate-400  | slate-400 | gray-400    |

<Info>
  Три переменные, помеченные "dark only", существуют потому, что у тёмной темы есть дополнительное hover-состояние для этих элементов, которого нет в
  light/slate-light — в остальных темах переопределять для них попросту нечего.
</Info>

```

### `docs/ru/reference/utilities.mdx`

```mdx
---
title: Утилиты
description: Узнайте о 4 удобных утилитах для работы с датами, поставляемых с Vanilla Calendar Pro. Эти функции позволяют форматировать даты, преобразовывать их в нужные форматы и определять номера недель.
section: 2
---

# Утилиты

Вместе с календарем устанавливаются его утилиты, с помощью которых можно удобно форматировать даты.

Всего есть 4 утилиты, они являются функциями и вы можете использовать их в любом месте вашего кода, даже без календаря.

1. **`parseDates(dates: string[])`** — принимает на вход массив диапазонов дат с использованием разделителя между датами в строковом формате типа `FormatDateString ('YYYY-MM-DD')`. Возвращает массив дат в строковом формате типа `FormatDateString ('YYYY-MM-DD')`.
```ts
import { parseDates } from 'vanilla-calendar-pro/utils';
parseDates(['2024-12-12:2024-12-15']); // возвращает: ['2024-12-12', '2024-12-13', '2024-12-14', '2024-12-15']
```

2. **`getDateString(date: Date)`** — принимает на вход дату типа `Date`. Возвращает дату в строковом формате типа `FormatDateString ('YYYY-MM-DD')`.
```ts
import { getDateString } from 'vanilla-calendar-pro/utils';
getDateString(new Date('24.12.2024')); // возвращает: 2024-12-24
```

3. **`getDate(date: FormatDateString)`** — принимает дату в строковом формате, например `FormatDateString ('YYYY-MM-DD')`. Возвращает дату типа `Date`.
```ts
import { getDate } from 'vanilla-calendar-pro/utils';
getDate('2024-12-12'); // возвращает: Tue Dec 24 2024 00:00:00 GMT
```

4. **`getWeekNumber(date: FormatDateString, weekStartDay: WeekDayID)`** — принимает на вход дату в строковом формате типа `FormatDateString ('YYYY-MM-DD')` и день начала недели, а точнее его `id` с типом `number` от 0 до 6. Возвращает объект `{ year: yearNumber, week: weekNumber }` для даты, указанной в аргументах.
```ts
import { getWeekNumber } from 'vanilla-calendar-pro/utils';
getWeekNumber('2024-12-12', 1); // возвращает: {year: 2024, week: 50}
```

```

### `docs/zh/learn.mdx`

```mdx
---
title: 介绍
description: 页面描述
---

# Vanilla Calendar Pro 介绍

**Vanilla Calendar Pro** 是一个强大、灵活且轻量级的处理日期和时间的工具，专为需要为 Web 应用程序或网站提供功能齐全且易于自定义的日历的开发人员而创建。它独立于外部库且性能卓越，是集成到任何需要日历的项目中的绝佳选择。

此日历专为从事各种项目的开发人员设计，无论是个人网站、企业门户还是复杂的 Web 应用程序。Vanilla Calendar Pro 非常适合那些寻找简单日期显示解决方案的人，以及那些需要更高级功能（如时间选择和交互操作）的人。

## 主要特性

Vanilla Calendar Pro 提供了一套丰富的功能，允许创建方便且自适应的日历小部件。

主要特性包括：

- **轻量级**：最终的 JavaScript 文件经过压缩和优化，可快速加载。
- **无依赖**：完全独立，无需额外的库。
- **易于本地化**：支持轻松本地化为任何语言。
- **可自定义**：通过 CSS 和 HTML 标记轻松配置。
- **多实例**：允许在单个页面上使用无限数量的日历。
- **主题支持**：自动在浅色和深色主题之间切换，并支持自定义主题。
- **周起始日自定义**：允许选择一周中的任何一天作为起始日。
- **周末自定义**：允许为每周设置自定义周末。
- **周数显示**：可以显示一年中的周数。
- **不绑定到 `<input>`**：与许多日历不同，它不限于与 `<input>` 元素一起使用。
- **可访问性**：包括 ARIA 标签、`tabindex` 和完整的键盘导航，增强了可访问性。
- **日期和时间范围选择**：支持选择具有最小和最大限制的日期和时间范围。
- **弹出窗口和工具提示**：允许设置带有自定义信息的弹出窗口，并为日期范围选择添加工具提示。

## 尝试 Vanilla Calendar Pro

以下是 Vanilla Calendar Pro 在 JS 沙盒中的实时示例。您可以修改参数并立即查看日历如何适应您的设置。

<Sandbox example="installation-and-usage" />

<Info>**此演示示例** — 本节中的众多示例之一 — 帮助您了解如何使用 Vanilla Calendar Pro 并根据您的需求进行自定义。</Info>

在以下部分中，您将找到成功集成和设置 Vanilla Calendar Pro 所需的一切。

```

### `docs/zh/learn/additional-features-animation.mdx`

```mdx
---
title: 动画
new: true
description: 了解如何配置日历视图切换时的滑动、交叉淡入淡出和折叠动画。
section: 6. 附加功能
---

# 动画

视图之间的切换可以添加动画。箭头导航和滑动手势会水平滑动，月份与年份选择器使用交叉淡入淡出，折叠则在整月与一周之间对日历高度进行动画。

<Info>出于向后兼容的考虑，动画默认关闭：该选项是后来加入的，而滑动和交叉淡入淡出进行期间，DOM 查询结果会短暂发生变化。</Info>

<Sandbox example="additional-features-animation" height={400} />

## 所有过渡共用一套时间

传入对象而不是 `true` 即可覆盖时间设置。顶层的值会作用于所有过渡。

<Sandbox example="additional-features-animation-shared" height={400} />

## 分别设置时间

三组过渡可以彼此独立地调整。把值嵌套在 `slide`（箭头和滑动手势）、`fade`（选择器）或 `collapse`（整月与一周之间的折叠）下即可。嵌套值优先于顶层值。

下面的示例给滑动配了一条会越过目标再回弹的曲线，而选择器和折叠控件分别使用更平缓的时间设置。

<Sandbox example="additional-features-animation-custom" height={400} />

<Info>当访问者通过 `prefers-reduced-motion: reduce` 要求减少动效时，松手后的过渡动画会被跳过。手势仍会跟随指针，并在松手后立即落位。</Info>

## 动画进行时查询日历

滑动和交叉淡入淡出进行期间，正在退出的内容会保留在 DOM 中带有 `inert` 的 `[data-vc-ghost]` 图层内，因此日期元素可能会短暂出现两份。`onClickArrow` 和 `onClickDate` 等回调正是在这个时间窗口内触发的，如果你在回调里检查日历，请排除这个图层。折叠不会创建幽灵图层。

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/zh/learn/additional-features-collapse.mdx`

```mdx
---
title: 折叠
new: true
description: 了解如何让访问者把整月折叠为一周并再次展开。
section: 6. 附加功能
---

# 折叠

`enableCollapse` 会在网格下方添加一个控件。点击它，整月会折叠为一周，再次点击则展开。该选项默认关闭，并且不依赖 `enableSwipe` 或 `animation`。

<Sandbox example="additional-features-collapse" height={420} />

控件会随设备变化。使用鼠标时是一个箭头；在触摸屏上则变成一根可以上下拖动的小横条，日历会全程跟随手指。缓慢拖动时需要超过全程的四分之一；快速甩动还会考虑松手速度，因此可能更早完成。其他情况下日历会回弹。

如果第一个选中日期属于当前显示月份，就以它所在的周为准。否则，如果今天属于该月份，就使用今天所在的周；再否则，以当前显示月份第一天所在的周为准。

折叠状态下，箭头每次翻动一周。再次展开时，日历会回到围绕这一周的月份。

<Info>折叠会把 `type` 切换为 `'week'`，因此 `calendar.type` 能反映当前状态，而 `set({ type: 'week' })` 会在没有过渡的情况下做同样的事。该选项只被 `default` 和 `week` 类型接受，与 `multiple` 搭配会在 `init()` 时抛出错误。</Info>

## 时间设置

过渡使用 [`animation`](/docs/reference/settings) 选项，并可通过 `collapse` 分组单独设置时间：

```ts
new Calendar('#calendar', {
  animation: { collapse: { duration: 450 } },
  enableCollapse: true,
});
```

<Info>未启用 `animation` 或访问者通过 `prefers-reduced-motion: reduce` 要求减少动效时，拖动仍然跟随手指，但松手后会立即落位。</Info>

```

### `docs/zh/learn/additional-features-layouts.mdx`

```mdx
---
title: 布局
description: 布局允许您自定义日历的 HTML 标记，添加您自己的元素，例如按钮。学习如何自定义日历标题并为不同类型的日历添加元素。
section: 6. 附加功能
---

# 布局

日历提供了一种使用 `layouts` 参数自定义 HTML 标记的便捷方式。这允许您向日历添加自己的元素，例如按钮或任何其他 HTML 元素。

`layouts` 将日历的 `type` 作为键，将字符串作为值。

在以下示例中，为 `type: 'default'` 自定义了日历标题，并在日历内部添加了一个常规按钮。

<Sandbox example="additional-features-layouts" />

现在，让我们使用 `inputMode: true` 参数。我们将添加一个按钮，单击该按钮时将隐藏日历。

<Sandbox example="additional-features-layouts-btn-close" input={true} />

```

### `docs/zh/learn/additional-features-popups-and-tooltip.mdx`

```mdx
---
title: 弹出窗口和工具提示
description: 学习如何为日历中的任何日期添加带有信息的弹出窗口，并使用工具提示选择日期范围。
section: 6. 附加功能
---

# 弹出窗口和工具提示

## 弹出窗口

日历允许您为任何日期添加带有信息的弹出窗口，这些信息将在悬停该日期时显示。

在提供的示例中，使用 CSS 修饰符突出显示特定日期，并将信息添加到弹出窗口。

有关弹出窗口的更多详细信息，请参阅参考指南。

<Sandbox example="additional-features-popups" />

## 工具提示

当 `selectionDatesMode` 参数设置为 `'multiple-ranged'` 时，可以使用工具提示。使用 `onCreateDateRangeTooltip`，您可以创建完全自定义的工具提示。

<Sandbox example="additional-features-tooltips" />

```

### `docs/zh/learn/additional-features-styles.mdx`

```mdx
---
title: 样式
description: 通过用您自己的 CSS 类替换来定制日历的样式。学习如何自定义日历的外观。
section: 6. 附加功能
---

# 样式

日历中使用的所有 CSS 类都是变量，可以通过用您自己的值替换它们来自定义。

<Info>当用您自己的 CSS 类替换时，请记住您需要在您自己的 CSS 中创建并设置此类的样式。</Info>

以下是用您自己的类替换箭头类的示例。完整的类列表可以在参考指南中找到。

<Sandbox example="additional-features-styles" />

## CSS 变量

如果您只需要更改颜色，甚至不需要替换任何类——内置主题中的每一种颜色都以 CSS 自定义属性的形式暴露，并以主题的原始颜色作为回退值（fallback）：

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

只有当您显式设置某个变量时，效果才会改变。完整的变量列表可在[参考指南](/docs/reference/styles)中找到。

```

### `docs/zh/learn/additional-features-swipe.mdx`

```mdx
---
title: 滑动
new: true
description: 了解如何让访问者横向拖动日历，切换到下一个或上一个周期。
section: 6. 附加功能
---

# 滑动

`enableSwipe` 允许横向拖动日历内容。该选项默认关闭，与 `enableCollapse` 和 `animation` 相互独立，并可用于所有能通过箭头导航的视图——`default`、`multiple`、`week` 和年份列表。手势每次移动的幅度与当前视图中的箭头一致。

<Sandbox example="additional-features-swipe" height={420} />

手势一开始，相邻周期就已渲染并随指针移动，因此拖动过程中看到的是即将到达的内容，而不是一片空白。缓慢拖动时需要超过宽度的四分之一；快速甩动还会考虑松手速度，因此可能更早翻页。其他情况下内容会滑回原处。

<Info>
  手势只占用横向轴，因此页面在日历上方仍可正常纵向滚动。只有对应箭头可见时才能滑动，因此手势会遵守 `dateMin`、`dateMax`
  和导航限制。松手时指针下方的日期不会被选中。
</Info>

## 时间设置

手势使用 [`animation`](/docs/reference/settings) 选项的 `slide` 分组，因此与箭头导航采用相同的时间设置：

```ts
new Calendar('#calendar', {
  animation: { slide: { duration: 350 } },
  enableSwipe: true,
});
```

<Info>未启用 `animation` 或访问者通过 `prefers-reduced-motion: reduce` 要求减少动效时，拖动仍然跟随指针，但松手后会立即落位。</Info>

## 手势进行时查询日历

滑动使用的图层与箭头动画相同，因此在其进行期间，正在退出的周期仍保留在 DOM 中带有 `inert` 的 `[data-vc-ghost]` 元素内，日期单元格会短暂地出现两份。如果你自己的代码会遍历它们，请排除这个图层。

```ts
const dates = calendar.context.mainElement.querySelectorAll('[data-vc-date]');
const visible = [...dates].filter((date) => !date.closest('[data-vc-ghost]'));
```

```

### `docs/zh/learn/additional-features-themes.mdx`

```mdx
---
title: 主题
description: 日历支持自定义主题，默认具有浅色和深色主题。学习如何配置主题并使用系统设置或您自己的主题。
section: 6. 附加功能
---

# 主题

日历支持自定义主题，默认具有浅色和深色主题。

如果 `themeAttrDetect` 参数设置为 `false`，主题将由用户的系统设置或 `selectedTheme` 参数确定。

日历可以根据设置的标签和属性自动检测和跟踪网站的主题。有关此参数的更多信息可以在参考指南中找到。

如果您的网站仅支持一个主题，或者您想根据自己的喜好自定义日历的外观，可以明确选择可用的主题之一。

以下示例演示了强制使用深色主题：

<Sandbox example="additional-features-themes-dark" themeDetection={false} />

这是相同的示例，但使用浅色主题：

<Sandbox example="additional-features-themes-light" themeDetection={false} />

如上所述，您可以使用自己的主题，自己创建它们，或者如果它们存在，从日历中导入它们。

<Sandbox example="additional-features-themes-slate-light" themeDetection={false} />

```

### `docs/zh/learn/components-for-libraries-angular.mdx`

```mdx
---
title: Angular 组件
description: 学习如何为 Vanilla Calendar Pro 创建和使用 Angular 组件。创建组件并将其集成到 Angular 应用程序中的详细指南。
section: 7. 库组件
---

# Angular 组件

<Info>
  本示例适用于 Angular 15+（standalone 组件）。
</Info>

出于演示目的，让我们为 Vanilla Calendar Pro 创建一个简单的 Angular 组件。创建一个名为 `vanilla-calendar.component.ts` 的文件，并将以下代码复制到其中：

```ts
import { AfterViewInit, Component, ElementRef, Input, ViewChild } from '@angular/core';
import { Calendar, Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

@Component({
  selector: 'vanilla-calendar',
  standalone: true,
  template: `<div #calendarRef></div>`,
})
export class VanillaCalendarComponent implements AfterViewInit {
  @Input() config?: Options;
  @ViewChild('calendarRef') calendarRef!: ElementRef<HTMLDivElement>;

  ngAfterViewInit() {
    const calendar = new Calendar(this.calendarRef.nativeElement, this.config);
    calendar.init();
  }
}
```

然后，将创建的 `VanillaCalendarComponent` 导入到您计划显示日历的组件中。

```ts
// ...
import { VanillaCalendarComponent } from './vanilla-calendar.component';
// ...
```

将其添加到 standalone 组件的 `imports` 数组中，并在模板中使用。

```ts
@Component({
  // ...
  imports: [VanillaCalendarComponent],
  template: `
    <!-- -->
    <vanilla-calendar />
    <!-- -->
  `,
})
```

`VanillaCalendarComponent` 可以接受 `<div>` 标签支持的任何 HTML 属性（Angular 会自动将它们转发到宿主元素），以及用于配置日历的 `config` 输入属性。

```ts
template: `
  <!-- -->
  <vanilla-calendar [config]="{ type: 'multiple' }" class="thisIsMyClass" />
  <!-- -->
`,
```

```

### `docs/zh/learn/components-for-libraries-react.mdx`

```mdx
---
title: React 组件
description: 学习如何为 Vanilla Calendar Pro 创建和使用 React 组件。创建组件并将其集成到 React 应用程序中的详细指南。
section: 7. 库组件
---

# React 组件

<Info>
  本示例适用于 React 16.8+（使用 Hooks 的函数组件）。如果您不使用 TypeScript，请使用 `.jsx` 扩展名而不是 `.tsx`，并从组件中删除 `CalendarProps` 接口。
</Info>

出于演示目的，让我们考虑 Vanilla Calendar Pro 的最简单 React 组件。创建一个名为 `VanillaCalendar.tsx` 的文件，并将以下代码复制到其中：

```tsx
import { useEffect, useRef, useState } from 'react';
import { Options, Calendar } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

interface CalendarProps extends React.HTMLAttributes<HTMLDivElement> {
  config?: Options,
}

function VanillaCalendar({ config, ...attributes }: CalendarProps) {
  const ref = useRef(null);
  const [calendar, setCalendar] = useState<Calendar | null>(null);

  useEffect(() => {
    if (!ref.current) return;
    setCalendar(new Calendar(ref.current, config));
  }, [ref, config])

  useEffect(() => {
    if (!calendar) return;
    calendar.init()
  }, [calendar])

  return (
    <div {...attributes} ref={ref}></div>
  )
}

export default VanillaCalendar;
```

然后，将创建的 `VanillaCalendar` 组件导入到您计划显示日历的 React 应用程序中。

```tsx
import VanillaCalendar from './VanillaCalendar';
```

使用创建的组件。

```tsx
// ...
<VanillaCalendar />
// ...
```

`VanillaCalendar` 组件可以接受 `<div>` 标签支持的任何 HTML 属性，以及用于配置日历的 `config` 参数。

```tsx
// ...
<VanillaCalendar config={{
    type: 'multiple',
  }} className="thisIsMyClass" />
// ...
```

```

### `docs/zh/learn/components-for-libraries-vue.mdx`

```mdx
---
title: Vue 组件
description: 学习如何为 Vanilla Calendar Pro 创建和使用 Vue 组件。创建组件并将其集成到 Vue 应用程序中的详细指南。
section: 7. 库组件
---

# Vue 组件

<Info>
  本示例适用于 Vue 3.2+（使用 `<script setup>` 的 Composition API）。
</Info>

为了演示，让我们为 Vanilla Calendar Pro 创建一个简单的 Vue 组件。创建一个名为 `VanillaCalendar.vue` 的文件，并将以下代码复制到其中：

```vue
<script setup lang="ts">
import { onMounted, ref, useAttrs } from 'vue';
import { Calendar, Options } from 'vanilla-calendar-pro';
import 'vanilla-calendar-pro/styles/index.css'

const calendarRef = ref(null);
const attributes = useAttrs();
const { config } = defineProps<{ config?: Options }>();

onMounted(() => {
  if (!calendarRef.value) return;
  const calendar = new Calendar(calendarRef.value, config);
  calendar.init();
});
</script>

<template>
  <div v-bind="attributes" ref="calendarRef"></div>
</template>
```

然后将创建的 `VanillaCalendar` 组件导入到您想要显示日历的 Vue 应用程序中。

```vue
<script setup lang="ts">
// ...
import VanillaCalendar from './VanillaCalendar.vue';
// ...
</script>
```

使用创建的组件。

```vue
<template>
  <!-- -->
  <VanillaCalendar />
  <!-- -->
</template>
```

`VanillaCalendar` 组件可以接受 `<div>` 标签支持的任何 HTML 属性，以及用于日历配置的 `config` 参数。

```vue
<template>
  <!-- -->
  <VanillaCalendar :config="{ type: 'multiple' }" />
  <!-- -->
</template>
```

```

### `docs/zh/learn/components-for-libraries-web-component.mdx`

```mdx
---
title: Web 组件
description: 学习如何将 Vanilla Calendar Pro 封装为原生 Web 组件，以及用于完全隔离样式和 DOM 的可选 Shadow DOM 方案。
section: 7. 库组件
---

# Web 组件

<Info>
  Web 组件是一种原生的、与框架无关的自定义 HTML 元素。注册后，它在任何框架或纯 HTML 中的表现完全一致，无需额外的封装库。
</Info>

## 普通 Web 组件

出于演示目的，让我们考虑封装 Vanilla Calendar Pro 的最简单原生 Web 组件。创建一个名为 `VanillaCalendarElement.ts` 的文件，并将以下代码复制到其中：

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    this.calendar = new Calendar(this, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

该自定义元素直接将日历渲染到自身的（light）DOM 中——无需任何额外设置，`disconnectedCallback` 会调用 `calendar.destroy()`，因此每当自定义元素从页面中移除时，日历都会自行清理。

注册完成后，即可在任何框架或不使用任何框架的 HTML 中的任意位置使用该自定义元素：

```html
<vanilla-calendar-element></vanilla-calendar-element>
```

## 带 Shadow DOM 的 Web 组件

如果你需要完全隔离样式和 DOM——例如，要把日历放进设计系统组件中，同时避免其 CSS 泄漏出去或与宿主页面的样式冲突——可以改为附加一个 Shadow DOM。Vanilla Calendar Pro 完全支持在 Shadow DOM 内部初始化：弹出层会被添加到正确的根节点，点击和焦点会相对于 shadow 边界进行跟踪，系统主题监听器也会按实例单独作用域化。无需任何特殊选项。

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

class VanillaCalendarElement extends HTMLElement {
  calendar?: Calendar;

  connectedCallback() {
    const shadow = this.attachShadow({ mode: 'open' });

    // the calendar's own CSS has to be loaded inside the shadow root too, since
    // styles in the outer document don't cross the shadow boundary
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css';
    shadow.appendChild(link);

    const container = document.createElement('div');
    shadow.appendChild(container);

    const options: Options = {
      onClickDate(self) {
        console.log(self.context.selectedDates);
      },
    };

    // pass the element directly rather than a string selector: a string selector is
    // resolved with document.querySelector, which can't reach inside a Shadow DOM
    this.calendar = new Calendar(container, options);
    this.calendar.init();
  }

  disconnectedCallback() {
    if (this.calendar) this.calendar.destroy();
  }
}

customElements.define('vanilla-calendar-element', VanillaCalendarElement);
```

有几点值得说明：

- 日历的样式表通过一个直接添加到 shadow root 内部的 `<link>` 元素加载，因为外部文档中声明的样式无法穿过 shadow 边界。
- 容器是以元素本身而非字符串选择器的形式传给 `new Calendar(...)` 的：字符串选择器是通过 `document.querySelector` 解析的，而它无法访问 Shadow DOM 内部。

```

### `docs/zh/learn/date-management-date-min-and-max.mdx`

```mdx
---
title: 最大和最小日期
description: 学习如何使用 dateMin 和 dateMax 参数在日历中设置日期范围。配置最小和最大日期以限制允许的范围。
section: 4. 管理日期和时间
---

# 最大和最小日期

日历中的日期范围可以使用 `dateMin` 和 `dateMax` 参数设置。这些参数指定日历中允许的日期范围。

默认情况下，最小日期是 `'1970-01-01'`，对应于 <a href="https://en.wikipedia.org/wiki/Unix_time" rel="noopener noreferrer" target="_blank">UNIX 时间</a> 的开始。
默认情况下，最大日期设置为 `'2470-12-31'`，并且是任意选择的。

如果您需要设置特定的可能日期范围，请将 `dateMin` 和 `dateMax` 参数的值替换为您需要的日期。请注意，日历不会处理指定范围之外的日期。

<Sandbox example="date-management-date-min-and-max" />

```

### `docs/zh/learn/date-management-display-range-dates.mdx`

```mdx
---
title: 显示日期范围
description: 学习如何使用 displayDateMin 和 displayDateMax 参数在日历中设置显示的日期范围。配置指定范围内的日期显示和选择。
section: 4. 管理日期和时间
---

# 显示日期范围

`displayDateMin` 和 `displayDateMax` 参数定义了可以在日历中显示的日期范围，但不影响日历的生命周期。它们仅指示哪些日期允许显示和选择。

例如，如果 `displayDisabledDates` 参数设置为 `true`，则用户可查看的最小和最大年份将由 `dateMin` 和 `dateMax` 参数的值确定。

<Sandbox example="date-management-display-range-dates" />

更改 `displayDisabledDates` 参数允许您控制日历中可供查看和选择的日期。

```

### `docs/zh/learn/date-management-enable-or-disable-days.mdx`

```mdx
---
title: 启用或禁用日期
description: 学习如何在日历中禁用或启用特定日期。根据您的需求配置日期的可用性以供选择。
section: 4. 管理日期和时间
---

# 启用或禁用日期

您可能需要禁用某些日期，使其不可用于选择。

<Sandbox example="date-management-disable-dates" />

有时，禁用所有日期并启用特定日期可能比列出禁用的日期更容易。

<Sandbox example="date-management-enable-dates" />

```

### `docs/zh/learn/date-management-enable-time-picker.mdx`

```mdx
---
title: 启用时间选择
description: 学习如何在日历中启用和配置时间选择。支持 12 小时和 24 小时格式，设置初始时间，管理时间范围和步长。
section: 4. 管理日期和时间
---

# 启用时间选择

默认情况下，时间选择是禁用的，但您可以轻松启用它并根据您的需求进行配置。

## 12 小时制带 AM/PM

您可以启用 12 小时时间格式并添加 AM/PM 标记。

<Sandbox example="date-management-enable-time-picker-12" height={400} />

## 24 小时制

如果您需要不带 AM/PM 的 24 小时时间格式，可以按如下方式配置。

<Sandbox example="date-management-enable-time-picker-24" height={400} />

## 设置您自己的时间

您可以在初始化日历时设置初始时间。对于 24 小时制，您不需要指定 AM/PM 标记。

<Sandbox example="date-management-enable-time-picker-your-time" height={400} />

## 管理时间范围

您可以设置可能的时间范围。

<Sandbox example="date-management-enable-time-picker-range" height={400} />

## 管理时间步长

除了所有其他功能外，您还可以配置分钟和小时的时间步长。您还可以禁用手动在输入字段中输入时间的功能。

<Sandbox example="date-management-enable-time-picker-control" height={400} />

```

### `docs/zh/learn/date-management-forbid-choice.mdx`

```mdx
---
title: 禁用日期、月份和年份选择
description: 学习如何在日历中禁用选择日期、月份或年份的功能。根据您的需求配置日历。
section: 4. 管理日期和时间
---

# 禁用日期、月份和年份选择

日历允许您轻松地单独禁用选择日期、月份或年份的功能。

<Sandbox example="date-management-forbid-choice" />

```

### `docs/zh/learn/date-management-other-today.mdx`

```mdx
---
title: 自定义今天
description: 学习如何在日历中指定不同的日期作为今天。根据您的需求配置日历。
section: 4. 管理日期和时间
---

# 自定义今天

日历提供了指定哪个日期应被视为今天的功能。

<Sandbox example="date-management-other-today" />

```

### `docs/zh/learn/date-management-selected-days-month-year.mdx`

```mdx
---
title: 初始化时选择的日期、月份和年份
description: 学习如何在初始化日历时指定选择的日期、月份和年份。根据您的需求配置日历。
section: 4. 管理日期和时间
---

# 初始化时选择的日期、月份和年份

日历允许您在初始化时明确指定选择的日期，以及将显示的月份和年份，无论当前日期如何。

如果您需要预选某些日期并设置特定的月份和年份，这非常有用。

<Sandbox example="date-management-selected-days-month-year" />

```

### `docs/zh/learn/handle-click-a-day.mdx`

```mdx
---
title: 处理日期点击
description: 学习如何使用 onClickDate() 操作处理日历中日期的点击。配置选择单个日期或日期范围的处理。
section: 5. 操作处理程序
---

# 处理日期点击

为了用户与日历的交互，提供了各种操作，其中之一是 `onClickDate()`。此操作允许您跟踪用户何时单击日历中的特定日期。

将所选日期输出到控制台的示例：

<Sandbox example="handle-click-a-day" />

请注意，所选日期表示为数组，因为如果日历参数允许，用户不仅可以选择单个日期，还可以选择日期范围。

<Sandbox example="handle-click-a-day-ranged" />

```

### `docs/zh/learn/handle-click-on-a-month-in-the-month-selection.mdx`

```mdx
---
title: 处理月份列表中的月份点击
description: 学习如何处理月份列表中的月份点击。获取有关所选月份及其索引的信息。
section: 5. 操作处理程序
---

# 处理月份列表中的月份点击

当在所有月份的列表中单击月份时，您可以处理此事件并获取有关所选元素及其索引的信息。

<Info>需要注意的是，根据 JS 标准，月份从零开始编号，其中一月对应第零个月，十二月对应第十一个月。</Info>

<Sandbox example="handle-click-on-a-month-in-the-month-selection" />

```

### `docs/zh/learn/handle-click-on-the-arrows.mdx`

```mdx
---
title: 处理箭头点击
description: 学习如何处理箭头点击以在日历中切换月份或年份。根据您的需求配置事件处理。
section: 5. 操作处理程序
---

# 处理箭头点击

当单击任何箭头时，会发生切换日历中月份或年份的事件。此事件可以根据您的需求使用。

<Sandbox example="handle-click-on-the-arrows" />

```

### `docs/zh/learn/handle-click-on-the-year-in-the-year-selection.mdx`

```mdx
---
title: 处理年份选择中的年份点击
description: 学习如何处理年份列表中的年份点击。获取有关所选年份及其编号的信息。
section: 5. 操作处理程序
---

# 处理年份选择中的年份点击

就像选择月份一样，您可以通过单击日历中的年份标题来选择年份。

当从列表中单击年份时，您可以获取有关被单击的所选元素的信息，以及年份编号。

<Sandbox example="handle-click-on-the-year-in-the-year-selection" />

```

### `docs/zh/learn/handle-click-on-weekday-and-the-week-number.mdx`

```mdx
---
title: 处理星期几和周数点击
description: 学习如何处理日历中星期几和周数的点击。配置事件处理以选择与所选星期几相关的月份中的所有日期，或选择所选周中的日期。
section: 5. 操作处理程序
---

# 处理星期几和周数点击

## 星期几

您可以拦截对星期几的点击，例如，选择与该星期几对应的月份中的所有日期。

<Sandbox example="handle-click-on-weekday" />

## 周数

您可以使用 `enableWeekNumbers` 参数在日历中显示周数，并处理对它们的点击。拥有所选周中日期的信息，您可以以相同的方式轻松选择这些日期。

<Sandbox example="handle-click-on-the-week-number" />

```

### `docs/zh/learn/handle-get-and-change-every-day.mdx`

```mdx
---
title: 获取和修改每个日期
description: 学习如何获取和修改日历中的每个日期。执行各种操作，添加附加信息或对每个日期进行更改。
section: 5. 操作处理程序
---

# 获取和修改每个日期

通过访问日历中的每个日期，您可以执行各种操作，添加附加信息或对每个日期进行更改。

例如，您可以为每个日期添加随机成本或值。

<Sandbox example="handle-get-and-change-every-day" height={370} />

```

### `docs/zh/learn/handle-select-and-change-of-time.mdx`

```mdx
---
title: 选择和更改时间
description: 学习如何在日历中激活和处理时间的选择和更改。每次时间更改时获取数据。
section: 5. 操作处理程序
---

# 选择和更改时间

通过激活 `selectionTimeMode` 参数，您将能够自动接收每次时间更改所需的必要数据。

<Sandbox example="handle-select-and-change-of-time" height={400} />

```

### `docs/zh/learn/installation-and-usage.mdx`

```mdx
---
title: 安装和使用
description: 学习如何安装和使用 Vanilla Calendar Pro。通过包管理器或 CDN 集成日历，并根据您的需求进行配置。
section: 1. 开始使用
---

# 安装和使用

Vanilla Calendar Pro 可以轻松集成到任何项目中。根据您管理依赖项和构建项目的方式，有几种安装方法。

## 通过包管理器安装

安装 Vanilla Calendar Pro 最常见的方法是使用包管理器。这种方法非常适合使用 Node.js 和现代构建工具的项目。

1. 安装包：

```bash
npm install vanilla-calendar-pro
# 或
yarn add vanilla-calendar-pro
# 或
pnpm add vanilla-calendar-pro
```

2. 在文档的 body 中创建一个带有任意 CSS 选择器的 HTML 元素：

```html
<html>
  <head>
  </head>
  <body>
    <div id="calendar"></div>
  </body>
</html>
```

<Info>在本节的演示目的中，我们将使用 `#calendar` 作为 CSS 选择器，但您可以创建和使用任何其他选择器。</Info>

3. 在您的 JavaScript 或 TypeScript 文件中导入脚本，创建日历实例并初始化它。

```ts
import { Calendar } from 'vanilla-calendar-pro';

const calendar = new Calendar('#calendar', {
  // 您的设置
});
calendar.init();
```

4. 在同一文件中导入样式。`index.css` 文件包含日历的布局网格，以及浅色和深色主题。

```ts
import 'vanilla-calendar-pro/styles/index.css';
```

您也可以选择分别包含布局和主题样式，如下所示：

```ts
import 'vanilla-calendar-pro/styles/layout.css'; // 仅骨架
import 'vanilla-calendar-pro/styles/themes/light.css'; // 浅色主题
import 'vanilla-calendar-pro/styles/themes/dark.css'; // 深色主题
// 或任何其他自定义主题...
```

5. 没有任何自定义设置的简单初始化的完整示例：

<Sandbox example="installation-and-usage" />

<Info>正如您可能在此示例中注意到的，我们使用的是扁平日历视图，而不使用 **«输入»** 字段，如果您对如何将日历集成到 **«输入»** 中感兴趣，请查看 [此示例](/zh/docs/learn/type-default#with-input)。</Info>

## 本地或 CDN

如果您需要快速集成 Vanilla Calendar Pro 而不使用构建工具或包管理器，可以通过 CDN 包含它，或 <a href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro@latest/package.zip" rel="noopener noreferrer" target="_blank">下载存档</a> 最新版本并在本地包含它。

```html
<html>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/styles/index.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/vanilla-calendar-pro/index.js" defer></script>
  </head>
  <body style="display: flex; align-items: start">
    <div id="calendar"></div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        // 解构 Calendar 构造函数
        const { Calendar } = window.VanillaCalendarPro;
        // 创建日历实例并初始化它。
        const calendar = new Calendar('#calendar');
        calendar.init();
      });
    </script>
  </body>
</html>
```

```

### `docs/zh/learn/internationalization-locale.mdx`

```mdx
---
title: 本地化
description: 学习如何使用 locale 参数本地化日历，或通过提供月份和星期几名称的数组手动设置区域设置。
section: 3. 国际化
---

# 本地化

如果您的区域设置受 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleString" rel="noopener noreferrer" target="_blank">`.toLocaleString()`</a> 方法支持，您可以简单地将其传递给 `locale` 参数来本地化日历。

<Sandbox example="internationalization-locale" />

如果区域设置不受支持或翻译不正确，您可以随时手动设置区域设置。为此，您需要提供月份和星期几名称的数组，而不是语言标签。

<Sandbox example="internationalization-assign-manually" />

```

### `docs/zh/learn/internationalization-week-numbers.mdx`

```mdx
---
title: 周数
description: 学习如何通过将 enableWeekNumbers 参数设置为 true 来启用日历中周数的显示。
section: 3. 国际化
---

# 周数

在某些国家/地区，使用周数来表示日期。
您可以通过将 `enableWeekNumbers` 参数设置为 `true` 来启用日历中周数的显示。

<Sandbox example="internationalization-week-numbers" />

```

### `docs/zh/learn/internationalization-weekday-first-and-weekdays.mdx`

```mdx
---
title: 周起始日和周末
description: 学习如何在日历中配置周起始日和周末。更改 ISO 8601 标准，并将任何星期几指定为周末或禁用它们。
section: 3. 国际化
---

# 周起始日和周末

默认情况下，日历基于欧洲标准 **ISO 8601**。这意味着周的第一天是星期一。

使用单独的参数来定义周的第一天和显示的周末，您可以将任何一天指定为周的第一天，并将任何星期几指定为周末，或通过指定空数组完全禁用它们。

<Sandbox example="internationalization-weekday-first-and-weekdays" />

```

### `docs/zh/learn/internationalization-weekends-and-holidays.mdx`

```mdx
---
title: 额外周末和节假日
description: 学习如何在日历中指定额外的周末和节假日。通过手动设置将这些日期标记为红色。
section: 3. 国际化
---

# 额外周末和节假日

在日历中，您可以指定额外的周末或节假日，这些日期将被标记为红色。这些日期应手动设置。

<Sandbox example="internationalization-weekends-and-holidays" />

```

### `docs/zh/learn/type-default.mdx`

```mdx
---
title: 默认（单日）
description: 学习如何使用 'default' 日历类型来显示一个月并选择日期。配置日历以在单击带有 inputMode 参数的元素时显示。
section: 2. 日历类型
---

# 默认（单日）

## 静态

`'default'` 日历类型显示一个月，允许您选择日期，使用箭头在月份之间导航，并从相应的标题中选择月份和年份。这是日历的标准显示模式。

<Sandbox example="type-default" />

## 带输入框

如果您需要在单击 **«输入»** 时显示日历，可以通过使用 `inputMode: true` 参数初始化来轻松配置它。

<Info>
  需要注意的是，在此日历的上下文中，**«输入»** 不一定是 `<input>` 标签。它可以是任何 HTML 元素，例如 `<div>`。在 **«输入»** 中，您可以初始化任何类型的日历。
</Info>

默认情况下，日历不会向 **«输入»** 字段写入任何值，让您完全控制希望在 `value` 中看到的内容。

<Sandbox example="type-default-in-input" height={470} input={true} />

```

### `docs/zh/learn/type-month.mdx`

```mdx
---
title: 月份
description: 学习如何使用 'month' 日历类型来显示月份列表并选择月份和年份。将用户的选择限制为仅月份和年份。
section: 2. 日历类型
---

# 月份

`'month'` 日历类型显示月份列表，并允许用户从相应的标题中选择月份和年份。如果您需要将用户的选择限制为仅月份和年份，而无法选择特定日期，则此模式非常有用。

<Sandbox example="type-month" />

```

### `docs/zh/learn/type-multiple.mdx`

```mdx
---
title: 多选
description: 学习如何使用 'multiple' 日历类型来显示多个月份并选择日期。使用 selectionDatesMode 参数配置日期范围选择。
section: 2. 日历类型
---

# 多选

`'multiple'` 日历类型显示多个月份，允许您在其中的每一个月份中选择日期。当用户需要在不同月份中选择多个日期时，这种类型的日历非常有用。为此，您需要使用 `selectionDatesMode` 参数并将其值设置为 `'multiple'`。

创建 `'multiple'` 类型日历的示例代码：

<Sandbox example="type-multiple" vertically={false} height={680} />

如果您需要选择日期范围，可以使用 `selectionDatesMode` 参数并将其值设置为 `'multiple-ranged'`。这允许您选择日期范围而不是单个日期。

<Info>当 `selectionDatesMode` 参数设置为 `'multiple-ranged'` 时，为了性能优化，所选日期的数组仅包含开始和结束日期。您可以使用 `enableEdgeDatesOnly` 禁用此功能并获取完整的所选日期列表。</Info>

<Sandbox example="type-multiple-ranged" vertically={false} height={680} />

```

### `docs/zh/learn/type-week.mdx`

```mdx
---
title: 周
new: true
description: 学习如何使用 'week' 日历类型只显示一周而不是整月，以及箭头如何按周翻页。
section: 2. 日历类型
---

# 周

`'week'` 日历类型只显示一周，而不是整个月份。它适合预约流程，以及任何月份网格占用的空间超出选择本身价值的界面。

如果第一个选中日期属于当前显示月份，周条会停在包含该日期的那一周。否则，如果今天属于该月份，就使用今天所在的周；最后才取包含 `selectedMonth` 首日的那一周。

<Sandbox example="type-week" height={300} />

箭头每次翻动一周，并会带着周条跨越月份边界。所有日期都按当前周期的日期渲染，因此不会有任何一天被当作月外日期而变灰，点击某一天也不会让周条移动。

<Info>跨越两个月的一周，会以拥有它的月份来命名——也就是包含其第四天的那个月，这与判定 ISO 周数的规则一致。</Info>

## 把整月折叠为一周

`enableCollapse` 会在网格下方添加一个在月与周之间切换的控件，让访问者自己选择视图，而不是由你决定。详见[折叠](/docs/learn/additional-features-collapse)。

这些控件同样适用于 `inputMode`。下面的弹出日历会以周视图打开，可通过 `enableCollapse` 展开为整月，并通过 `enableSwipe` 翻动当前视图。

<Sandbox example="type-week-in-input" height={470} input={true} />

## 用代码切换

折叠会设置 `type`，因此这两个视图在你自己的代码里同样可达。

```ts
calendar.set({ type: 'week' }); // 折叠为一周
calendar.set({ type: 'default' }); // 回到整月
calendar.type; // 折叠状态下为 'week'
```

<Info>该类型的 `displayMonthsCount` 始终为 `1`，不支持并排显示多周。如果需要多个网格，请使用 `type: 'multiple'`。</Info>

```

### `docs/zh/learn/type-year.mdx`

```mdx
---
title: 年份
description: 学习如何使用 'year' 日历类型来显示年份列表并选择年份和月份。将用户的选择限制为仅年份和月份。
section: 2. 日历类型
---

# 年份

`'year'` 日历类型显示年份列表，允许用户从列表中选择年份，并从相应的标题中选择月份。如果您需要将用户的选择限制为仅年份和月份，而无法选择特定日期，则此模式非常有用。

<Sandbox example="type-year" />

```

### `docs/zh/reference.mdx`

```mdx
---
title: 指南概述
description: 页面描述
---

# 指南概述

本节提供有关使用 **Vanilla Calendar Pro API** 的详细文档。如果您正在寻找功能介绍，请查看 [«学习»](/zh/docs/learn) 部分。

Vanilla Calendar Pro API 文档分为几个功能子部分：

1. **实例创建** — 如何以及在何处创建日历实例。
2. **实用工具** — 允许您格式化日期的函数。
3. **方法** — 用于处理日历实例的可用方法。
4. **设置** — 可以提供的所有选项，用于更改日历的行为和显示。
5. **操作** — 事件处理程序，允许您接收和处理与日历的各种交互数据。
6. **弹出窗口** — 弹出窗口允许您选择任何日期，并在悬停该日期时直接在日历中显示有关它的简要信息。
7. **布局** — 允许您实际更改日历的整个 DOM 结构并添加您自己的 HTML 元素的模板。
8. **样式** — 用于设置日历样式的 CSS 类对象。它允许您使用任何 CSS 框架，如 Tailwind CSS，或自定义类。
9. **Aria 标签** — 用于 `aria-label` 的字符串对象。允许您本地化所有日历标签以确保可访问性。

```

### `docs/zh/reference/actions.mdx`

```mdx
---
title: 操作
description: 了解可以为日历配置的各种操作，包括日期、周、月份、年份和箭头的点击事件处理程序，以及时间更改和工具提示显示。
section: 5
---

# 操作

## onClickDate()

`类型: 函数`

`默认: null`

`选项: onClickDate(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickDate(self, event) {},
});
```

此方法在单击日历中的日期后触发。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `event` - 鼠标事件。

<Info>
  重要的是要知道每个 HTML 日期元素都包含一个数据属性，其中包含格式为 `YYYY-MM-DD` 的完整日期。
  如果您需要分别获取日、月和年，可以使用标准的 JS 方法。
  例如：`new Date('2022-11-07').getDate()` 将返回 `7`。
</Info>

---

## onClickWeekDay()

`类型: 函数`

`默认: null`

`选项: onClickWeekDay(self, day, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekDay(self, day, dateEls, event) {},
});
```

此方法在单击日历中的星期几后触发。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `day` - 星期几；
- `dateEls` - 日期数组（HTML 元素）；
- `event` - 鼠标事件。

---

## onClickWeekNumber()

`类型: 函数`

`默认: null`

`选项: onClickWeekNumber(self, number, year, dateEls, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickWeekNumber(self, number, year, dateEls, event) {},
});
```

此方法在单击日历中的周数后触发，但要使它工作，`enableWeekNumbers` 参数必须设置为 `true`。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `number` - 周数；
- `year` - 周的年份；
- `dateEls` - 日期数组（HTML 元素）；
- `event` - 鼠标事件。

---

## onClickTitle()

`类型: 函数`

`默认: null`

`选项: onClickTitle(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickTitle(self, event) {},
});
```

此方法在单击日历中的月份或年份标题后触发。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `event` - 鼠标事件。

---

## onClickMonth()

`类型: 函数`

`默认: null`

`选项: onClickMonth(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickMonth(self, event) {},
});
```

此方法在日历中选择月份后触发。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `event` - 鼠标事件。

---

## onClickYear()

`类型: 函数`

`默认: null`

`选项: onClickYear(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickYear(self, event) {},
});
```

此方法在日历中选择年份后触发。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `event` - 鼠标事件。

---

## onClickArrow()

`类型: 函数`

`默认: null`

`选项: onClickArrow(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onClickArrow(self, event) {},
});
```

此方法在单击日历中的箭头后触发。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `event` - 鼠标事件。

---

## onChangeTime()

`类型: 函数`

`默认: null`

`选项: onChangeTime(self, event, isError) => void | null`

```ts
new Calendar('#calendar', {
  onChangeTime(self, event) {},
});
```

此方法在更改日历中的时间后触发。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `event` - 更改事件；
- `isError` - 如果用户输入了不正确的时间，则返回 true。

---

## onChangeToInput()

`类型: 函数`

`默认: null`

`选项: onChangeToInput(self, event) => void | null`

```ts
new Calendar('#calendar', {
  onChangeToInput(self, event) {},
});
```

要使此方法工作，`inputMode` 参数必须设置为 `true`。
此方法在单击日历中的日期或以任何方式更改时间后触发。
您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `event` - 事件。

---

## onCreateDateRangeTooltip()

`类型: 函数`

`默认: null`

`选项: onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainElBCR) {},
});
```

允许为日期范围创建工具提示。如果 `selectionDatesMode` 参数设置为 `'multiple-ranged'`，则在单击和悬停日期时触发。
您可以获取以下参数：
- `self` - 对初始化日历的引用。
- `dateEl` - HTML 日期元素；
- `tooltipEl` - HTML 工具提示元素；
- `dateElBCR` - 包含 HTML 日期元素位置和大小信息的对象；
- `mainElBCR` - 包含主 HTML 日历元素位置和大小信息的对象。

---

## onCreateDateEls()

`类型: 函数`

`默认: null`

`选项: onCreateDateEls(self, dateEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateDateEls(self, dateEl) {},
});
```

此方法在日历初始化和任何更改期间触发。它提供对每个日期的信息的访问。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `dateEl` - HTML 日期元素。

---

## onCreateMonthEls()

`类型: 函数`

`默认: null`

`选项: onCreateMonthEls(self, monthEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateMonthEls(self, monthEl) {},
});
```

此方法在日历类型设置为 `'month'` 时触发。当用户单击月份标题或在初始化时使用参数 `type = 'month'` 时，日历类型也会变为 `'month'`。它提供对每个月份信息的访问。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `monthEl` - HTML 月份元素。

---

## onCreateYearEls()

`类型: 函数`

`默认: null`

`选项: onCreateYearEls(self, yearEl) => void | null`

```ts
new Calendar('#calendar', {
  onCreateYearEls(self, yearEl) {},
});
```

此方法在日历类型设置为 `'year'` 时触发。当用户单击年份标题或在初始化时使用参数 `type = 'year'` 时，日历类型变为 `'year'`。它提供对每个年份信息的访问。您可以获取以下参数：
- `self` - 对初始化日历的引用；
- `yearEl` - HTML 年份元素。

---

## onInit()

`类型: 函数`

`默认: null`

`选项: onInit(self) => void | null`

```ts
new Calendar('#calendar', {
  onInit(self) {},
});
```

此方法在日历初始化期间触发。如果 `inputMode` 参数设置为 `true`，该方法将在日历首次显示时执行，因为这是日历初始化的时间。
- `self` - 对初始化日历的引用。

---

## onUpdate()

`类型: 函数`

`默认: null`

`选项: onUpdate(self) => void | null`

```ts
new Calendar('#calendar', {
  onUpdate(self) {},
});
```

此方法在使用 `.update()` 方法更新/重置日历时触发。
- `self` - 对初始化日历的引用。

---

## onDestroy()

`类型: 函数`

`默认: null`

`选项: onDestroy(self) => void | null`

```ts
new Calendar('#calendar', {
  onDestroy(self) {},
});
```

此方法在日历销毁时触发。
- `self` - 对初始化日历的引用。

---

## onShow()

`类型: 函数`

`默认: null`

`选项: onShow(self) => void | null`

```ts
new Calendar('#calendar', {
  onShow(self) {},
});
```

此方法在日历显示给用户时触发，但仅当 `inputMode` 参数设置为 `true` 时。
- `self` - 对初始化日历的引用。

---

## onHide()

`类型: 函数`

`默认: null`

`选项: onHide(self) => void | null`

```ts
new Calendar('#calendar', {
  onHide(self) {},
});
```

此方法在日历隐藏时触发，但仅当 `inputMode` 参数设置为 `true` 时。
- `self` - 对初始化日历的引用。

```

### `docs/zh/reference/creating-an-instance.mdx`

```mdx
---
title: 创建实例
description: 学习如何使用 CSS 选择器或 HTML 元素创建 Vanilla Calendar Pro 的实例。配置日历以在单击元素时在包装器或弹出窗口中初始化。
section: 1
---

# 创建实例

`new Calendar()` - 创建 **Vanilla Calendar Pro** 的实例，该实例是日历、其设置和方法的封装。

<Info>如果您使用 `<script>` 标签包含了 **Vanilla Calendar Pro**，则该对象可作为全局变量 **window.VanillaCalendarPro** 使用。</Info>

`Calendar` 实例接受两个参数。第一个**必需**参数可以是 **CSS 选择器**或 **HTML 元素**。

**CSS 选择器**或 **HTML 元素**可以表示日历的包装器，日历将在其中初始化，或者表示 **«输入»**。

日历包装器是一个 `<div>` 标签，日历本身将在其中初始化。

在日历包装器中初始化：

```html
<div id="calendar"></div>
```

```ts
new Calendar('#calendar');
// 或
const calendarEl = document.querySelector('#calendar');
new Calendar(calendarEl);
```

**«输入»** 在此日历的上下文中不一定意味着 `<input>` 标签；它可以是任何 HTML 元素，例如 `<div>`。

当单击 **«输入»** 时，将出现带有日历的弹出窗口。

在 **«输入»** 中初始化：

```html
<input type="text" id="input">
<!-- 或 -->
<div id="input"></div>
```

```ts
new Calendar('#input', { inputMode: true });
// 或
const calendarInput = document.querySelector('#input');
new Calendar(calendarInput, {
  inputMode: true,
});
```

第二个**可选**参数是一个对象，定义日历的设置和操作。

```ts
new Calendar('#calendar', {
  // 设置
});
```

```

### `docs/zh/reference/labels.mdx`

```mdx
---
title: Aria 标签
description: Aria 标签允许您为可访问性本地化日历中的所有 aria-labels。
section: 9
---

# Aria 标签

`labels` 提供了为可访问性本地化日历中所有 aria-labels 的能力。

以下是所有默认 aria-labels 的列表。

```ts
new Calendar('#calendar', {
  labels: {
    application: '日历',
    navigation: '日历导航',
    arrowNext: {
      month: '下个月',
      year: '下一年份列表',
      week: '下一周',
    },
    arrowPrev: {
      month: '上个月',
      year: '上一年份列表',
      week: '上一周',
    },
    month: '选择月份，当前选中的月份：',
    months: '月份列表',
    year: '选择年份，当前选中的年份：',
    years: '年份列表',
    week: '一周中的天数',
    weekNumber: '一年中的周数',
    collapse: '折叠为一周',
    expand: '展开为整月',
    dates: '当前月份中的日期',
    selectingTime: '选择时间',
    inputHour: '小时',
    inputMinute: '分钟',
    rangeHour: '选择小时的滑块',
    rangeMinute: '选择分钟的滑块',
    btnKeeping: '切换 AM/PM，当前位置：',
  },
});
```

```

### `docs/zh/reference/layouts.mdx`

```mdx
---
title: 布局
description: 布局允许您更改日历的 DOM 结构并添加您自己的 HTML 元素。
section: 7
---

# 布局

布局允许您几乎完全更改日历的 DOM 结构并添加您自己的 HTML 元素，例如按钮。每种类型的日历都有自己的默认模板，您可以自定义它们中的每一个。

<Info>
  包含符号 **«#»** 的标签是日历的注册组件，应在标签末尾包含闭合斜杠，除了包装一个月的标签 **\<#Multiple>\<#/Multiple>**。
  所有默认模板都列出了该模板的所有可能组件。
</Info>

## layouts.default

`类型: 字符串`

`默认: 字符串`

`选项: 字符串`

```ts
new Calendar('#calendar', {
  layouts: {
    default: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

这是显示一个月及其日期的默认模板。

---

## layouts.multiple

`类型: 字符串`

`默认: 字符串`

`选项: 字符串`

```ts
new Calendar('#calendar', {
  layouts: {
    multiple: `
      <div class="${self.styles.controls}" data-vc="controls" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [month] />
        <#ArrowNext [month] />
      </div>
      <div class="${self.styles.grid}" data-vc="grid">
        <#Multiple>
          <div class="${self.styles.column}" data-vc="column" role="group">
            <div class="${self.styles.header}" data-vc="header">
              <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
                <#Month />
                <#Year />
              </div>
            </div>
            <div class="${self.styles.wrapper}" data-vc="wrapper">
              <#WeekNumbers />
              <div class="${self.styles.content}" data-vc="content">
                <#Week />
                <#Dates />
              </div>
            </div>
          </div>
        <#/Multiple>
        <#DateRangeTooltip />
      </div>
      <#ControlTime />
    `,
  },
});
```

这是显示多个月及其日期的默认模板。

---

## layouts.month

`类型: 字符串`

`默认: 字符串`

`选项: 字符串`

```ts
new Calendar('#calendar', {
  layouts: {
    month: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Months />
        </div>
      </div>
    `,
  },
});
```

这是选择月份的默认模板。

---

## layouts.year

`类型: 字符串`

`默认: 字符串`

`选项: 字符串`

```ts
new Calendar('#calendar', {
  layouts: {
    year: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [year] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [year] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <div class="${self.styles.content}" data-vc="content">
          <#Years />
        </div>
      </div>
    `,
  },
});
```

这是选择年份的默认模板。

---

## layouts.week

`Type: String`

`Default: string`

`Options: string`

```ts
new Calendar('#calendar', {
  layouts: {
    week: `
      <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
        <#ArrowPrev [week] />
        <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [week] />
      </div>
      <div class="${self.styles.wrapper}" data-vc="wrapper">
        <#WeekNumbers />
        <div class="${self.styles.content}" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `,
  },
});
```

这是单周的默认模板。除了箭头按周翻页之外，其余与 `layouts.default` 相同。

```

### `docs/zh/reference/methods.mdx`

```mdx
---
title: 方法
description: 用于管理日历的方法，包括初始化、更新、设置参数、删除、显示和隐藏日历。
section: 3
---

# 方法

## init()

`init()` 方法是主要的实例方法，启动日历初始化过程。

```ts
const calendar = new Calendar(element, params);
calendar.init();
```

---

## update()

`update()` 方法允许您将新设置应用于日历并执行重置。
此方法接受一个带有可选参数的对象来控制重置，默认情况下在更新后重置用户选择的日期、月份和年份。

所有参数默认为 `true`：

```ts
{
  year: boolean;
  month: boolean;
  dates: boolean | 'only-first';
  holidays: boolean;
  time: boolean;
}
```

- `true` - 将重置为设置中指定的参数；
- `false` - 不会执行重置，保留用户选择的参数；
- `'only-first'` - 重置所有选定的日期，只保留最早的日期。如果日期选择类型指定为 `'multiple-ranged'`，则添加 `'mousemove'` 和 `'keydown'` 处理程序以进行悬停。

使用示例：

```ts
calendar.locale = 'de-AT';
calendar.firstWeekday = 0;

calendar.update({
  dates: true,
});
```

---

## set()

如果您需要为尚未初始化或已初始化的日历指定新参数或处理程序，可以使用 `.set()` 方法。
此方法接受一个带有新参数的对象和一个带有可选参数的对象来控制重置，默认情况下在更新后重置用户选择的日期、月份和年份。

使用示例：

```ts
calendar.set({
  locale: 'de-AT',
  firstWeekday: 0,
}, {
  dates: true,
});
```

此方法可以替代在创建日历实例时指定参数。如果您在初始化之前调用此方法，请不要指定用于控制重置的对象。

```ts
const calendar = new Calendar(element);
calendar.set({ locale: 'de-AT', firstWeekday: 0 });
calendar.init();
```

---

## destroy()

如果您需要完全删除日历实例，可以使用 `destroy()` 方法。

```ts
calendar.destroy();
```

---

## show()

`show()` 方法允许您显示日历（如果它被隐藏）。

```ts
calendar.show();
```

---

## hide()

`hide()` 方法允许您隐藏日历（如果它被显示）。

```ts
calendar.hide();
```

```

### `docs/zh/reference/popups.mdx`

```mdx
---
title: 弹出窗口
description: 弹出窗口允许您突出显示任何日期，并在悬停该日期时直接在日历中显示有关它的简要信息。
section: 6
---

# 弹出窗口

弹出窗口允许您突出显示任何日期，并在悬停该日期时直接在日历中显示有关它的简要信息。

## popups['date']

`类型: 字符串`

`默认: null`

`选项: 'YYYY-MM-DD' | 'YYYY-MM-DD:YYYY-MM-DD' | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {},
    '2022-07-01:2022-07-05': {},
  }
});
```

格式为 `YYYY-MM-DD` 的日期用作键。在给定的示例中，为 2022 年 6 月 28 日设置了弹出窗口。

<Info>键也可以是 `'YYYY-MM-DD:YYYY-MM-DD'` 格式的日期范围（两个日期之间可以使用任意分隔符）。这样同一个弹出窗口（`modifier`/`html`）会应用到该范围内的每一天，无需为每个日期重复相同的条目。</Info>

---

## popups['date'].modifier

`类型: 字符串`

`默认: null`

`选项: CSS 类 | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
    },
  }
});
```

`modifier` 接受任意 CSS 类，用空格分隔。使用这些类，您可以设置日期的样式以使其突出显示或更改其外观。

---

## popups['date'].html

`类型: 字符串`

`默认: null`

`选项: '' | HTML | null`

```ts
new Calendar('#calendar', {
  popups: {
    '2022-06-28': {
      modifier: 'bg-red color-pink',
      html: `<div>
        <u><b>12:00 PM</b></u>
        <p style="margin: 5px 0 0;">拉斯维加斯的飞机</p>
      </div>`,
      // 或只是文本
      // html: '拉斯维加斯的飞机',
    },
  }
});
```

`html` 接受纯文本或 HTML 标记以格式化弹出窗口。
在此示例中，当悬停在 2022 年 6 月 28 日上时，将显示一个弹出窗口，其中包含文本"拉斯维加斯的飞机"和时间"12:00 PM"，并且将应用在类 `bg-red` 和 `color-pink` 中指定的样式。

```

### `docs/zh/reference/settings.mdx`

```mdx
---
title: 设置
description: 日历设置，包括显示类型、输入模式、定位、本地化、日期和时间。
new:
  - animation
  - enableCollapse
  - enableSwipe
section: 4
---

# 设置

## type

`类型: 字符串`

`默认: 'default'`

`选项: 'default' | 'multiple' | 'month' | 'year' | 'week'`

```ts
new Calendar('#calendar', {
  type: 'default',
});
```

`type` 参数定义显示的日历类型。`week` 类型显示单独一周而不是整月。它可以单独使用，也可以与 `enableCollapse` 一起使用，让访问者在整月和一周之间切换。

---

## inputMode

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  inputMode: true,
});
```

`inputMode` 参数指示作为第一个参数传递的 `mainElement` 表示输入字段而不是日历的包装器。

---

## openOnFocus

`类型: 布尔值 | 函数`

`默认: true`

`选项: true | false | () => false`

```ts
new Calendar('#calendar', {
  openOnFocus: false,
  // 或使用回调
  openOnFocus: (self) => !self.context.isShowInInputMode,
});
```

如果 `openOnFocus` 参数为 `true` 或回调返回 `true`，则聚焦 input 会打开日历。使用 `false` 或回调来控制此行为并实现您自己的焦点处理器。

---

## positionToInput

`类型: 字符串`

`默认: 'left'`

`选项: 'auto' | 'center' | 'left' | 'right' | ['bottom' | 'top', 'center' | 'left' | 'right']`

```ts
new Calendar('#calendar', {
  positionToInput: 'auto',
  // positionToInput: ['bottom', 'center'],
});
```

此参数定义日历相对于输入的位置，如果日历使用 `inputMode` 参数初始化。

`positionToInput` 接受一个字符串，值为 `'left'`、`'center'` 或 `'right'`，或者一个值数组 `[Y轴, X轴]`，其中 Y 轴可以是 `'bottom'` 或 `'top'`，X 轴可以是 `'left'`、`'center'` 或 `'right'`。
如果未指定 Y 轴，则使用默认值 `'bottom'`。

您可以使用值 `positionToInput: 'auto'` 根据视口中可用空间自动确定最佳位置。
该选项允许计算所有 4 个边的可用空间，并首先尝试在输入下方显示日历，这是默认位置。
如果下方空间不足，它将评估另一个最佳可用位置。

---

## animation

`Type: Boolean | Object`

`Default: false`

`Options: true | false | { duration?: Number, easing?: String, slide?: Timing, fade?: Timing, collapse?: Timing }`

`Timing: { duration?: Number, easing?: String }`

```ts
new Calendar('#calendar', {
  animation: true,
  // animation: { duration: 400, easing: 'ease-out' },
  // animation: { slide: { duration: 400 }, fade: { duration: 120 }, collapse: { duration: 300 } },
});
```

为视图之间的切换添加动画。箭头导航和 `enableSwipe` 使用水平滑动，月份与年份选择器使用交叉淡入淡出，`enableCollapse` 则在整月与一周之间对日历高度进行动画。

不同过渡的默认值并不相同——滑动为 `250ms`，交叉淡入淡出为 `150ms`，折叠为 `300ms`，缓动均为 `cubic-bezier(0.4, 0, 0.2, 1)`。传入对象可覆盖其中任意一项：`duration` 的单位是毫秒，`easing` 接受 CSS 缓动函数。顶层的值作用于所有过渡；嵌套在 `slide`（箭头和 `enableSwipe`）、`fade`（选择器）或 `collapse`（`enableCollapse`）下则只作用于该组。嵌套值优先于顶层值。

<Info>当访问者通过 `prefers-reduced-motion: reduce` 要求减少动效时，松手后的过渡动画会被跳过。手势仍会跟随指针，但松手后会立即完成或返回。</Info>

出于向后兼容的考虑，默认值为 `false`：该选项是后来加入的，而开启它会改变滑动和交叉淡入淡出期间的 DOM 查询结果。正在退出的内容仍保留在 DOM 中带有 `inert` 的 `[data-vc-ghost]` 图层内，因此日期元素可能会短暂地出现两份。如果你自己的代码会查询这些元素，请排除该图层；折叠不会创建幽灵图层。

---

## firstWeekday

`类型: 数字`

`默认: 1`

`选项: 从 0 到 6`

```ts
new Calendar('#calendar', {
  firstWeekday: 1,
});
```

此参数设置一周的第一天。指定一个从 0 到 6 的数字，其中数字表示星期几的标识符。根据 JS 标准，星期几从 0 开始，0 是星期日。

---

## monthsToSwitch

`类型: 数字`

`默认: 1`

`选项: 从 1 到 12`

```ts
new Calendar('#calendar', {
  monthsToSwitch: 1,
});
```

`monthsToSwitch` 参数控制可切换月份的数量。

<Info>
  当 `monthsToSwitch` 大于 `1` 时，月份选择视图（month picker）也只允许选择从当前选中月份按 `monthsToSwitch`
  步长可到达的月份——其他月份将显示为禁用状态。这是为了让导航与设定的步长保持一致（在 `type: 'multiple'` 下与 `displayMonthsCount`
  搭配使用时尤为重要，可使多个可见月份保持同步）。
</Info>

---

## themeAttrDetect

`类型: 字符串 | 假`

`默认: 'html[data-theme]'`

`选项: '字符串 | false`

```ts
new Calendar('#calendar', {
  themeAttrDetect: 'html[data-theme]',
});
```

要让日历自动跟踪并应用网站的主题，您可以传递一个字符串值，形式为 CSS 选择器。
方括号表示包含主题名称的属性。
默认情况下，跟踪带有 `data-theme` 属性的 `html` 标签，但您可以配置任何其他属性和标签，例如 `class`，如果类名用于设置主题：`'html[class]'`。
如果设置为 `false`，主题将由用户的系统或 `selectedTheme` 参数确定。

---

## locale

`类型: 字符串`

`默认: 'en'`

`选项: 语言标签 | 数组<区域设置>`

```ts
new Calendar('#calendar', {
  locale: 'en',
  // 或为您的标签指定一个对象
  // locale: {
  //   months: {
  //     long: [],
  //     short: [],
  //   },
  //   weekday: {
  //     long: [],
  //     short: [],
  //   }
  // },
});
```

此参数设置日历的语言本地化。
您可以根据 <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry" target="_blank" rel="nofollow noreferrer">BCP 47</a> 指定语言标签，或提供月份和星期几名称的数组，更多详细信息请参见[此处](/zh/docs/learn/internationalization-locale)。

---

## dateToday

`类型: Date 对象`

`默认: 'today'`

`选项: Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateToday: 'today',
});
```

`dateToday` 参数定义哪个日期将被视为日历的今天。

---

## dateMin

`类型: 字符串`

`默认: '1970-01-01'`

`选项: 'Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMin: '1970-01-01',
});
```

`dateMin` 参数设置日历将考虑的最小允许日期，该日期不能小于此日期。

---

## dateMax

`类型: 字符串`

`默认: '2470-12-31'`

`选项: 'Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  dateMax: '2470-12-31',
});
```

`dateMax` 参数设置日历将考虑的最大允许日期，该日期不能大于此日期。

---

## displayDateMin

`类型: 字符串`

`默认: '1970-01-01'`

`选项: 'Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMin: '2022-07-01',
});
```

此参数设置用户可以选择的最小日期。早于指定日期的日期将被禁用且不可选择。

<Info>需要注意的是，`displayDateMin` 和 `displayDateMax` 禁用范围之外的日期，而 `dateMin` 和 `dateMax` 根本不创建它们。</Info>

<Info>在 `.set()` 中为 `displayDateMin` 传入 `null` 会将其显式重置为默认值。传入 `undefined`（例如省略该属性）则保持当前值不变。</Info>

---

## displayDateMax

`类型: 字符串`

`默认: '2470-12-31'`

`选项: 'Date | number | 'YYYY-MM-DD' | 'today'`

```ts
new Calendar('#calendar', {
  displayDateMax: '2024-07-01',
});
```

此参数设置用户可以选择的最大日期。晚于指定日期的日期将被禁用且不可选择。

<Info>需要注意的是，`displayDateMin` 和 `displayDateMax` 禁用范围之外的日期，而 `dateMin` 和 `dateMax` 根本不创建它们。</Info>

<Info>在 `.set()` 中为 `displayDateMax` 传入 `null` 会将其显式重置为默认值。传入 `undefined`（例如省略该属性）则保持当前值不变。</Info>

---

## displayDatesOutside

`类型: 布尔值`

`默认: true`

`选项: true | false`

```ts
new Calendar('#calendar', {
  displayDatesOutside: false,
});
```

使用此参数，您可以决定是否显示上个月和下个月的日期。

---

## displayDisabledDates

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  displayDisabledDates: false,
});
```

此参数确定是否显示所有日期，包括禁用的日期。

---

## displayMonthsCount

`类型: 数字`

`默认: 2`

`选项: 从 2 到 12`

```ts
new Calendar('#calendar', {
  displayMonthsCount: 2,
});
```

`displayMonthsCount` 参数定义如果日历类型设置为 `'multiple'` 时显示的月份数量。

---

## disableDates

`类型: 字符串[] | 数字[] | 日期[]`

`默认: null`

`选项: ['YYYY-MM-DD'] | [数字] | [日期] | null`

```ts
new Calendar('#calendar', {
  disableDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

此参数允许您禁用指定的日期，无论指定的范围如何。

<Info>要指定日期范围，请在单个字符串内的日期之间使用任何分隔符。</Info>

---

## disableAllDates

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  disableAllDates: true,
});
```

此参数禁用所有日期，在使用 `enableDates` 时可能很有用。

---

## disableDatesPast

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  disableDatesPast: true,
});
```

此参数禁用所有过去的日期。

---

## disableDatesGaps

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  disableDatesGaps: true,
});
```

此参数禁用范围内带有禁用日期的日期选择。仅当 `selectionDatesMode` 参数设置为 `'multiple-ranged'` 时才有效。

---

## disableWeekdays

`类型: 数字`

`默认: []`

`选项: 从 0 到 6`

```ts
new Calendar('#calendar', {
  disableWeekdays: [0, 6],
});
```

此参数允许您禁用指定的星期几。指定一个包含从 0 到 6 的数字的数组，其中每个数字表示星期几的标识符。根据 JS 标准，星期几从 0 开始，0 是星期日。

---

## disableToday

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  disableToday: true,
});
```

使用此参数，您可以禁用日历中今天日期的选择。

---

## enableDates

`类型: 字符串[] | 数字[] | 日期[]`

`默认: null`

`选项: ['YYYY-MM-DD'] | [数字] | [日期] | null`

```ts
new Calendar('#calendar', {
  enableDates: ['2022-08-11:2022-08-16', '2022-08-20', 1722152977141, new Date()],
});
```

此参数允许您启用指定的日期，无论范围和禁用的日期如何。

<Info>要指定日期范围，请在单个字符串内的日期之间使用任何分隔符。</Info>

---

## enableEdgeDatesOnly

`类型: 布尔值`

`默认: true`

`选项: true | false`

```ts
new Calendar('#calendar', {
  enableEdgeDatesOnly: true,
});
```

此参数允许您仅获取用户选择的开始和结束日期，忽略中间日期。此参数仅在 `selectionDatesMode` 设置为 `'multiple-ranged'` 时有效。

<Info>需要注意的是，使用此参数时，日期范围内的禁用日期将无效。因此，仅当您对用户选择的开始和结束日期感兴趣时才使用此选项。</Info>

---

## enableDateToggle

`类型: 布尔值 | 函数`

`默认: true`

`选项: true | false | () => false`

```ts
new Calendar('#calendar', {
  enableDateToggle: false,
  // 或使用回调
  enableDateToggle: (self) => new Date(self.selectedDates[0]) < new Date(),
});
```

如果 `enableDateToggle` 参数为 `true` 或回调返回 `true`，则再次单击选定的日期将取消选择它。

---

## enableWeekNumbers

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  enableWeekNumbers: true,
});
```

使用此参数，您可以决定是否在年份中显示周数。

---

## enableMonthChangeOnDayClick

`类型: 布尔值`

`默认: true`

`选项: true | false`

```ts
new Calendar('#calendar', {
  enableMonthChangeOnDayClick: false,
});
```

使用此参数，您可以决定当单击上个月或下个月的日期时月份是否会切换。

---

## enableJumpToSelectedDate

`类型: 布尔值`

`默认: false`

`选项: true | false`

```ts
new Calendar('#calendar', {
  enableJumpToSelectedDate: true,
  selectedDates: ['2018-05-02'],
});
```

如果启用此选项并指定一个或多个选定日期，但未指定 `selectedMonth` 和 `selectedYear`，日历将跳转到第一个选定日期。如果设置为 `false`，日历将始终打开当前月份和年份。

<Info>如果指定了 `selectedMonth` 和 `selectedYear`，此选项无效。</Info>

---

## enableCollapse

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableCollapse: true,
});
```

在网格下方添加一个控件，把整月折叠为一周，再次操作则展开。如果第一个选中日期属于当前显示月份，就以它所在的周为准；否则，如果今天属于该月份，就以今天所在的周为准；再否则，以当前显示月份第一天所在的周为准。在使用鼠标的设备上显示为箭头，在触摸设备上显示为可上下拖动的小横条。

<Info>`enableCollapse` 不依赖 `enableSwipe` 或 `animation`。折叠会把 `type` 切换为 `'week'`，因此读取 `calendar.type` 即可得知当前状态，而 `set({ type: 'week' })` 会在没有过渡的情况下做同样的事。该选项仅支持 `default` 和 `week` 类型；其他类型会在 `init()` 时抛出错误。</Info>

---

## enableSwipe

`Type: Boolean`

`Default: false`

`Options: true | false`

```ts
new Calendar('#calendar', {
  enableSwipe: true,
});
```

允许访问者横向拖动日历内容来切换到下一个或上一个周期，适用于所有可以用箭头导航的视图：`default`、`multiple`、`week` 和年份列表。相邻周期会跟随指针移动，松手时的距离和速度决定它是落位还是返回。

<Info>
  `enableSwipe` 不依赖 `enableCollapse` 或 `animation`；未启用动画时，松手后会立即落位。日历上的纵向滚动仍然交给页面。只有对应箭头可见时才能滑动，因此手势会遵守
  `dateMin`、`dateMax` 和导航限制。拖动结束时所在的日期不会被选中。
</Info>

---

## selectionDatesMode

`类型: 字符串 | false`

`默认: 'single'`

`选项: 'single' | 'multiple' | 'multiple-ranged' | false`

```ts
new Calendar('#calendar', {
  selectionDatesMode: 'single',
});
```

此参数确定是允许选择一个或多个日期，还是完全禁用日期选择。

---

## selectionMonthsMode

`类型: 布尔值`

`默认: true`

`选项: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionMonthsMode: false,
});
```

此参数允许您禁用月份选择，仅允许使用箭头切换月份，或允许以任何方式切换月份。

---

## selectionYearsMode

`类型: 布尔值`

`默认: true`

`选项: true | false | 'only-arrows'`

```ts
new Calendar('#calendar', {
  selectionYearsMode: false,
});
```

此参数允许您禁用年份选择，仅允许使用箭头切换年份，或允许以任何方式切换年份。

---

## selectionTimeMode

`类型: 假 | 数字`

`默认: false`

`选项: false | 24 | 12`

```ts
new Calendar('#calendar', {
  selectionTimeMode: true,
});
```

此参数启用时间选择。您还可以使用数字指定时间格式：24 小时制或 12 小时制。

---

## selectedDates

`类型: 字符串[] | 数字[] | 日期[]`

`默认: null`

`选项: ['YYYY-MM-DD'] | [数字] | [日期] | null`

```ts
new Calendar('#calendar', {
  selectedDates: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

此参数允许您指定在日历初始化时将选择的日期列表。

<Info>要指定日期范围，请在单个字符串内的日期之间使用任何分隔符。</Info>

---

## selectedMonth

`类型: 数字`

`默认: null`

`选项: 从 0 到 11 | null`

```ts
new Calendar('#calendar', {
  selectedMonth: 0,
});
```

此参数定义在日历初始化时将显示的月份。根据 JS 标准，月份从 0 到 11 编号。参见 [enableJumpToSelectedDate](/zh/docs/reference/settings#enablejumptoselecteddate)，以默认使用第一条选中的日期。

---

## selectedYear

`类型: 数字`

`默认: null`

`选项: 数字 (YYYY) | null`

```ts
new Calendar('#calendar', {
  selectedYear: 2022,
});
```

此参数定义在日历初始化时将显示的年份。参见 [enableJumpToSelectedDate](/zh/docs/reference/settings#enablejumptoselecteddate)，以默认使用第一条选中的日期。

---

## selectedHolidays

`类型: 字符串[] | 数字[] | 日期[]`

`默认: null`

`选项: ['YYYY-MM-DD'] | [数字] | [日期] | null`

```ts
new Calendar('#calendar', {
  selectedHolidays: ['2022-08-10:2022-08-15', '2022-08-20', 1722152977141, new Date()],
});
```

此参数允许您指定将被视为节假日的日期，并将接收额外的数据属性以进行样式设置。

<Info>要指定日期范围，请在单个字符串内的日期之间使用任何分隔符。</Info>

---

## selectedWeekends

`类型: 数字`

`默认: [0, 6]`

`选项: 数字[0-6]`

```ts
new Calendar('#calendar', {
  selectedWeekends: [0, 6],
});
```

此参数允许您指定一周的周末日。指定一个包含从 0 到 6 的数字的数组，其中每个数字表示星期几的标识符。根据 JS 标准，星期几从 0 开始，0 是星期日。

---

## selectedTime

`类型: 字符串`

`默认: null`

`选项: 'hh:mm aa' | null`

```ts
new Calendar('#calendar', {
  selectedTime: '03:44 AM',
});
```

此参数允许您设置在日历初始化时将显示的时间。时间以格式 `'hh:mm aa'` 设置，其中 `'aa'` 是 AM/PM 标记。如果使用 24 小时制，则不需要 `'aa'` 标记。

---

## selectedTheme

`类型: 字符串`

`默认: 'system'`

`选项: 字符串 (自定义主题) | 'light' | 'dark' | 'system'`

```ts
new Calendar('#calendar', {
  selectedTheme: 'system',
});
```

此参数定义日历的主题。默认情况下，主题由用户的系统或网站设置确定。

---

## timeMinHour

`类型: 数字`

`默认: 0`

`选项: 从 0 到 23`

```ts
new Calendar('#calendar', {
  timeMinHour: 0,
});
```

此参数指定哪个小时将是选择的最小值。

---

## timeMaxHour

`类型: 数字`

`默认: 23`

`选项: 从 0 到 23`

```ts
new Calendar('#calendar', {
  timeMaxHour: 23,
});
```

此参数指定哪个小时将是选择的最大值。

---

## timeMinMinute

`类型: 数字`

`默认: 0`

`选项: 从 0 到 59`

```ts
new Calendar('#calendar', {
  timeMinMinute: 0,
});
```

此参数指定哪个分钟将是选择的最小值。

---

## timeMaxMinute

`类型: 数字`

`默认: 59`

`选项: 从 0 到 59`

```ts
new Calendar('#calendar', {
  timeMaxMinute: 59,
});
```

此参数指定哪个分钟将是选择的最大值。

---

## timeControls

`类型: 字符串`

`默认: 'all'`

`选项: 'all' | 'range'`

```ts
new Calendar('#calendar', {
  timeControls: 'all',
});
```

此参数定义时间选择的方法：`'all'`（任何方法）或 `'range'`（仅使用控制器）。

---

## timeStepHour

`类型: 数字`

`默认: 1`

`选项: 从 1 到 23`

```ts
new Calendar('#calendar', {
  timeStepHour: 1,
});
```

此参数设置小时控制器的步长。

---

## timeStepMinute

`类型: 数字`

`默认: 1`

`选项: 从 1 到 59`

```ts
new Calendar('#calendar', {
  timeStepMinute: 1,
});
```

此参数设置分钟控制器的步长。

---

## sanitizerHTML

`类型: 函数`

`默认: (html) => html`

```ts
import DOMPurify from 'dompurify';

new Calendar('#calendar', {
  sanitizerHTML: (html) => DOMPurify.sanitize(html),
});
```

`sanitizerHTML` 可以清理 HTML 模板，使其对 CSP 安全。

<Info>
  请注意，该示例使用第三方库{' '}
  <a href="https://www.npmjs.com/package/dompurify" target="_blank" rel="nofollow noreferrer">
    `dompurify`
  </a>
  。`sanitizerHTML` 不是日历运行所必需的。
</Info>

```

### `docs/zh/reference/styles.mdx`

```mdx
---
title: 样式
description: 使用 styles 参数自定义日历中 CSS 类的综合指南，包括默认类列表及其替换。
section: 8
---

# 样式

`styles` 提供了覆盖日历中任何 CSS 类的能力。您可以用 CSS 类列表替换任何值。

以下是所有默认类的列表。

## CSS 类

```ts
new Calendar('#calendar', {
  styles: {
    // 基础
    calendar: 'vc',
    controls: 'vc-controls',
    grid: 'vc-grid',
    column: 'vc-column',

    // 标题栏
    header: 'vc-header',
    headerContent: 'vc-header__content',
    month: 'vc-month',
    year: 'vc-year',
    arrowPrev: 'vc-arrow vc-arrow_prev',
    arrowNext: 'vc-arrow vc-arrow_next',

    // 月份 / 年份选择器
    wrapper: 'vc-wrapper',
    content: 'vc-content',
    months: 'vc-months',
    monthsRow: 'vc-months__row',
    monthsCell: 'vc-months__cell',
    monthsMonth: 'vc-months__month',
    years: 'vc-years',
    yearsRow: 'vc-years__row',
    yearsCell: 'vc-years__cell',
    yearsYear: 'vc-years__year',

    // 星期行 / 周数
    week: 'vc-week',
    weekDay: 'vc-week__day',
    weekDayBtn: 'vc-week__day-btn',
    weekNumbers: 'vc-week-numbers',
    weekNumbersTitle: 'vc-week-numbers__title',
    weekNumbersContent: 'vc-week-numbers__content',
    weekNumber: 'vc-week-number',

    // 日期
    collapse: 'vc-collapse',
    dates: 'vc-dates',
    datesRow: 'vc-dates__row',
    date: 'vc-date',
    dateBtn: 'vc-date__btn',

    // 弹窗和提示框
    datePopup: 'vc-date__popup',
    dateRangeTooltip: 'vc-date-range-tooltip',

    // 时间控件
    time: 'vc-time',
    timeContent: 'vc-time__content',
    timeHour: 'vc-time__hour',
    timeMinute: 'vc-time__minute',
    timeKeeping: 'vc-time__keeping',
    timeRanges: 'vc-time__ranges',
    timeRange: 'vc-time__range',
  },
});
```

---

## CSS 变量

内置主题（`light`、`dark`、`slate-light`）中的每一种颜色都通过 CSS 自定义属性定义，并以主题的原始颜色作为回退值（fallback）。这意味着您只需设置少量变量即可重新设置日历样式，而无需修改任何 CSS 类，也不必担心主题覆盖是否能正确生效。

```css
:root {
  --vc-date-selected-bg: #7c3aed;
  --vc-date-selected-color: #fff;
}
```

如果变量未设置，日历的渲染效果与之前完全一致——只有当您显式设置某个变量时，效果才会改变。

<Info>在 `:root` 上设置变量会同时应用到所有主题（light/dark/slate-light 都读取相同的变量名）。若只想重新设置某一个主题的样式，请将覆盖限定在该主题的选择器范围内，例如：`[data-vc-theme='dark'] { --vc-date-selected-bg: #7c3aed; }`。</Info>

### 基础

| 变量                       | light      | dark       | slate-light |
| -------------------------- | ---------- | ---------- | ----------- |
| `--vc-bg`                  | white      | slate-900  | slate-100   |
| `--vc-color`               | slate-900  | white      | gray-800    |
| `--vc-focus-outline-color` | orange-300 | orange-300 | blue-300    |

### 头部 / 标题

| 变量                        | light     | dark      | slate-light |
| --------------------------- | --------- | --------- | ----------- |
| `--vc-header-color`         | slate-900 | white     | gray-800    |
| `--vc-title-color`          | slate-900 | white     | gray-800    |
| `--vc-title-color-hover`    | slate-500 | slate-500 | gray-600    |
| `--vc-title-color-disabled` | slate-300 | slate-700 | gray-400    |

### 月份 / 年份选择器

| 变量                               | light     | dark      | slate-light |
| ---------------------------------- | --------- | --------- | ----------- |
| `--vc-months-years-bg`             | white     | slate-900 | slate-100   |
| `--vc-months-years-color`          | slate-500 | white     | gray-600    |
| `--vc-months-years-bg-hover`       | slate-100 | slate-800 | slate-200   |
| `--vc-months-years-color-disabled` | slate-300 | slate-700 | gray-400    |
| `--vc-months-years-bg-selected`    | cyan-500  | slate-500 | blue-500    |
| `--vc-months-years-color-selected` | white     | white     | white       |

### 折叠控件

| 变量                  | light     | dark      | slate-light |
| --------------------- | --------- | --------- | ----------- |
| `--vc-collapse-color` | slate-300 | slate-600 | slate-300   |

### 星期行 / 周数

| 变量                            | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-week-numbers-title-color` | slate-500 | white     | gray-600    |
| `--vc-week-number-color`        | slate-500 | white     | gray-600    |
| `--vc-week-number-color-hover`  | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-color`           | slate-500 | white     | gray-600    |
| `--vc-week-day-color-hover`     | slate-600 | slate-300 | gray-800    |
| `--vc-week-day-off-color`       | rose-500  | rose-500  | red-500     |
| `--vc-week-day-off-color-hover` | rose-600  | rose-600  | red-600     |

### 日期

| 变量                                         | light     | dark      | slate-light |
| -------------------------------------------- | --------- | --------- | ----------- |
| `--vc-date-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-color`                            | slate-900 | slate-400 | gray-800    |
| `--vc-date-color-hover` <sup>dark only</sup> | —         | slate-200 | —           |
| `--vc-date-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-hover-edge-bg`                    | slate-200 | slate-700 | slate-300   |
| `--vc-date-disabled-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-outside-color`                    | slate-400 | slate-600 | gray-400    |
| `--vc-date-today-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-today-color`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-today-outside-color`              | slate-500 | slate-600 | gray-600    |
| `--vc-date-selected-bg`                      | cyan-500  | cyan-500  | blue-500    |
| `--vc-date-selected-color`                   | white     | white     | white       |
| `--vc-date-selected-outside-bg`              | slate-300 | slate-700 | slate-300   |
| `--vc-date-selected-outside-color`           | slate-500 | slate-300 | gray-600    |

### 周末 / 节假日

| 变量                                                         | light     | dark      | slate-light |
| ------------------------------------------------------------ | --------- | --------- | ----------- |
| `--vc-date-weekend-color`                                    | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-bg-hover`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-bg`                                 | rose-50   | slate-800 | slate-200   |
| `--vc-date-weekend-hover-edge-bg`                            | rose-100  | slate-700 | slate-300   |
| `--vc-date-weekend-disabled-color`                           | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-today-color`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-today-disabled-color`                     | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-outside-bg`                               | white     | slate-900 | slate-100   |
| `--vc-date-weekend-outside-color`                            | slate-400 | slate-600 | gray-400    |
| `--vc-date-weekend-outside-color-hover` <sup>dark only</sup> | —         | slate-300 | —           |
| `--vc-date-weekend-outside-bg-hover`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-outside-hover-bg`                         | slate-100 | slate-800 | slate-200   |
| `--vc-date-weekend-today-outside-color`                      | slate-400 | slate-400 | gray-400    |
| `--vc-date-weekend-disabled-outside-color`                   | slate-300 | slate-700 | gray-400    |
| `--vc-date-weekend-selected-bg`                              | rose-500  | rose-500  | red-500     |
| `--vc-date-weekend-selected-color`                           | white     | white     | white       |

### 选中的日期范围 (`multiple-ranged`)

| 变量                                   | light           | dark            | slate-light     |
| -------------------------------------- | --------------- | --------------- | --------------- |
| `--vc-date-range-middle-bg`            | cyan-500 at 70% | cyan-500 at 80% | blue-500 at 80% |
| `--vc-date-range-middle-color`         | white           | white           | white           |
| `--vc-date-range-middle-outside-bg`    | slate-200       | slate-800       | slate-200       |
| `--vc-date-range-middle-outside-color` | slate-500       | slate-300       | gray-600        |
| `--vc-date-range-middle-weekend-bg`    | rose-500 at 70% | rose-500 at 80% | red-500 at 80%  |
| `--vc-date-range-middle-weekend-color` | white           | white           | white           |

### 弹出窗口和提示框

| 变量                            | light     | dark      | slate-light |
| ------------------------------- | --------- | --------- | ----------- |
| `--vc-date-popup-bg`            | white     | slate-800 | white       |
| `--vc-date-popup-color`         | slate-900 | white     | gray-800    |
| `--vc-date-range-tooltip-bg`    | slate-50  | slate-800 | slate-50    |
| `--vc-date-range-tooltip-color` | slate-500 | slate-400 | slate-500   |

### 时间控件

| 变量                                                 | light      | dark      | slate-light |
| ---------------------------------------------------- | ---------- | --------- | ----------- |
| `--vc-time-border-color`                             | slate-300  | slate-800 | gray-300    |
| `--vc-time-separator-color`                          | slate-900  | white     | gray-800    |
| `--vc-time-input-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-input-color`                              | slate-900  | white     | gray-800    |
| `--vc-time-input-bg-hover`                           | orange-100 | slate-700 | blue-100    |
| `--vc-time-keeping-color`                            | slate-500  | slate-500 | gray-600    |
| `--vc-time-keeping-color-hover` <sup>dark only</sup> | —          | slate-400 | —           |
| `--vc-time-range-bg`                                 | white      | slate-900 | slate-100   |
| `--vc-time-range-track-color`                        | slate-300  | slate-600 | slate-300   |
| `--vc-time-range-thumb-bg`                           | white      | slate-800 | slate-100   |
| `--vc-time-range-thumb-border`                       | slate-300  | slate-600 | gray-300    |
| `--vc-time-range-thumb-border-hover`                 | slate-400  | slate-400 | gray-400    |

<Info>
  标记为 "dark only" 的三个变量存在的原因是，深色主题在这些元素上有一个 light/slate-light
  主题没有的额外悬停状态——在其他主题中，这些特定变量根本没有可覆盖的目标。
</Info>

```

### `docs/zh/reference/utilities.mdx`

```mdx
---
title: 实用工具
description: 发现 Vanilla Calendar Pro 提供的 4 个便捷日期实用工具。这些功能允许您格式化日期、将其转换为所需格式并确定周数。
section: 2
---

# 实用工具

日历附带其实用工具，使处理日期格式化变得容易。

总共有 4 个实用工具，它们是可以在代码中任何位置使用的函数，甚至无需日历。

1. **`parseDates(dates: string[])`** — 接受使用字符串格式 `FormatDateString ('YYYY-MM-DD')` 中日期之间的分隔符的日期范围数组。返回字符串格式 `FormatDateString ('YYYY-MM-DD')` 的日期数组。
```ts
import { parseDates } from 'vanilla-calendar-pro/utils';
parseDates(['2024-12-12:2024-12-15']); // 返回: ['2024-12-12', '2024-12-13', '2024-12-14', '2024-12-15']
```

2. **`getDateString(date: Date)`** — 接受 `Date` 类型的日期。返回字符串格式 `FormatDateString ('YYYY-MM-DD')` 的日期。
```ts
import { getDateString } from 'vanilla-calendar-pro/utils';
getDateString(new Date('24.12.2024')); // 返回: 2024-12-24
```

3. **`getDate(date: FormatDateString)`** — 接受字符串格式的日期，例如 `FormatDateString ('YYYY-MM-DD')`。返回 `Date` 类型的日期。
```ts
import { getDate } from 'vanilla-calendar-pro/utils';
getDate('2024-12-12'); // 返回: Tue Dec 24 2024 00:00:00 GMT
```

4. **`getWeekNumber(date: FormatDateString, weekStartDay: WeekDayID)`** — 接受字符串格式 `FormatDateString ('YYYY-MM-DD')` 的日期和周起始日，特别是其 `id` 类型为 `number` 从 0 到 6。返回参数中指定日期的对象 `{ year: yearNumber, week: weekNumber }`。
```ts
import { getWeekNumber } from 'vanilla-calendar-pro/utils';
getWeekNumber('2024-12-12', 1); // 返回: {year: 2024, week: 50}
```

```

### `eslint.config.mjs`

```mjs
import pluginJs from '@eslint/js';
import eslintConfigPrettier from 'eslint-config-prettier';
import prettierPlugin from 'eslint-plugin-prettier';
import pluginSimpleImportSort from 'eslint-plugin-simple-import-sort';
import globals from 'globals';
import tseslint from 'typescript-eslint';

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  {
    plugins: {
      '@typescript-eslint': tseslint.plugin,
      'simple-import-sort': pluginSimpleImportSort,
      prettier: prettierPlugin,
    },
  },
  {
    files: ['**/*.{js,mjs,cjs,ts}'],
  },
  {
    ignores: ['node_modules', 'next', 'demo/build', 'package/dist'],
  },
  {
    languageOptions: {
      globals: {
        ...globals.node,
        ...globals.browser,
        ...globals.es2021,
      },
      parserOptions: {
        project: ['tsconfig.json'],
      },
    },
  },
  {
    rules: {
      ...prettierPlugin.configs.recommended.rules,
      ...eslintConfigPrettier.rules,
      '@typescript-eslint/consistent-type-imports': ['error', { prefer: 'type-imports' }],
      '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      'no-extra-boolean-cast': 'off',
      'arrow-parens': ['error', 'always'],
      'simple-import-sort/imports': [
        'error',
        {
          groups: [['^antd'], ['^@?\\w'], ['~/(.*)', '@/(.*)'], ['^[./]']],
        },
      ],
    },
  },
];

```

### `examples/additional-features-animation-custom.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  animation: {
    slide: { duration: 700, easing: 'cubic-bezier(0.68, -0.55, 0.27, 1.55)' },
    fade: { duration: 450, easing: 'ease-in-out' },
    collapse: { duration: 550, easing: 'ease-in-out' },
  },
  enableCollapse: true,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-animation-shared.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  animation: { duration: 400 },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-animation.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  animation: true,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-collapse.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  animation: true,
  enableCollapse: true,
  selectedDates: ['2024-06-19'],
  enableJumpToSelectedDate: true,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-layouts-btn-close.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  inputMode: true,
  onChangeToInput(self) {
    if (!self.context.inputElement) return;
    if (self.context.selectedDates[0]) {
      self.context.inputElement.value = self.context.selectedDates[0];
    } else {
      self.context.inputElement.value = '';
    }
  },
  onInit(self) {
    const handleClickMainElement = (e: MouseEvent) => {
      if ((e.target as HTMLElement).closest('#btn-close')) {
        self.hide();
      }
    };
    self.context.mainElement.addEventListener('click', handleClickMainElement);
    return () => self.context.mainElement.removeEventListener('click', handleClickMainElement);
  },
  layouts: {
    default: `
      <div class="vc-header" data-vc="header" role="toolbar" aria-label="Calendar Navigation">
        <#ArrowPrev />
        <div class="vc-header__content" data-vc-header="content">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext />
      </div>
      <div class="vc-wrapper" data-vc="wrapper">
        <#WeekNumbers />
        <div class="vc-content" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
      <button id="btn-close" type="button">Close</button>
    `,
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-layouts.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  layouts: {
    default: `
      <div class="vc-header" data-vc="header" role="toolbar" aria-label="Calendar Navigation">
        <div class="vc-header__content" data-vc-header="content">
          <#Year /> | <#Month />
        </div>
        <#ArrowPrev />
        <#ArrowNext />
      </div>
      <div class="vc-wrapper" data-vc="wrapper">
        <#WeekNumbers />
        <div class="vc-content" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
      <button type="button">I am a button</button>
    `,
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-popups.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectedMonth: 6,
  selectedYear: 2024,
  popups: {
    '2024-07-03': {
      modifier: 'bg-sponsor',
      html: `
        <div>
          💖 Support the project: <a href="https://buymeacoffee.com/uvarov" rel="noopener noreferrer" target="_blank">Vanilla Calendar Pro</a>
        </div>
      `,
    },
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-styles.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  styles: {
    arrowPrev: 'arrow-smile',
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

// Add to your css and uncomment:
// button.arrow-smile::before {
//   background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewport='0 0 24 24' style='fill:black;font-size:24px;'><text y='90%' x='0'>😊</text></svg>");
//   transform: rotate(0);
//   transition: transform 0.2s;
// }

// button.arrow-smile:hover::before {
//   transform: rotate(180deg);
// }

```

### `examples/additional-features-swipe.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  animation: true,
  enableSwipe: true,
  selectedDates: ['2024-06-19'],
  enableJumpToSelectedDate: true,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-themes-dark.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectedTheme: 'dark',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-themes-light.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectedTheme: 'light',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-themes-slate-light.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/layout.css';
import 'vanilla-calendar-pro/styles/themes/slate-light.css';

const options: Options = {
  selectedTheme: 'slate-light',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/additional-features-tooltips.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionDatesMode: 'multiple-ranged',
  onCreateDateRangeTooltip(self) {
    const createRow = (title: string, value: string) =>
      `<div style="text-align: left; white-space: nowrap">
        <span>${title}</span>
        <b>${value}</b>
      </div>`;

    return `
      ${createRow('Start:', self.context.selectedDates[0])}
      ${self.context.selectedDates[1] ? createRow('End:', self.context.selectedDates[1]) : ''}
    `;
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-date-min-and-max.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  dateMin: '1920-01-01',
  dateMax: '2038-12-31',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-disable-dates.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  displayDateMin: '2022-07-01',
  displayDateMax: '2022-09-30',
  disableDates: ['2022-08-10:2022-08-13', '2022-08-22'],
  selectedYear: 2022,
  selectedMonth: 7,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-display-range-dates.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  dateMin: '1920-01-01',
  dateMax: '2038-12-31',
  displayDateMin: '2000-01-01',
  displayDateMax: '2024-12-31',
  displayDisabledDates: false,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-enable-dates.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  disableAllDates: true,
  enableDates: ['2022-08-10:2022-08-13', '2022-08-22'],
  selectedYear: 2022,
  selectedMonth: 7,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-enable-time-picker-12.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionTimeMode: 12,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-enable-time-picker-24.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionTimeMode: 24,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-enable-time-picker-control.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionTimeMode: 12,
  timeControls: 'range',
  timeStepHour: 5,
  timeStepMinute: 5,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-enable-time-picker-range.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionTimeMode: 12,
  timeMinHour: 6,
  timeMaxHour: 21,
  timeMinMinute: 10,
  timeMaxMinute: 40,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-enable-time-picker-your-time.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionTimeMode: 12,
  selectedTime: '03:44 AM',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-forbid-choice.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionDatesMode: false,
  selectionMonthsMode: false,
  selectionYearsMode: false,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-other-today.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  dateToday: new Date('2022-01-07'),
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/date-management-selected-days-month-year.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionDatesMode: 'multiple',
  selectedDates: ['2022-01-09:2022-01-13', '2022-01-22'],
  selectedMonth: 0,
  selectedYear: 2022,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-click-a-day-ranged.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionDatesMode: 'multiple-ranged',
  onClickDate(self) {
    console.log(self.context.selectedDates);
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-click-a-day.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  onClickDate(self) {
    console.log(self.context.selectedDates);
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-click-on-a-month-in-the-month-selection.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'month',
  onClickMonth(self) {
    console.log(self.context.selectedMonth);
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-click-on-the-arrows.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  onClickArrow(self) {
    console.log(self.context.selectedYear, self.context.selectedMonth);
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-click-on-the-week-number.ts`

```ts
import { Calendar, type FormatDateString, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  enableWeekNumbers: true,
  selectionDatesMode: 'multiple-ranged',
  onClickWeekNumber(self, number, year, dateEls) {
    const selectedDates = dateEls.map((dateEl) => dateEl.dataset.vcDate) as FormatDateString[];
    self.set({ selectedDates }, { dates: true });
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-click-on-the-year-in-the-year-selection.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'year',
  onClickYear(self) {
    console.log(self.context.selectedYear);
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-click-on-weekday.ts`

```ts
import { Calendar, type FormatDateString, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionDatesMode: 'multiple',
  onClickWeekDay(self, day, dateEls) {
    const selectedDates = dateEls.map((dateEl) => dateEl.dataset.vcDate) as FormatDateString[];
    self.set({ selectedDates }, { dates: true });
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-get-and-change-every-day.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  onCreateDateEls(self, dateEl) {
    const randomBoolean = Math.random() < 0.5;
    if (!randomBoolean) return;
    const randomPrice = Math.floor(Math.random() * (999 - 100 + 1) + 100);
    const btnEl = dateEl.querySelector('[data-vc-date-btn]') as HTMLButtonElement;
    const day = btnEl.innerText;
    btnEl.style.flexDirection = 'column';
    btnEl.innerHTML = `
      <span>${day}</span>
      <span style="font-size: 8px;color: #8BC34A;">$${randomPrice}</span>
    `;
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/handle-select-and-change-of-time.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectionTimeMode: 12,
  onChangeTime(self) {
    console.log(self.context.selectedTime);
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/installation-and-usage.ts`

```ts
import { Calendar } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const calendar = new Calendar('#calendar');
calendar.init();

```

### `examples/internationalization-assign-manually.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  locale: {
    months: {
      short: ['Vör', 'Thors', 'Skadi', 'Freya', 'Baldur', 'Njord', 'Tyr', 'Frigg', 'Odin', 'Loki', 'Hel', 'Idunn'],
      long: [
        'Vörmánuðr',
        'Thorsmánuðr',
        'Skadimánuðr',
        'Freymánuðr',
        'Baldurmánuðr',
        'Njordmánuðr',
        'Tyrmánuðr',
        'Friggmánuðr',
        'Odinmánuðr',
        'Lokimánuðr',
        'Helmánuðr',
        'Idunnmánuðr',
      ],
    },
    weekdays: {
      short: ['Sunna', 'Mani', 'Tiw', 'Woden', 'Thor', 'Frigg', 'Saturn'],
      long: ['Sunnandæg', 'Manadæg', 'Tiwesdæg', 'Wodensdæg', 'Thorsdæg', 'Friggsdæg', 'Saturnsdag'],
    },
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/internationalization-locale.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  locale: 'de-AT', // Austrian-German
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/internationalization-week-numbers.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  enableWeekNumbers: true,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/internationalization-weekday-first-and-weekdays.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  firstWeekday: 0,
  selectedWeekends: [0, 3, 6],
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/internationalization-weekends-and-holidays.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  selectedMonth: 0,
  selectedYear: 2022,
  selectedHolidays: ['2022-01-01:2022-01-05', '2022-01-10', '2022-01-13'],
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/type-default-in-input.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  inputMode: true,
  positionToInput: 'auto',
  onChangeToInput(self) {
    if (!self.context.inputElement) return;
    if (self.context.selectedDates[0]) {
      self.context.inputElement.value = self.context.selectedDates[0];
      // if you want to hide the calendar after picking a date
      self.hide();
    } else {
      self.context.inputElement.value = '';
    }
  },
};

const calendarInput = new Calendar('#calendar', options);
calendarInput.init();

```

### `examples/type-default.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'default',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/type-month.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'month',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/type-multiple-ranged.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'multiple',
  displayMonthsCount: 2,
  monthsToSwitch: 2,
  displayDatesOutside: false,
  disableDatesPast: true,
  enableEdgeDatesOnly: true,
  selectionDatesMode: 'multiple-ranged',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/type-multiple.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'multiple',
  displayMonthsCount: 2,
  monthsToSwitch: 1,
  selectionDatesMode: 'multiple',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/type-week-in-input.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'week',
  inputMode: true,
  positionToInput: 'auto',
  animation: true,
  enableCollapse: true,
  enableSwipe: true,
  selectedDates: ['2024-06-19'],
  enableJumpToSelectedDate: true,
  onChangeToInput(self) {
    if (!self.context.inputElement) return;
    self.context.inputElement.value = self.context.selectedDates[0] ? self.context.selectedDates[0] : '';
  },
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/type-week.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'week',
  animation: true,
  selectedDates: ['2024-06-19'],
  enableJumpToSelectedDate: true,
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `examples/type-year.ts`

```ts
import { Calendar, type Options } from 'vanilla-calendar-pro';

import 'vanilla-calendar-pro/styles/index.css';

const options: Options = {
  type: 'year',
};

const calendar = new Calendar('#calendar', options);
calendar.init();

```

### `helpers.js`

```js
/* eslint-disable @typescript-eslint/no-require-imports */
const fs = require('fs');
const path = require('path');
const { minify: minifyJs } = require('terser');
const postcss = require('postcss');
const cssnano = require('cssnano');
const pako = require('pako');
const archiver = require('archiver');
require('colors');

const inputDir = path.resolve(__dirname, 'package/dist');

const logMessage = (type, file, originalSize, minifiedSize, gzipSize) => {
  const sizeToKb = (size) => Math.round((size / 1024) * 100) / 100;
  const originalSizeKb = sizeToKb(originalSize);
  const minifiedSizeKb = sizeToKb(minifiedSize);
  const gzipSizeKb = sizeToKb(gzipSize);

  console.log(`Minified ${type}: `.gray + `${file}`.blue + ' | ' + `${originalSizeKb} kB → ${minifiedSizeKb} kB `.green + `(gzip: ${gzipSizeKb} kB)`.magenta);
};

const getGzipSize = (content) => Buffer.byteLength(pako.gzip(content));

const minifyFile = async (filePath, minifier) => {
  const fileContent = fs.readFileSync(filePath, 'utf8');
  const originalSize = Buffer.byteLength(fileContent);

  try {
    const result = await minifier(fileContent);
    fs.writeFileSync(filePath, result.code || result.css);

    const minifiedSize = Buffer.byteLength(result.code || result.css);
    const gzipSize = getGzipSize(result.code || result.css);
    logMessage(path.extname(filePath).slice(1).toUpperCase(), path.basename(filePath), originalSize, minifiedSize, gzipSize);
  } catch (e) {
    console.error(`Error minifying ${path.basename(filePath)}:`.red, e);
  }
};

const processDirectory = async (directory) => {
  const files = fs.readdirSync(directory);
  await Promise.all(
    files.map(async (file) => {
      const filePath = path.join(directory, file);
      if (fs.statSync(filePath).isDirectory()) {
        await processDirectory(filePath);
      } else if (file.endsWith('.js') || file.endsWith('.mjs')) {
        await minifyFile(filePath, minifyJs);
      } else if (file.endsWith('.css')) {
        await minifyFile(filePath, (content) => postcss([cssnano]).process(content, { from: filePath }));
      }
    }),
  );
};

const zipDirectory = async (sourceDir) => {
  const outputZipPath = path.join(sourceDir, 'package.zip');

  if (fs.existsSync(outputZipPath)) fs.unlinkSync(outputZipPath);

  const output = fs.createWriteStream(outputZipPath);
  const archive = archiver('zip', { zlib: { level: 9 } });

  return new Promise((resolve, reject) => {
    output.on('close', () => {
      console.log(`Archive created: ${outputZipPath.green}`.blue + ` (${(archive.pointer() / 1024).toFixed(2)} kB)`.green);
      resolve();
    });

    archive.on('error', (err) => {
      reject(err);
    });

    archive.pipe(output);

    function addFilesToArchive(dir) {
      fs.readdirSync(dir).forEach((file) => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
          addFilesToArchive(filePath);
        } else if (stat.isFile() && path.extname(file) !== '.zip') {
          archive.file(filePath, { name: path.relative(sourceDir, filePath) });
        }
      });
    }

    addFilesToArchive(sourceDir);
    archive.finalize();
  });
};

const main = async () => {
  try {
    await processDirectory(inputDir);
    console.log('Minification complete.'.green);
    await zipDirectory(inputDir);
    console.log('Archiving complete.'.green);
  } catch (err) {
    console.error('Error during processing:'.red, err);
  }
};

main();

```

### `LICENSE`

```
package/public/LICENSE
```

### `package.json`

```json
{
  "name": "vanilla-calendar-pro-project",
  "version": "0.0.0",
  "homepage": "https://vanilla-calendar.pro",
  "directories": {
    "config": "config/*",
    "cypress": "cypress/*",
    "demo": "demo/*",
    "docs": "docs/*",
    "examples": "examples/*",
    "package": "package/*"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/uvarov-frontend/vanilla-calendar-pro.git"
  },
  "author": {
    "name": "Yury Uvarov",
    "email": "uvarov.frontend@gmail.com",
    "url": "https://frontend.uvarov.tech"
  },
  "license": "MIT",
  "scripts": {
    "package:assets": "vite build --config config/assets.config.ts",
    "package:main": "vite build --config config/main.config.ts",
    "package:utils": "vite build --config config/utils.config.ts",
    "package:helpers": "node helpers.js",
    "package:build": "tsc && npm-run-all package:assets package:main package:utils package:helpers",
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "ESLINT_USE_FLAT_CONFIG=true npx eslint . --report-unused-disable-directives --max-warnings 0",
    "lint:fix": "ESLINT_USE_FLAT_CONFIG=true npx eslint . --fix",
    "prettier": "prettier . --check --ignore-unknown",
    "prettier:fix": "prettier . -w",
    "cypress:open": "env -u ELECTRON_RUN_AS_NODE cypress open",
    "cypress:run": "env -u ELECTRON_RUN_AS_NODE cypress run",
    "test:cypress": "start-server-and-test dev http://localhost:5173 cypress:run",
    "test:cypress:a11y": "start-server-and-test dev http://localhost:5173 \"npm run cypress:run -- --spec cypress/e2e/a11y.cy.ts\""
  },
  "devDependencies": {
    "@eslint/js": "^9.14.0",
    "@testing-library/cypress": "^10.0.2",
    "@types/node": "~18.18.14",
    "archiver": "^7.0.1",
    "autoprefixer": "^10.4.20",
    "axe-core": "^4.13.0",
    "colors": "^1.4.0",
    "cssnano": "^7.0.6",
    "cypress": "^13.15.2",
    "cypress-axe": "^1.7.0",
    "eslint": "^9.14.0",
    "eslint-config-prettier": "^9.1.0",
    "eslint-plugin-prettier": "^5.2.1",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "globals": "^15.12.0",
    "npm-run-all": "^4.1.5",
    "pako": "^2.1.0",
    "postcss": "^8.4.47",
    "prettier": "^3.3.3",
    "start-server-and-test": "^2.0.8",
    "tailwindcss": "^3.4.14",
    "terser": "^5.36.0",
    "typescript": "~4.9.3",
    "typescript-eslint": "^8.13.0",
    "vite": "~4.5.5",
    "vite-plugin-banner": "~0.7.1",
    "vite-plugin-dts": "^4.3.0",
    "vite-plugin-eslint": "~1.8.1"
  },
  "dependencies": {}
}

```

### `package/public/index.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>The Vanilla Calendar Pro is a versatile JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript frameworks and libraries.</title>
    <link href="./styles/index.css" rel="stylesheet" />
    <script src="./utils/index.js" defer></script>
    <script src="./index.js" defer></script>
  </head>
  <body style="display: flex; justify-items: flex-start">
    <div id="calendar"></div>
    <script>
      document.addEventListener('DOMContentLoaded', () => {
        // Destructuring the Calendar constructor and its utilities.
        const { Calendar } = window.VanillaCalendarPro;
        const { getDateString } = window.VanillaCalendarProUtils;

        // Instantiate the calendar and initialize it.
        const calendar = new Calendar('#calendar', { animation: true, enableSwipe: true, enableCollapse: true });
        calendar.init();

        // Create logs for demonstration.
        console.log('A copy of the calendar:', calendar);
        console.log('Date string conversion utility:', getDateString(new Date()));
      });
    </script>
  </body>
</html>

```

### `package/public/LICENSE`

```
MIT License

Copyright (c) 2024 Yury Uvarov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

### `package/public/package.json`

```json
{
  "name": "vanilla-calendar-pro",
  "description": "The Vanilla Calendar Pro is a versatile JavaScript date and time picker component with TypeScript support, making it compatible with any JavaScript frameworks and libraries. It is designed to be lightweight, easy to use, and feature-rich, without relying on external dependencies.",
  "version": "3.3.1",
  "private": false,
  "homepage": "https://vanilla-calendar.pro",
  "keywords": [
    "calendar",
    "datepicker",
    "timepicker",
    "date-picker",
    "vanilla-js",
    "javascript",
    "typescript",
    "react",
    "native",
    "pure",
    "picker",
    "vanilla",
    "default",
    "js",
    "ts"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/uvarov-frontend/vanilla-calendar-pro.git"
  },
  "author": {
    "name": "Yury Uvarov",
    "email": "uvarov.frontend@gmail.com",
    "url": "https://frontend.uvarov.tech"
  },
  "bugs": {
    "url": "https://github.com/uvarov-frontend/vanilla-calendar-pro/issues",
    "email": "uvarov.frontend@gmail.com"
  },
  "funding": {
    "type": "individual",
    "url": "https://buymeacoffee.com/uvarov"
  },
  "license": "MIT",
  "main": "./index.js",
  "module": "./index.mjs",
  "types": "./index.d.ts",
  "style": "./styles/index.css",
  "exports": {
    ".": {
      "types": "./index.d.ts",
      "require": "./index.js",
      "import": "./index.mjs",
      "default": "./index.mjs"
    },
    "./utils": {
      "types": "./utils/index.d.ts",
      "require": "./utils/index.js",
      "import": "./utils/index.mjs",
      "default": "./utils/index.mjs"
    },
    "./styles/*": "./styles/*",
    "./package.json": "./package.json"
  },
  "devDependencies": {},
  "dependencies": {}
}

```

### `package/public/README.md`

```md
# Vanilla Calendar Pro - Lightweight and Functional JavaScript Plugin for Date and Time Selection

[![vanilla-calendar preview](https://vanilla-calendar.pro/vanilla-calendar-preview-v3.png?v1)](https://vanilla-calendar.pro)

[![version](https://img.shields.io/npm/v/vanilla-calendar-pro.svg)](https://npmjs.com/package/vanilla-calendar-pro)
[![tests](https://github.com/uvarov-frontend/vanilla-calendar/actions/workflows/pull_request.yml/badge.svg)](https://github.com/uvarov-frontend/vanilla-calendar/actions/workflows/pull_request.yml)
[![downloads](https://img.shields.io/npm/dm/vanilla-calendar-pro.svg)](https://npmjs.com/package/vanilla-calendar-pro)

This is a versatile JavaScript date and time picker component with TypeScript support, compatible with any JavaScript frameworks and libraries. It is designed to be lightweight, easy to use, and feature-rich, without relying on external dependencies.

## Key Features

- **Lightweight**: The final JavaScript file is minified and optimized for fast loading.
- **No Dependencies**: Completely self-contained, ensuring you don't need to include additional libraries.
- **Simple Localization**: Supports simple localization for any language.
- **Customizable**: Can be easily configured using CSS and HTML markup, including CSS custom properties for theme colors.
- **Multiple Instances**: Allows for an unlimited number of calendar instances on a single page.
- **Theme Support**: Supports automatic theme switching between light and dark modes, as well as custom user-defined themes.
- **Week Start Customization**: Supports any day of the week as the starting day.
- **Custom Weekends**: Define custom weekend days for each week as needed.
- **Week Number Display**: Can display week numbers throughout the year.
- **Week View and Gestures**: A single-week calendar type, plus optional swipe navigation and collapsing a month down to one week.
- **Animated Transitions**: Optional sliding, cross-fading, and collapsing animations, with `prefers-reduced-motion` respected.
- **Not Tied to Input Tags**: Unlike many date pickers, it's not limited to the `<input>` tag.
- **Shadow DOM Support**: Can be initialized inside a Shadow DOM for encapsulated Web Components.
- **Accessible**: ARIA grid semantics, arrow-key navigation with a single tab stop per grid, managed focus, and localizable ARIA labels.
- **Date and Time Range Selection**: Supports selecting ranges for both dates and times, with maximum and minimum limits.
- **Popups and Tooltips**: Allows setting custom popups with user-defined information—including a single popup for a date range—and provides tooltips on hover in date range selection mode.

## Browser Support

VanillaCalendar is compatible with a wide range of browsers:

![Chrome](https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png) | ![Firefox](https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png) | ![Edge](https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png) | ![Opera](https://raw.githubusercontent.com/alrra/browser-logos/master/src/opera/opera_48x48.png) | ![Safari](https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png)
--- | --- | --- | --- | --- |
57+ ✔ | 52+ ✔ | 80+ ✔ | 44+ ✔ | 10.1+ ✔ |

## Support and Feedback

Vanilla Calendar Pro is free to use for everyone, but maintaining it comes with costs. I personally cover expenses like hosting, domain, and development resources to keep the project running smoothly. Your donations help me continue improving the tool while keeping it accessible for the community. Any contribution, big or small, makes a difference!

If you’d like to support the project, please consider making a donation or giving it a 🌟 star on [GitHub](https://github.com/uvarov-frontend/vanilla-calendar-pro).

[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://buymeacoffee.com/uvarov)

Feel free to report any issues or share your ideas—your feedback is invaluable!

## Getting Started

### Installation

You can install it using `npm` or `yarn`:

```sh
npm install vanilla-calendar-pro
# or
yarn add vanilla-calendar-pro
```

### Usage

Here's a simple example of using it in your HTML:

```html
<html>
  <head>
  </head>
  <body>
    <div id="calendar"></div>
    <!-- or -->
    <!-- <input type="text" id="calendar-input"> -->
  </body>
</html>
```

To add the necessary styles and scripts, you can use the following code:

```js
import { Calendar } from 'vanilla-calendar-pro';
import 'vanilla-calendar-pro/styles/index.css';

// Initialize the calendar
const calendar = new Calendar('#calendar');
calendar.init();
// or
// const calendarWithInput = new Calendar('#calendar-input', { inputMode: true });
// calendarWithInput.init();
```

## CSS Styles

```js
// Only layout calendar
import 'vanilla-calendar-pro/styles/layout.css';

// Themes
import 'vanilla-calendar-pro/styles/themes/light.css';
import 'vanilla-calendar-pro/styles/themes/dark.css';
// ...and others
```

The calendar can automatically switch between a light or dark theme depending on the user's system settings, or track a custom HTML attribute that specifies the desired theme.

- The `index.css` file contains all the styles from the `layout.css` file, as well as the light and dark theme styles.
- The `layout.css` file contains the essential structural styles for the calendar.
- The `themes/light.min.css` theme provides a light color scheme.
- The `themes/dark.min.css` theme offers a dark color scheme.
- ...and others

If you want to apply a specific theme, it is recommended to import `layout.css` along with your preferred theme instead of `index.css`.

## Layouts

The calendar contains custom `layouts` for each calendar type, which allow you to change the calendar structure to suit your needs.
Each layout contains its own set of components that can be moved or removed from it if necessary. By default, a layout contains all the components available to it.
Components are identified by tags containing the `#` character, and they must contain a slash at the end of the tag.

Here is an example of the default layout:

```js
new Calendar('#calendar', {
  layouts: {
    default: `
      <div class="vc-header" data-vc="header" role="group" aria-label="Calendar Navigation">
        <#ArrowPrev [month] />
        <div class="vc-header__content" data-vc-header="content" aria-live="polite" aria-atomic="true">
          <#Month />
          <#Year />
        </div>
        <#ArrowNext [month] />
      </div>
      <div class="vc-wrapper" data-vc="wrapper">
        <#WeekNumbers />
        <div class="vc-content" data-vc="content" role="grid">
          <#Week />
          <#Dates />
          <#DateRangeTooltip />
        </div>
      </div>
      <#Collapse />
      <#ControlTime />
    `
  }
});
```

## Library components

For detailed instructions on how to use the calendar as a component for various libraries, please visit the [website](https://vanilla-calendar.pro/docs/learn) with detailed documentation and examples.

## API Reference

For detailed information on the available parameters and settings, please refer to the [API reference](https://vanilla-calendar.pro/docs/reference).

## Sponsor

This project is tested with BrowserStack.

## License

MIT License

## Author

Yury Uvarov (*uvarov.frontend@gmail.com*)

```

### `package/src/index.ts`

```ts
import { destroy, hide, init, set, show, update } from '@scripts/methods';
import errorMessages from '@scripts/utils/getErrorMessages';
import replaceProperties from '@scripts/utils/replaceProperties';
import setContext from '@scripts/utils/setContext';
import OptionsCalendar from '@src/options';
import type {
  AnimationOptions,
  AnimationTiming,
  ContextVariables,
  DateAny,
  DateMode,
  DatesArr,
  FormatDateString,
  HtmlElementPosition,
  Labels,
  LabelsOptions,
  Layouts,
  Locale,
  LocaleStated,
  MonthsCount,
  Options,
  Popup,
  Popups,
  Positions,
  PositionToInput,
  Range,
  Reset,
  Styles,
  ThemesDefault,
  TimePicker,
  ToggleSelected,
  TypesCalendar,
  WeekDayID,
  WeekDays,
} from '@src/types';

export class Calendar extends OptionsCalendar {
  private static memoizedElements: Map<string, HTMLElement> = new Map();

  constructor(selector: HTMLElement | string, options?: Options) {
    super();

    this.context = {
      ...this.context,
      locale: {
        months: {
          short: [],
          long: [],
        },
        weekdays: {
          short: [],
          long: [],
        },
      },
    };

    setContext(this, 'mainElement', typeof selector === 'string' ? (Calendar.memoizedElements.get(selector) ?? this.queryAndMemoize(selector)) : selector);

    if (options) replaceProperties(this, options);
  }

  private queryAndMemoize(selector: string) {
    const element = document.querySelector<HTMLElement>(selector);
    if (!element) throw new Error(errorMessages.notFoundSelector(selector));

    Calendar.memoizedElements.set(selector, element);
    return element;
  }

  init = () => init(this);

  update = (resetOptions?: Partial<Reset>) => update(this, resetOptions);

  destroy = () => {
    const staleElement = this.inputMode ? this.context.inputElement : this.context.mainElement;
    destroy(this);
    if (staleElement) {
      for (const [selector, element] of Calendar.memoizedElements) {
        if (element === staleElement) Calendar.memoizedElements.delete(selector);
      }
    }
  };

  show = () => show(this);

  hide = () => hide(this);

  set = (options: Options, resetOptions?: Partial<Reset>) => set(this, options, resetOptions);

  readonly context!: Readonly<ContextVariables>;
}

export {
  AnimationOptions,
  AnimationTiming,
  DateAny,
  DateMode,
  DatesArr,
  FormatDateString,
  HtmlElementPosition,
  Labels,
  LabelsOptions,
  Layouts,
  Locale,
  LocaleStated,
  MonthsCount,
  Options,
  Popup,
  Popups,
  Positions,
  PositionToInput,
  ContextVariables,
  Range,
  Reset,
  Styles,
  ThemesDefault,
  TimePicker,
  ToggleSelected,
  TypesCalendar,
  WeekDayID,
  WeekDays,
};

```

### `package/src/labels.ts`

```ts
const labels = {
  application: 'Calendar',
  navigation: 'Calendar Navigation',
  arrowNext: {
    month: 'Next month',
    year: 'Next list of years',
    week: 'Next week',
  },
  arrowPrev: {
    month: 'Previous month',
    year: 'Previous list of years',
    week: 'Previous week',
  },
  month: 'Select month, current selected month:',
  months: 'List of months',
  year: 'Select year, current selected year:',
  years: 'List of years',
  week: 'Days of the week',
  weekNumber: 'Numbers of weeks in a year',
  collapse: 'Collapse to a single week',
  expand: 'Expand to the whole month',
  dates: 'Dates in the current month',
  selectingTime: 'Selecting a time ',
  inputHour: 'Hours',
  inputMinute: 'Minutes',
  rangeHour: 'Slider for selecting hours',
  rangeMinute: 'Slider for selecting minutes',
  btnKeeping: 'Switch AM/PM, current position:',
};

export default labels;

```

### `package/src/options.ts`

```ts
import type { Calendar } from '@src/index';
import labels from '@src/labels';
import styles from '@src/styles';
import type {
  AnimationOptions,
  DateAny,
  DateMode,
  DatesArr,
  Labels,
  Layouts,
  Locale,
  MonthsCount,
  Popups,
  PositionToInput,
  Range,
  Styles,
  ThemesDefault,
  TimeControl,
  ToggleSelected,
  TypesCalendar,
  WeekDayID,
  WeekDays,
} from '@src/types';

export default class OptionsCalendar {
  type: TypesCalendar = 'default';

  inputMode: boolean = false;
  openOnFocus: ToggleSelected = true;
  positionToInput: PositionToInput = 'left';

  animation: boolean | AnimationOptions = false;

  firstWeekday: WeekDayID = 1;
  monthsToSwitch: 1 | MonthsCount = 1;
  themeAttrDetect: string = 'html[data-theme]';

  locale: Locale = 'en';

  dateToday: DateAny = 'today';
  dateMin: DateAny = '1970-01-01';
  dateMax: DateAny = '2470-12-31';

  displayDateMin!: DateAny | null;
  displayDateMax!: DateAny | null;
  displayDatesOutside: boolean = true;
  displayDisabledDates: boolean = false;
  displayMonthsCount!: MonthsCount;

  disableDates: DatesArr = [];
  disableAllDates: boolean = false;
  disableDatesPast: boolean = false;
  disableDatesGaps: boolean = false;
  disableWeekdays: Range<7>[] = [];
  disableToday: boolean = false;

  enableDates: DatesArr = [];
  enableEdgeDatesOnly: boolean = true;
  enableDateToggle: ToggleSelected = true;
  enableWeekNumbers: boolean = false;
  enableMonthChangeOnDayClick: boolean = true;
  enableJumpToSelectedDate: boolean = false;
  enableCollapse: boolean = false;
  enableSwipe: boolean = false;

  selectionDatesMode: false | DateMode = 'single';
  selectionMonthsMode: boolean | 'only-arrows' = true;
  selectionYearsMode: boolean | 'only-arrows' = true;
  selectionTimeMode: false | 12 | 24 = false;

  selectedDates: DatesArr = [];
  selectedMonth!: Range<12>;
  selectedYear!: number;
  selectedHolidays: DatesArr = [];
  selectedWeekends: WeekDays<WeekDayID> = [0, 6];
  selectedTime!: string;
  selectedTheme: ThemesDefault | string = 'system';

  timeMinHour: Range<24> = 0;
  timeMaxHour: Range<24> = 23;
  timeMinMinute: Range<60> = 0;
  timeMaxMinute: Range<60> = 59;
  timeControls: TimeControl = 'all';
  timeStepHour: number = 1;
  timeStepMinute: number = 1;

  sanitizerHTML: (dirtyHtml: string) => string = (dirtyHtml: string) => dirtyHtml;

  onClickDate!: (self: Calendar, event: MouseEvent) => void;
  onClickWeekDay!: (self: Calendar, day: number, dateEls: HTMLElement[], event: MouseEvent) => void;
  onClickWeekNumber!: (self: Calendar, number: number, year: number, dateEls: HTMLElement[], event: MouseEvent) => void;
  onClickTitle!: (self: Calendar, event: MouseEvent) => void;
  onClickMonth!: (self: Calendar, event: MouseEvent) => void;
  onClickYear!: (self: Calendar, event: MouseEvent) => void;
  onClickArrow!: (self: Calendar, event: MouseEvent) => void;
  onChangeTime!: (self: Calendar, event: Event, isError: boolean) => void;
  onChangeToInput!: (self: Calendar, event: Event) => void;
  onCreateDateRangeTooltip!: (self: Calendar, dateEl: HTMLElement, tooltipEl: HTMLElement, dateElBCR: DOMRect, mainElBCR: DOMRect) => string;
  onCreateDateEls!: (self: Calendar, dateEl: HTMLElement) => void;
  onCreateMonthEls!: (self: Calendar, monthEl: HTMLElement) => void;
  onCreateYearEls!: (self: Calendar, yearEl: HTMLElement) => void;
  onInit!: (self: Calendar) => void;
  onUpdate!: (self: Calendar) => void;
  onDestroy!: (self: Calendar) => void;
  onShow!: (self: Calendar) => void;
  onHide!: (self: Calendar) => void;

  popups: Popups = {};
  labels: Labels = { ...labels };
  layouts: Layouts = { default: '', multiple: '', month: '', year: '', week: '' };
  styles: Styles = { ...styles };
}

```

### `package/src/scripts/components/ArrowNext.ts`

```ts
import { getArrowLabel, type NavigationType } from '@scripts/utils/updateNavigationA11y';
import type { Calendar } from '@src/index';

const ArrowNext = (self: Calendar, type: NavigationType) =>
  `<button type="button" class="${self.styles.arrowNext}" data-vc-arrow="next" aria-label="${getArrowLabel(self, 'next', type)}"></button>`;

export default ArrowNext;

```

### `package/src/scripts/components/ArrowPrev.ts`

```ts
import { getArrowLabel, type NavigationType } from '@scripts/utils/updateNavigationA11y';
import type { Calendar } from '@src/index';

const ArrowPrev = (self: Calendar, type: NavigationType) =>
  `<button type="button" class="${self.styles.arrowPrev}" data-vc-arrow="prev" aria-label="${getArrowLabel(self, 'prev', type)}"></button>`;

export default ArrowPrev;

```

### `package/src/scripts/components/Collapse.ts`

```ts
import { getCollapseA11y } from '@scripts/utils/updateNavigationA11y';
import type { Calendar } from '@src/index';

const Collapse = (self: Calendar) => {
  if (!self.enableCollapse) return '';
  const { expanded, label } = getCollapseA11y(self);
  return `<button type="button" class="${self.styles.collapse}" data-vc="collapse" aria-expanded="${expanded}" aria-label="${label}"></button>`;
};

export default Collapse;

```

### `package/src/scripts/components/ControlTime.ts`

```ts
import type { Calendar } from '@src/index';

const ControlTime = (self: Calendar) =>
  self.selectionTimeMode ? `<div class="${self.styles.time}" data-vc="time" role="group" aria-label="${self.labels.selectingTime}"></div>` : '';

export default ControlTime;

```

### `package/src/scripts/components/DateRangeTooltip.ts`

```ts
import type { Calendar } from '@src/index';

const DateRangeTooltip = (self: Calendar) =>
  !!self.onCreateDateRangeTooltip ? `<div class="${self.styles.dateRangeTooltip}" data-vc-date-range-tooltip="hidden"></div>` : '';

export default DateRangeTooltip;

```

### `package/src/scripts/components/Dates.ts`

```ts
import type { Calendar } from '@src/index';

const Dates = (self: Calendar) => `<div class="${self.styles.dates}" data-vc="dates" role="rowgroup" aria-label="${self.labels.dates}"></div>`;

export default Dates;

```

### `package/src/scripts/components/index.ts`

```ts
import ArrowNext from '@scripts/components/ArrowNext';
import ArrowPrev from '@scripts/components/ArrowPrev';
import Collapse from '@scripts/components/Collapse';
import ControlTime from '@scripts/components/ControlTime';
import DateRangeTooltip from '@scripts/components/DateRangeTooltip';
import Dates from '@scripts/components/Dates';
import Month from '@scripts/components/Month';
import Months from '@scripts/components/Months';
import Week from '@scripts/components/Week';
import WeekNumbers from '@scripts/components/WeekNumbers';
import Year from '@scripts/components/Year';
import Years from '@scripts/components/Years';

export const components = { ArrowNext, ArrowPrev, Collapse, ControlTime, Dates, DateRangeTooltip, Month, Months, Week, WeekNumbers, Year, Years };
export const getComponent = (pattern: string) => components[pattern as keyof typeof components];

```

### `package/src/scripts/components/Month.ts`

```ts
import type { Calendar } from '@src/index';

const Month = (self: Calendar) => `<button type="button" class="${self.styles.month}" data-vc="month"></button>`;

export default Month;

```

### `package/src/scripts/components/Months.ts`

```ts
import type { Calendar } from '@src/index';

const Months = (self: Calendar) => `<div class="${self.styles.months}" data-vc="months" role="grid" aria-label="${self.labels.months}"></div>`;

export default Months;

```

### `package/src/scripts/components/TimeInput.ts`

```ts
const TimeInput = (name: string, CSSClass: string, labels: { [key: string]: string }, value: string, range: boolean) => `
  <div class="${CSSClass}" data-vc-time-input="${name}">
    <input type="text" name="${name}" maxlength="2" aria-label="${labels[`input${name.charAt(0).toUpperCase() + name.slice(1)}`]}" value="${value}" ${range ? 'disabled' : ''}>
  </div>
`;

export default TimeInput;

```

### `package/src/scripts/components/TimeRange.ts`

```ts
const TimeRange = (name: string, CSSClass: string, labels: { [key: string]: string }, min: number, max: number, step: number, value: string) => `
  <div class="${CSSClass}" data-vc-time-range="${name}">
    <input type="range" min="${min}" max="${max}" step="${step}" aria-label="${labels[`range${name.charAt(0).toUpperCase() + name.slice(1)}`]}" value="${value}">
  </div>
`;

export default TimeRange;

```

### `package/src/scripts/components/Week.ts`

```ts
import type { Calendar } from '@src/index';

const Week = (self: Calendar) => `<div class="${self.styles.week}" data-vc="week" role="row" aria-label="${self.labels.week}"></div>`;

export default Week;

```

### `package/src/scripts/components/WeekNumbers.ts`

```ts
import type { Calendar } from '@src/index';

const WeekNumbers = (self: Calendar) =>
  self.enableWeekNumbers ? `<div class="${self.styles.weekNumbers}" data-vc-week="numbers" role="group" aria-label="${self.labels.weekNumber}"></div>` : '';

export default WeekNumbers;

```

### `package/src/scripts/components/Year.ts`

```ts
import type { Calendar } from '@src/index';

const Year = (self: Calendar) => `<button type="button" class="${self.styles.year}" data-vc="year"></button>`;

export default Year;

```

### `package/src/scripts/components/Years.ts`

```ts
import type { Calendar } from '@src/index';

const Years = (self: Calendar) => `<div class="${self.styles.years}" data-vc="years" role="grid" aria-label="${self.labels.years}"></div>`;

export default Years;

```

### `package/src/scripts/creators/create.ts`

```ts
import createDates from '@scripts/creators/createDates/createDates';
import createLayouts from '@scripts/creators/createLayouts';
import createMonths from '@scripts/creators/createMonths';
import createTime from '@scripts/creators/createTime';
import createWeek from '@scripts/creators/createWeek';
import createYears from '@scripts/creators/createYears';
import visibilityArrows from '@scripts/creators/visibilityArrows';
import visibilityTitle from '@scripts/creators/visibilityTitle';
import handleTheme from '@scripts/handles/handleTheme';
import getLocale from '@scripts/utils/getLocale';
import initWeek from '@scripts/utils/initVariables/initWeek';
import type { Calendar } from '@src/index';

const create = (self: Calendar) => {
  const createComponents = {
    default: () => {
      createWeek(self);
      createDates(self);
    },
    multiple: () => {
      createWeek(self);
      createDates(self);
    },
    week: () => {
      initWeek(self);
      createWeek(self);
      createDates(self);
    },
    month: () => createMonths(self),
    year: () => createYears(self),
  };

  handleTheme(self);
  getLocale(self);
  createLayouts(self);
  visibilityTitle(self);
  visibilityArrows(self);
  createTime(self);
  createComponents[self.context.currentType]();
};

export default create;

```

### `package/src/scripts/creators/createDates/createDate.ts`

```ts
import setDateModifier from '@scripts/creators/createDates/setDateModifier';
import getDate from '@scripts/utils/getDate';
import getLocaleString from '@scripts/utils/getLocaleString';
import getWeekNumber from '@scripts/utils/getWeekNumber';
import type { Calendar, FormatDateString, WeekDayID } from '@src/index';

const addWeekNumberForDate = (self: Calendar, dateEl: HTMLElement, dateStr: FormatDateString) => {
  const weekNumber = getWeekNumber(dateStr, self.firstWeekday);
  if (!weekNumber) return;
  dateEl.dataset.vcDateWeekNumber = String(weekNumber.week);
};

const setDaysAsDisabled = (self: Calendar, date: FormatDateString, dayWeekID: WeekDayID) => {
  const isDisableWeekday = self.disableWeekdays?.includes(dayWeekID);
  const isDisableAllDaysAndIsRangeEnabled = self.disableAllDates && !!self.context.enableDates?.[0];

  if ((isDisableWeekday || isDisableAllDaysAndIsRangeEnabled) && !self.context.enableDates?.includes(date) && !self.context.disableDates?.includes(date)) {
    self.context.disableDates.push(date);
    self.context.disableDates?.sort((a, b) => +new Date(a) - +new Date(b));
  }
};

const createDate = (
  self: Calendar,
  currentYear: number,
  datesContainer: { addDate: (dateEl: HTMLElement) => void },
  dateID: number,
  dateStr: FormatDateString,
  monthType: 'current' | 'prev' | 'next',
) => {
  const dayWeekID = getDate(dateStr).getDay() as WeekDayID;
  const localeDate = typeof self.locale === 'string' && self.locale.length ? self.locale : 'en';

  const dateEl = document.createElement('div');
  dateEl.className = self.styles.date;
  dateEl.dataset.vcDate = dateStr;
  dateEl.dataset.vcDateMonth = monthType;
  dateEl.dataset.vcDateWeekDay = String(dayWeekID);
  dateEl.role = 'gridcell';

  let dateBtnEl: HTMLButtonElement | undefined = undefined;
  if (monthType !== 'current' ? self.displayDatesOutside : true) {
    dateBtnEl = document.createElement('button');
    dateBtnEl.className = self.styles.dateBtn;
    dateBtnEl.type = 'button';
    dateBtnEl.ariaLabel = getLocaleString(dateStr, localeDate, { dateStyle: 'long', timeZone: 'UTC' });
    dateBtnEl.dataset.vcDateBtn = '';
    dateBtnEl.innerText = String(dateID);
    dateEl.appendChild(dateBtnEl);
  }

  if (self.enableWeekNumbers) addWeekNumberForDate(self, dateEl, dateStr);

  setDaysAsDisabled(self, dateStr, dayWeekID);
  setDateModifier(self, currentYear, dateEl, dateBtnEl, dayWeekID, dateStr, monthType);

  datesContainer.addDate(dateEl);
  if (self.onCreateDateEls) self.onCreateDateEls(self, dateEl);
};

export default createDate;

```

### `package/src/scripts/creators/createDates/createDatePopup.ts`

```ts
import parseDates from '@scripts/utils/parseDates';
import getAvailablePosition from '@scripts/utils/positions/getAvailablePosition';
import type { Calendar, Popup } from '@src/index';

const handleDay = (self: Calendar, date: string, dateInfo: Popup, datesEl: HTMLElement) => {
  const dateEl = datesEl.querySelector<HTMLElement>(`[data-vc-date="${date}"]`);
  const dateBtnEl = dateEl?.querySelector<HTMLButtonElement>(`[data-vc-date-btn]`);
  if (!dateEl || !dateBtnEl) return;

  if (dateInfo?.modifier) dateBtnEl.classList.add(...dateInfo.modifier.trim().split(' '));
  if (!dateInfo?.html) return;

  const datePopup = document.createElement('div');
  datePopup.className = self.styles.datePopup;
  datePopup.dataset.vcDatePopup = '';
  datePopup.innerHTML = self.sanitizerHTML(dateInfo.html);
  dateBtnEl.ariaLabel = `${dateBtnEl.ariaLabel}, ${datePopup?.textContent?.replace(/^\s+|\s+(?=\s)|\s+$/g, '').replace(/&nbsp;/g, ' ')}`;
  dateEl.appendChild(datePopup);

  // Use requestAnimationFrame to wait until the next repaint to calculate position
  requestAnimationFrame(() => {
    if (!datePopup) return;
    const { canShow } = getAvailablePosition(dateEl, datePopup);
    const top = canShow.bottom ? dateEl.offsetHeight : -datePopup.offsetHeight;
    const left =
      canShow.left && !canShow.right ? dateEl.offsetWidth - datePopup.offsetWidth / 2 : !canShow.left && canShow.right ? datePopup.offsetWidth / 2 : 0;
    Object.assign(datePopup.style, { left: `${left}px`, top: `${top}px` });
  });
};

const createDatePopup = (self: Calendar, datesEl: HTMLElement) => {
  if (!self.popups) return;
  Object.entries(self.popups)?.forEach(([dateKey, dateInfo]) => {
    parseDates([dateKey]).forEach((date) => handleDay(self, date, dateInfo, datesEl));
  });
};

export default createDatePopup;

```

### `package/src/scripts/creators/createDates/createDateRangeTooltip.ts`

```ts
import type { Calendar } from '@src/index';

const createDateRangeTooltip = (self: Calendar, tooltipEl: HTMLElement | null, dateEl: HTMLElement | null) => {
  if (!tooltipEl) return;

  if (!dateEl) {
    tooltipEl.dataset.vcDateRangeTooltip = 'hidden';
    tooltipEl.textContent = '';
    return;
  }

  const mainBCR = self.context.mainElement.getBoundingClientRect();
  const dateElBCR = dateEl.getBoundingClientRect();

  tooltipEl.style.left = `${dateElBCR.left - mainBCR.left + dateElBCR.width / 2}px`;
  tooltipEl.style.top = `${dateElBCR.bottom - mainBCR.top - dateElBCR.height}px`;
  tooltipEl.dataset.vcDateRangeTooltip = 'visible';
  tooltipEl.innerHTML = self.sanitizerHTML(self.onCreateDateRangeTooltip(self, dateEl, tooltipEl, dateElBCR, mainBCR));
};

export default createDateRangeTooltip;

```

### `package/src/scripts/creators/createDates/createDates.ts`

```ts
import createDatePopup from '@scripts/creators/createDates/createDatePopup';
import createDatesFromCurrentMonth from '@scripts/creators/createDates/createDatesFromCurrentMonth';
import createDatesFromNextMonth from '@scripts/creators/createDates/createDatesFromNextMonth';
import createDatesFromPrevMonth from '@scripts/creators/createDates/createDatesFromPrevMonth';
import createWeekDates from '@scripts/creators/createDates/createWeekDates';
import createWeekNumbers from '@scripts/creators/createWeekNumbers';
import updateRovingTabIndex from '@scripts/utils/rovingTabIndex';
import type { Calendar } from '@src/index';

const createDates = (self: Calendar) => {
  const initDate = new Date(self.context.selectedYear as number, self.context.selectedMonth as number, 1);
  const datesEls = self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc="dates"]');
  const weekNumbersEls = self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc-week="numbers"]');

  datesEls.forEach((datesEl, index: number) => {
    if (!self.selectionDatesMode) datesEl.dataset.vcDatesDisabled = '';
    datesEl.textContent = '';

    if (self.context.currentType === 'week') {
      createWeekDates(self, datesEl);
      createDatePopup(self, datesEl);
      createWeekNumbers(self, 0, 7, weekNumbersEls[index], datesEl);
      return;
    }

    const currentDate = new Date(initDate);
    currentDate.setMonth(currentDate.getMonth() + index);
    const currentMonth = currentDate.getMonth();
    const currentYear = currentDate.getFullYear();
    const firstDayWeek = (new Date(currentYear, currentMonth, 1).getDay() - self.firstWeekday + 7) % 7;
    const days = new Date(currentYear, currentMonth + 1, 0).getDate();

    const totalDays = firstDayWeek + days;
    const totalWeeks = Math.ceil(totalDays / 7);
    const daysNextMonth = totalWeeks * 7 - totalDays;

    const weekRows: HTMLElement[] = [];

    for (let i = 0; i < totalWeeks; i++) {
      const weekRow = document.createElement('div');
      weekRow.className = self.styles.datesRow;
      weekRow.setAttribute('data-vc-dates', 'row');
      weekRow.setAttribute('role', 'row');
      weekRows.push(weekRow);
    }

    let currentRowIndex = 0;
    let daysInCurrentRow = 0;

    const dateContainer = {
      addDate: (dateEl: HTMLElement) => {
        weekRows[currentRowIndex].appendChild(dateEl);
        daysInCurrentRow++;
        if (daysInCurrentRow >= 7) {
          currentRowIndex++;
          daysInCurrentRow = 0;
        }
      },
    };

    createDatesFromPrevMonth(self, dateContainer, currentYear, currentMonth, firstDayWeek);
    createDatesFromCurrentMonth(self, dateContainer, days, currentYear, currentMonth);
    createDatesFromNextMonth(self, dateContainer, daysNextMonth, currentYear, currentMonth);
    for (const weekRow of weekRows) {
      datesEl.appendChild(weekRow);
    }
    createDatePopup(self, datesEl);
    createWeekNumbers(self, firstDayWeek, days, weekNumbersEls[index], datesEl);
  });

  updateRovingTabIndex(self);
};

export default createDates;

```

### `package/src/scripts/creators/createDates/createDatesFromCurrentMonth.ts`

```ts
import createDate from '@scripts/creators/createDates/createDate';
import getDateString from '@scripts/utils/getDateString';
import type { Calendar } from '@src/index';

const createDatesFromCurrentMonth = (
  self: Calendar,
  datesContainer: { addDate: (dateEl: HTMLElement) => void },
  days: number,
  currentYear: number,
  currentMonth: number,
) => {
  for (let dateID = 1; dateID <= days; dateID++) {
    const date = new Date(currentYear, currentMonth, dateID);
    createDate(self, currentYear, datesContainer, dateID, getDateString(date), 'current');
  }
};

export default createDatesFromCurrentMonth;

```

### `package/src/scripts/creators/createDates/createDatesFromNextMonth.ts`

```ts
import createDate from '@scripts/creators/createDates/createDate';
import type { Calendar, FormatDateString } from '@src/index';

const createDatesFromNextMonth = (
  self: Calendar,
  datesContainer: { addDate: (dateEl: HTMLElement) => void },
  daysNextMonth: number,
  currentYear: number,
  currentMonth: number,
) => {
  const year = currentMonth + 1 === 12 ? currentYear + 1 : currentYear;
  const month = currentMonth + 1 === 12 ? '01' : currentMonth + 2 < 10 ? `0${currentMonth + 2}` : currentMonth + 2;

  for (let i = 1; i <= daysNextMonth; i++) {
    const day = i < 10 ? `0${i}` : String(i);
    const dateStr = `${year}-${month}-${day}` as FormatDateString;
    createDate(self, currentYear, datesContainer, i, dateStr, 'next');
  }
};

export default createDatesFromNextMonth;

```

### `package/src/scripts/creators/createDates/createDatesFromPrevMonth.ts`

```ts
import createDate from '@scripts/creators/createDates/createDate';
import type { Calendar, FormatDateString } from '@src/index';

const createDatesFromPrevMonth = (
  self: Calendar,
  datesContainer: { addDate: (dateEl: HTMLElement) => void },
  currentYear: number,
  currentMonth: number,
  firstDayWeek: number,
) => {
  let date = new Date(currentYear, currentMonth, 0).getDate() - (firstDayWeek - 1);
  const year = currentMonth === 0 ? currentYear - 1 : currentYear;
  const month = currentMonth === 0 ? 12 : currentMonth < 10 ? `0${currentMonth}` : currentMonth;

  for (let i = firstDayWeek; i > 0; i--, date++) {
    const dateStr = `${year}-${month}-${date}` as FormatDateString;
    createDate(self, currentYear, datesContainer, date, dateStr, 'prev');
  }
};

export default createDatesFromPrevMonth;

```

### `package/src/scripts/creators/createDates/createWeekDates.ts`

```ts
import createDate from '@scripts/creators/createDates/createDate';
import getDate from '@scripts/utils/getDate';
import getDateString from '@scripts/utils/getDateString';
import type { Calendar } from '@src/index';

const createWeekDates = (self: Calendar, datesEl: HTMLElement) => {
  const weekStart = getDate(self.context.displayWeekDate);
  const weekRow = document.createElement('div');
  weekRow.className = self.styles.datesRow;
  weekRow.dataset.vcDates = 'row';
  weekRow.role = 'row';

  const dateContainer = { addDate: (dateEl: HTMLElement) => weekRow.appendChild(dateEl) };

  for (let i = 0; i < 7; i++) {
    const date = new Date(weekStart);
    date.setDate(weekStart.getDate() + i);
    createDate(self, date.getFullYear(), dateContainer, date.getDate(), getDateString(date), 'current');
  }

  datesEl.appendChild(weekRow);
};

export default createWeekDates;

```

### `package/src/scripts/creators/createDates/setDateModifier.ts`

```ts
import getDate from '@scripts/utils/getDate';
import parseDates from '@scripts/utils/parseDates';
import type { Calendar, FormatDateString, WeekDayID } from '@src/index';

const updateAttribute = (el: HTMLElement | HTMLButtonElement, condition: boolean | undefined, attr: string, value = '') => {
  if (condition) {
    el.setAttribute(attr, value);
  } else if (el.getAttribute(attr) === value) {
    el.removeAttribute(attr);
  }
};

const getDateTime = (date: FormatDateString) => Date.parse(`${date}T00:00:00`);

const setDateModifier = (
  self: Calendar,
  currentYear: number,
  dateEl: HTMLElement,
  dateBtnEl: HTMLButtonElement | undefined,
  dayWeekID: WeekDayID,
  dateStr: FormatDateString,
  monthType: 'current' | 'prev' | 'next',
) => {
  const dateTime = getDateTime(dateStr);
  const isDisabled =
    getDateTime(self.context.displayDateMin) > dateTime ||
    getDateTime(self.context.displayDateMax) < dateTime ||
    self.context.disableDates?.includes(dateStr) ||
    (!self.selectionMonthsMode && monthType !== 'current') ||
    (!self.selectionYearsMode && getDate(dateStr).getFullYear() !== currentYear);

  // Check if the date is disabled
  updateAttribute(dateEl, isDisabled, 'data-vc-date-disabled');
  if (dateBtnEl) updateAttribute(dateBtnEl, isDisabled, 'aria-disabled', 'true');
  if (dateBtnEl) updateAttribute(dateBtnEl, isDisabled, 'tabindex', '-1');
  if (dateBtnEl) dateBtnEl.disabled = !!isDisabled;

  // Check if the date is today
  updateAttribute(dateEl, !self.disableToday && self.context.dateToday === dateStr, 'data-vc-date-today');
  updateAttribute(dateEl, !self.disableToday && self.context.dateToday === dateStr, 'aria-current', 'date');

  // Check if the date is a weekend
  updateAttribute(dateEl, self.selectedWeekends?.includes(dayWeekID), 'data-vc-date-weekend');

  // Check if the date is a holiday
  const selectedHolidays = self.selectedHolidays?.[0] ? parseDates(self.selectedHolidays) : [];
  updateAttribute(dateEl, selectedHolidays.includes(dateStr), 'data-vc-date-holiday');

  // Check if the date is selected: aria-selected belongs on the gridcell, a button does not support it
  if (self.context.selectedDates?.includes(dateStr)) {
    dateEl.setAttribute('data-vc-date-selected', '');
    dateEl.setAttribute('aria-selected', 'true');
    if (self.context.selectedDates.length > 1 && self.selectionDatesMode === 'multiple-ranged') {
      if (self.context.selectedDates[0] === dateStr && self.context.selectedDates[self.context.selectedDates.length - 1] === dateStr) {
        dateEl.setAttribute('data-vc-date-selected', 'first-and-last');
      } else if (self.context.selectedDates[0] === dateStr) {
        dateEl.setAttribute('data-vc-date-selected', 'first');
      } else if (self.context.selectedDates[self.context.selectedDates.length - 1] === dateStr) {
        dateEl.setAttribute('data-vc-date-selected', 'last');
      }

      if (self.context.selectedDates[0] !== dateStr && self.context.selectedDates[self.context.selectedDates.length - 1] !== dateStr)
        dateEl.setAttribute('data-vc-date-selected', 'middle');
    }
  } else if (dateEl.hasAttribute('data-vc-date-selected')) {
    dateEl.removeAttribute('data-vc-date-selected');
    dateEl.removeAttribute('aria-selected');
  }

  // When using multiple-ranged with range edges only (only includes start/end selected dates)
  if (
    !self.context.disableDates.includes(dateStr) &&
    self.enableEdgeDatesOnly &&
    self.context.selectedDates.length > 1 &&
    self.selectionDatesMode === 'multiple-ranged'
  ) {
    const firstDate = getDate(self.context.selectedDates[0]);
    const lastDate = getDate(self.context.selectedDates[self.context.selectedDates.length - 1]);
    const currentDate = getDate(dateStr);
    updateAttribute(dateEl, currentDate > firstDate && currentDate < lastDate, 'data-vc-date-selected', 'middle');
  }
};

export default setDateModifier;

```

### `package/src/scripts/creators/createDates/updateDateModifiers.ts`

```ts
import setDateModifier from '@scripts/creators/createDates/setDateModifier';
import getDate from '@scripts/utils/getDate';
import updateRovingTabIndex from '@scripts/utils/rovingTabIndex';
import type { Calendar, FormatDateString, WeekDayID } from '@src/index';

const updateDateModifiers = (self: Calendar) => {
  const dateEls = self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc-date]');
  dateEls.forEach((dateEl) => {
    const dateBtnEl = dateEl.querySelector<HTMLButtonElement>('[data-vc-date-btn]') as HTMLButtonElement;
    const dateStr = dateEl.dataset.vcDate as FormatDateString;
    const dayWeekID = getDate(dateStr).getDay() as WeekDayID;
    setDateModifier(self, self.context.selectedYear, dateEl, dateBtnEl, dayWeekID, dateStr, 'current');
  });

  updateRovingTabIndex(self);
};

export default updateDateModifiers;

```

### `package/src/scripts/creators/createLayouts.ts`

```ts
import layoutDefault from '@scripts/layouts/default';
import layoutMonths from '@scripts/layouts/month';
import layoutMultiple from '@scripts/layouts/multiple';
import layoutWeek from '@scripts/layouts/week';
import layoutYears from '@scripts/layouts/year';
import { parseLayout, parseMultipleLayout } from '@scripts/utils/parseComponent';
import type { Calendar } from '@src/index';

const syncMultiselectable = (self: Calendar) => {
  const isMultiselectable = ['multiple', 'multiple-ranged'].includes(String(self.selectionDatesMode));
  self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc="content"][role="grid"]').forEach((gridEl) => {
    if (isMultiselectable) gridEl.setAttribute('aria-multiselectable', 'true');
    else gridEl.removeAttribute('aria-multiselectable');
  });
};

const createLayouts = (self: Calendar, target?: HTMLElement) => {
  const templateMap = {
    default: layoutDefault,
    month: layoutMonths,
    year: layoutYears,
    multiple: layoutMultiple,
    week: layoutWeek,
  };

  Object.keys(templateMap).forEach((key) => {
    const typedKey = key as keyof typeof templateMap;
    if (!self.layouts[typedKey].length) self.layouts[typedKey] = templateMap[typedKey](self);
  });

  self.context.mainElement.className = self.styles.calendar;
  self.context.mainElement.dataset.vc = 'calendar';
  self.context.mainElement.dataset.vcType = self.context.currentType;
  self.context.mainElement.toggleAttribute('data-vc-swipe', self.enableSwipe);
  // Native buttons and a grid need no `application` role, which would only cost screen reader
  // users their reading commands. In input mode the popup is a dialog the input opens.
  self.context.mainElement.role = self.inputMode ? 'dialog' : 'group';
  self.context.mainElement.tabIndex = -1;
  self.context.mainElement.ariaLabel = self.labels.application;

  if (self.context.currentType === 'multiple') {
    self.context.mainElement.innerHTML = self.sanitizerHTML(parseMultipleLayout(self, parseLayout(self, self.layouts[self.context.currentType])));
    syncMultiselectable(self);
    return;
  }

  if (self.type === 'multiple' && target) {
    const controlsEl = self.context.mainElement.querySelector<HTMLElement>('[data-vc="controls"]');
    const gridEl = self.context.mainElement.querySelector<HTMLElement>('[data-vc="grid"]');
    const columnEl = target.closest<HTMLElement>('[data-vc="column"]');

    if (controlsEl) controlsEl.remove();
    if (gridEl) gridEl.dataset.vcGrid = 'hidden';
    if (columnEl) columnEl.dataset.vcColumn = self.context.currentType;
    if (columnEl) columnEl.innerHTML = self.sanitizerHTML(parseLayout(self, self.layouts[self.context.currentType]));
    syncMultiselectable(self);
    return;
  }

  self.context.mainElement.innerHTML = self.sanitizerHTML(parseLayout(self, self.layouts[self.context.currentType]));
  syncMultiselectable(self);
};

export default createLayouts;

```

### `package/src/scripts/creators/createMonths.ts`

```ts
import createLayouts from '@scripts/creators/createLayouts';
import setMonthOrYearModifier from '@scripts/creators/setMonthOrYearModifier';
import visibilityTitle from '@scripts/creators/visibilityTitle';
import getColumnID from '@scripts/utils/getColumnID';
import getDate from '@scripts/utils/getDate';
import updateRovingTabIndex from '@scripts/utils/rovingTabIndex';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const createMonthEl = (
  self: Calendar,
  templateEl: HTMLButtonElement,
  selected: number,
  titleShort: string,
  titleLong: string,
  disabled: boolean,
  id: number,
) => {
  const monthWrapperEl = document.createElement('div');
  monthWrapperEl.className = self.styles.monthsCell;
  monthWrapperEl.dataset.vcMonths = 'cell';
  monthWrapperEl.role = 'gridcell';

  const monthEl = templateEl.cloneNode(false) as HTMLButtonElement;
  monthEl.className = self.styles.monthsMonth;
  monthEl.innerText = titleShort;
  monthEl.ariaLabel = titleLong;
  monthEl.dataset.vcMonthsMonth = `${id}`;
  if (disabled) monthEl.ariaDisabled = 'true';
  if (disabled) monthEl.tabIndex = -1;
  monthEl.disabled = disabled;

  monthWrapperEl.appendChild(monthEl);

  setMonthOrYearModifier(self, monthEl, 'month', selected === id, false);
  return monthWrapperEl;
};

const createMonths = (self: Calendar, target?: HTMLElement) => {
  const yearEl = target?.closest('[data-vc="header"]')?.querySelector<HTMLElement>('[data-vc="year"]');
  const selectedYear = yearEl ? Number(yearEl.dataset.vcYear) : (self.context.selectedYear as number);
  const selectedMonth = target?.dataset.vcMonth ? Number(target.dataset.vcMonth) : self.context.selectedMonth;

  setContext(self, 'currentType', 'month');
  createLayouts(self, target);
  visibilityTitle(self);

  const monthsEl = self.context.mainElement.querySelector('[data-vc="months"]');
  if (!self.selectionMonthsMode || !monthsEl) return;

  const activeMonthsID =
    self.monthsToSwitch > 1
      ? self.context.locale.months.long
          .map((_, i) => selectedMonth - self.monthsToSwitch * i)
          .concat(self.context.locale.months.long.map((_, i) => selectedMonth + self.monthsToSwitch * i))
          .filter((monthID) => monthID >= 0 && monthID <= 12)
      : Array.from(Array(12).keys());

  const templateMonthEl = document.createElement('button');
  templateMonthEl.type = 'button';

  let rowEl: HTMLDivElement | undefined;

  for (let i = 0; i < 12; i++) {
    if (i % 4 === 0) {
      rowEl = document.createElement('div');
      rowEl.className = self.styles.monthsRow;
      rowEl.dataset.vcMonths = 'row';
      rowEl.role = 'row';
      monthsEl.appendChild(rowEl);
    }

    const dateMin = getDate(self.context.dateMin);
    const dateMax = getDate(self.context.dateMax);
    const monthCount = self.context.displayMonthsCount - 1;
    const { columnID } = getColumnID(self, 'month');

    const monthDisabled =
      (selectedYear <= dateMin.getFullYear() && i < dateMin.getMonth() + columnID) ||
      (selectedYear >= dateMax.getFullYear() && i > dateMax.getMonth() - monthCount + columnID) ||
      selectedYear > dateMax.getFullYear() ||
      (i !== selectedMonth && !activeMonthsID.includes(i));
    const monthEl = createMonthEl(
      self,
      templateMonthEl,
      selectedMonth,
      self.context.locale.months.short[i],
      self.context.locale.months.long[i],
      monthDisabled,
      i,
    );
    rowEl?.appendChild(monthEl);
    if (self.onCreateMonthEls) self.onCreateMonthEls(self, monthEl);
  }

  updateRovingTabIndex(self);
};

export default createMonths;

```

### `package/src/scripts/creators/createTime.ts`

```ts
import TimeInput from '@scripts/components/TimeInput';
import TimeRange from '@scripts/components/TimeRange';
import handleTime from '@scripts/handles/handleTime/handleTime';
import transformTime24 from '@scripts/utils/transformTime24';
import type { Calendar, ContextVariables } from '@src/index';

const createTime = (self: Calendar) => {
  const timeEl = self.context.mainElement.querySelector<HTMLElement>('[data-vc="time"]');
  if (!self.selectionTimeMode || !timeEl) return;

  const [minHour, maxHour] = [self.timeMinHour, self.timeMaxHour];
  const [minMinutes, maxMinutes] = [self.timeMinMinute, self.timeMaxMinute];

  const valueHours = self.context.selectedKeeping ? transformTime24(self.context.selectedHours, self.context.selectedKeeping) : self.context.selectedHours;
  const range = self.timeControls === 'range';

  const btnKeeping = (selectedKeeping: ContextVariables['selectedKeeping']) =>
    `<button type="button" class="${self.styles.timeKeeping}" aria-label="${self.labels.btnKeeping} ${selectedKeeping}" data-vc-time="keeping" ${range ? 'disabled' : ''}>${selectedKeeping}</button>`;

  timeEl.innerHTML = self.sanitizerHTML(`
    <div class="${self.styles.timeContent}" data-vc-time="content">
      ${TimeInput('hour', self.styles.timeHour, self.labels as unknown as { [key: string]: string }, self.context.selectedHours, range)}
      ${TimeInput('minute', self.styles.timeMinute, self.labels as unknown as { [key: string]: string }, self.context.selectedMinutes, range)}
      ${self.selectionTimeMode === 12 ? btnKeeping(self.context.selectedKeeping) : ''}
    </div>
    <div class="${self.styles.timeRanges}" data-vc-time="ranges">
      ${TimeRange('hour', self.styles.timeRange, self.labels as unknown as { [key: string]: string }, minHour, maxHour, self.timeStepHour, valueHours)}
      ${TimeRange('minute', self.styles.timeRange, self.labels as unknown as { [key: string]: string }, minMinutes, maxMinutes, self.timeStepMinute, self.context.selectedMinutes)}
    </div>
  `);

  handleTime(self, timeEl);
};

export default createTime;

```

### `package/src/scripts/creators/createToInput.ts`

```ts
import handleArrowKeys from '@scripts/handles/handleArrowKeys';
import handleClick from '@scripts/handles/handleClick/handleClick';
import handleGestures from '@scripts/handles/handleGestures/handleGestures';
import { show } from '@scripts/methods';
import reset from '@scripts/methods/reset';
import getRootNode from '@scripts/utils/getRootNode';
import setContext from '@scripts/utils/setContext';
import { hideFromAT } from '@scripts/utils/toggleTabbing';
import type { Calendar } from '@src/index';

const createToInput = (self: Calendar) => {
  const calendar = document.createElement('div');
  calendar.className = self.styles.calendar;
  calendar.dataset.vc = 'calendar';
  calendar.dataset.vcInput = '';
  calendar.dataset.vcCalendarHidden = '';
  hideFromAT(calendar);

  // append into the input's own root (a ShadowRoot if the calendar lives inside one, so the
  // popup stays inside the same encapsulated style scope; document.body otherwise, since a
  // Document itself can't directly accept an arbitrary element as a child)
  const inputRoot = getRootNode(self.context.mainElement);
  const appendTarget = inputRoot === document ? document.body : inputRoot;

  setContext(self, 'inputModeInit', true);
  setContext(self, 'isShowInInputMode', false);
  setContext(self, 'mainElement', calendar);
  appendTarget.appendChild(self.context.mainElement);

  reset(self, {
    year: true,
    month: true,
    dates: true,
    time: true,
    locale: true,
  });

  setTimeout(() => show(self));

  if (self.onInit) self.onInit(self);
  handleArrowKeys(self);
  handleGestures(self);
  return handleClick(self);
};

export default createToInput;

```

### `package/src/scripts/creators/createWeek.ts`

```ts
import type { Calendar, WeekDayID } from '@src/index';

const createWeek = (self: Calendar) => {
  const weekend = self.selectedWeekends ? [...self.selectedWeekends] : [];
  const weekdaysData = [...self.context.locale.weekdays.long].reduce(
    (acc, day, index) => [
      ...acc,
      {
        id: index as WeekDayID,
        titleShort: self.context.locale.weekdays.short[index],
        titleLong: day,
        isWeekend: weekend.includes(index as WeekDayID),
      },
    ],
    [] as Array<{
      id: WeekDayID;
      titleShort: string;
      titleLong: string;
      isWeekend: boolean;
    }>,
  );
  const weekdays = [...weekdaysData.slice(self.firstWeekday), ...weekdaysData.slice(0, self.firstWeekday)];

  // A columnheader is not a role a button may carry, so the clickable variant keeps the header
  // cell as its own element and nests the button inside it.
  const isClickable = !!self.onClickWeekDay;
  const templateWeekDayEl = document.createElement(isClickable ? 'div' : 'b');
  const templateWeekDayBtnEl = document.createElement('button');
  templateWeekDayBtnEl.type = 'button';
  templateWeekDayBtnEl.className = self.styles.weekDayBtn;
  templateWeekDayBtnEl.dataset.vcWeekDayBtn = '';

  self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc="week"]').forEach((weekEl) => {
    weekdays.forEach((weekday) => {
      const weekDayEl = templateWeekDayEl.cloneNode(false) as HTMLElement;
      weekDayEl.className = self.styles.weekDay;
      weekDayEl.role = 'columnheader';
      weekDayEl.ariaLabel = weekday.titleLong;
      weekDayEl.dataset.vcWeekDay = String(weekday.id);
      if (weekday.isWeekend) weekDayEl.dataset.vcWeekDayOff = '';

      if (isClickable) {
        const weekDayBtnEl = templateWeekDayBtnEl.cloneNode(false) as HTMLButtonElement;
        weekDayBtnEl.innerText = weekday.titleShort;
        weekDayBtnEl.ariaLabel = weekday.titleLong;
        weekDayEl.appendChild(weekDayBtnEl);
      } else {
        weekDayEl.innerText = weekday.titleShort;
      }

      weekEl.appendChild(weekDayEl);
    });
  });
};

export default createWeek;

```

### `package/src/scripts/creators/createWeekNumbers.ts`

```ts
import getWeekNumber from '@scripts/utils/getWeekNumber';
import type { Calendar, FormatDateString } from '@src/index';

const createWeekNumbers = (self: Calendar, firstDayWeek: number, days: number, weekNumbersEl: HTMLElement, datesEl: HTMLElement) => {
  if (!self.enableWeekNumbers) return;
  weekNumbersEl.textContent = '';

  const weekNumbersTitleEl = document.createElement('b');
  weekNumbersTitleEl.className = self.styles.weekNumbersTitle;
  weekNumbersTitleEl.innerText = '#';
  weekNumbersTitleEl.dataset.vcWeekNumbers = 'title';
  weekNumbersEl.appendChild(weekNumbersTitleEl);

  const weekNumbersContentEl = document.createElement('div');
  weekNumbersContentEl.className = self.styles.weekNumbersContent;
  weekNumbersContentEl.dataset.vcWeekNumbers = 'content';
  weekNumbersEl.appendChild(weekNumbersContentEl);

  // Only make it a button when there is something to activate, and leave the row/rowheader roles
  // out of it: the column sits beside the grid, not inside it.
  const isClickable = !!self.onClickWeekNumber;
  const templateWeekNumberEl = document.createElement(isClickable ? 'button' : 'b');
  if (isClickable) (templateWeekNumberEl as HTMLButtonElement).type = 'button';
  templateWeekNumberEl.className = self.styles.weekNumber;

  const dateBtnEl = datesEl.querySelectorAll<HTMLButtonElement>('[data-vc-date]');
  const weeksCount = Math.ceil((firstDayWeek + days) / 7);

  for (let i = 0; i < weeksCount; i++) {
    const index = i === 0 ? 6 : i * 7;
    const date = dateBtnEl[index].dataset.vcDate as FormatDateString;
    const weekNumber = getWeekNumber(date, self.firstWeekday);

    if (!weekNumber) return;

    const weekNumberEl = templateWeekNumberEl.cloneNode(false) as HTMLElement;
    weekNumberEl.innerText = String(weekNumber.week);
    weekNumberEl.dataset.vcWeekNumber = String(weekNumber.week);
    weekNumberEl.dataset.vcWeekYear = String(weekNumber.year);
    weekNumbersContentEl.appendChild(weekNumberEl);
  }
};

export default createWeekNumbers;

```

### `package/src/scripts/creators/createYears.ts`

```ts
import createLayouts from '@scripts/creators/createLayouts';
import setMonthOrYearModifier from '@scripts/creators/setMonthOrYearModifier';
import visibilityArrows from '@scripts/creators/visibilityArrows';
import visibilityTitle from '@scripts/creators/visibilityTitle';
import getDate from '@scripts/utils/getDate';
import updateRovingTabIndex from '@scripts/utils/rovingTabIndex';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const createYearEl = (self: Calendar, templateEl: HTMLButtonElement, selected: number, disabled: boolean, id: number) => {
  const yearWrapperEl = document.createElement('div');
  yearWrapperEl.className = self.styles.yearsCell;
  yearWrapperEl.dataset.vcYears = 'cell';
  yearWrapperEl.role = 'gridcell';

  const yearEl = templateEl.cloneNode(false) as HTMLButtonElement;
  yearEl.className = self.styles.yearsYear;
  yearEl.innerText = String(id);
  yearEl.ariaLabel = String(id);
  yearEl.dataset.vcYearsYear = `${id}`;
  if (disabled) yearEl.ariaDisabled = 'true';
  if (disabled) yearEl.tabIndex = -1;
  yearEl.disabled = disabled;

  yearWrapperEl.appendChild(yearEl);

  setMonthOrYearModifier(self, yearEl, 'year', selected === id, false);
  return yearWrapperEl;
};

const createYears = (self: Calendar, target?: HTMLElement) => {
  const selectedYear = target?.dataset.vcYear ? Number(target.dataset.vcYear) : self.context.selectedYear;

  setContext(self, 'currentType', 'year');
  createLayouts(self, target);
  visibilityTitle(self);
  visibilityArrows(self);

  const yearsEl = self.context.mainElement.querySelector('[data-vc="years"]');
  if (!self.selectionYearsMode || !yearsEl) return;

  const relationshipID = self.type !== 'multiple' ? 0 : self.context.selectedYear === selectedYear ? 0 : 1;

  const templateYearEl = document.createElement('button');
  templateYearEl.type = 'button';

  let rowEl: HTMLDivElement | undefined;

  for (let i = self.context.displayYear - 7; i < self.context.displayYear + 8; i++) {
    if ((i - (self.context.displayYear - 7)) % 5 === 0) {
      rowEl = document.createElement('div');
      rowEl.className = self.styles.yearsRow;
      rowEl.dataset.vcYears = 'row';
      rowEl.role = 'row';
      yearsEl.appendChild(rowEl);
    }

    const yearDisabled = i < getDate(self.context.dateMin).getFullYear() + relationshipID || i > getDate(self.context.dateMax).getFullYear();
    const yearEl = createYearEl(self, templateYearEl, selectedYear, yearDisabled, i);
    rowEl?.appendChild(yearEl);
    if (self.onCreateYearEls) self.onCreateYearEls(self, yearEl);
  }

  updateRovingTabIndex(self);
};

export default createYears;

```

### `package/src/scripts/creators/setMonthOrYearModifier.ts`

```ts
import visibilityArrows from '@scripts/creators/visibilityArrows';
import visibilityTitle from '@scripts/creators/visibilityTitle';
import setContext from '@scripts/utils/setContext';
import type { Calendar, Range } from '@src/index';

const setYearModifier = (self: Calendar, el: HTMLButtonElement, type: 'month' | 'year', selected: boolean, reset: boolean) => {
  const selectors = {
    month: '[data-vc-months-month]',
    year: '[data-vc-years-year]',
  } as const;

  const attributes = {
    month: {
      selected: 'data-vc-months-month-selected',
      aria: 'aria-selected',
      value: 'vcMonthsMonth',
      selectedProperty: 'selectedMonth',
    },
    year: {
      selected: 'data-vc-years-year-selected',
      aria: 'aria-selected',
      value: 'vcYearsYear',
      selectedProperty: 'selectedYear',
    },
  } as const;

  if (reset) {
    self.context.mainElement.querySelectorAll<HTMLElement>(selectors[type])?.forEach((el) => {
      el.removeAttribute(attributes[type].selected);
      el.parentElement?.removeAttribute(attributes[type].aria);
    });

    setContext(self, attributes[type].selectedProperty, Number(el.dataset[attributes[type].value]) as Range<12>);
    visibilityTitle(self);
    if (type === 'year') visibilityArrows(self);
  }

  if (selected) {
    el.setAttribute(attributes[type].selected, '');
    el.parentElement?.setAttribute(attributes[type].aria, 'true');
  }
};

export default setYearModifier;

```

### `package/src/scripts/creators/visibilityArrows.ts`

```ts
import getDate from '@scripts/utils/getDate';
import getDateString from '@scripts/utils/getDateString';
import type { Calendar } from '@src/index';

const setVisibilityArrows = (arrowPrevEl: HTMLElement, arrowNextEl: HTMLElement, isArrowPrevHidden: boolean, isArrowNextHidden: boolean) => {
  arrowPrevEl.style.visibility = isArrowPrevHidden ? 'hidden' : '';
  arrowNextEl.style.visibility = isArrowNextHidden ? 'hidden' : '';
};

const handleDefaultType = (self: Calendar, arrowPrevEl: HTMLElement, arrowNextEl: HTMLElement) => {
  const currentSelectedDate = getDate(getDateString(new Date(self.context.selectedYear as number, self.context.selectedMonth as number, 1)));
  const jumpDateMin = new Date(currentSelectedDate.getTime());
  const jumpDateMax = new Date(currentSelectedDate.getTime());
  jumpDateMin.setMonth(jumpDateMin.getMonth() - self.monthsToSwitch);
  jumpDateMax.setMonth(jumpDateMax.getMonth() + self.monthsToSwitch);

  const dateMin = getDate(self.context.dateMin);
  const dateMax = getDate(self.context.dateMax);

  if (!self.selectionYearsMode) {
    dateMin.setFullYear(currentSelectedDate.getFullYear());
    dateMax.setFullYear(currentSelectedDate.getFullYear());
  }

  const isArrowPrevHidden =
    !self.selectionMonthsMode ||
    jumpDateMin.getFullYear() < dateMin.getFullYear() ||
    (jumpDateMin.getFullYear() === dateMin.getFullYear() && jumpDateMin.getMonth() < dateMin.getMonth());
  const isArrowNextHidden =
    !self.selectionMonthsMode ||
    jumpDateMax.getFullYear() > dateMax.getFullYear() ||
    (jumpDateMax.getFullYear() === dateMax.getFullYear() && jumpDateMax.getMonth() > dateMax.getMonth() - (self.context.displayMonthsCount - 1));

  setVisibilityArrows(arrowPrevEl, arrowNextEl, isArrowPrevHidden, isArrowNextHidden);
};

const handleYearType = (self: Calendar, arrowPrevEl: HTMLElement, arrowNextEl: HTMLElement) => {
  const dateMin = getDate(self.context.dateMin);
  const dateMax = getDate(self.context.dateMax);
  const isArrowPrevHidden = !!(dateMin.getFullYear() && self.context.displayYear - 7 <= dateMin.getFullYear());
  const isArrowNextHidden = !!(dateMax.getFullYear() && self.context.displayYear + 7 >= dateMax.getFullYear());

  setVisibilityArrows(arrowPrevEl, arrowNextEl, isArrowPrevHidden, isArrowNextHidden);
};

const handleWeekType = (self: Calendar, arrowPrevEl: HTMLElement, arrowNextEl: HTMLElement) => {
  const weekStart = getDate(self.context.displayWeekDate);
  const prevWeekStart = new Date(weekStart);
  prevWeekStart.setDate(weekStart.getDate() - 7);
  const prevWeekEnd = new Date(weekStart);
  prevWeekEnd.setDate(weekStart.getDate() - 1);
  const nextWeekStart = new Date(weekStart);
  nextWeekStart.setDate(weekStart.getDate() + 7);
  const ownerYear = (start: Date) => {
    const reference = new Date(start);
    reference.setDate(start.getDate() + 3);
    return reference.getFullYear();
  };
  const prevChangesYear = !self.selectionYearsMode && ownerYear(prevWeekStart) !== self.context.selectedYear;
  const nextChangesYear = !self.selectionYearsMode && ownerYear(nextWeekStart) !== self.context.selectedYear;

  const isArrowPrevHidden = !self.selectionMonthsMode || prevChangesYear || prevWeekEnd < getDate(self.context.dateMin);
  const isArrowNextHidden = !self.selectionMonthsMode || nextChangesYear || nextWeekStart > getDate(self.context.dateMax);

  setVisibilityArrows(arrowPrevEl, arrowNextEl, isArrowPrevHidden, isArrowNextHidden);
};

const visibilityArrows = (self: Calendar) => {
  if (self.context.currentType === 'month') return;

  const arrowPrevEl = self.context.mainElement.querySelector<HTMLElement>('[data-vc-arrow="prev"]');
  const arrowNextEl = self.context.mainElement.querySelector<HTMLElement>('[data-vc-arrow="next"]');
  if (!arrowPrevEl || !arrowNextEl) return;

  const updateType = {
    default: () => handleDefaultType(self, arrowPrevEl, arrowNextEl),
    year: () => handleYearType(self, arrowPrevEl, arrowNextEl),
    week: () => handleWeekType(self, arrowPrevEl, arrowNextEl),
  };

  updateType[self.context.currentType === 'multiple' ? 'default' : self.context.currentType]();
};

export default visibilityArrows;

```

### `package/src/scripts/creators/visibilityTitle.ts`

```ts
import type { Calendar } from '@src/index';

const visibilityHandler = (self: Calendar, el: HTMLButtonElement, index: number, initDate: Date, type: 'month' | 'year') => {
  const yearID = new Date(initDate.setFullYear(self.context.selectedYear as number, (self.context.selectedMonth as number) + index)).getFullYear();
  const monthID = new Date(initDate.setMonth((self.context.selectedMonth as number) + index)).getMonth();
  const monthLabel = self.context.locale.months.long[monthID];

  const columnEl = el.closest('[data-vc="column"]');
  if (columnEl) columnEl.ariaLabel = `${monthLabel} ${yearID}`;

  const value = {
    month: { id: monthID, label: monthLabel },
    year: { id: yearID, label: yearID },
  };

  el.innerText = String(value[type].label);
  el.dataset[`vc${type.charAt(0).toUpperCase() + type.slice(1)}`] = String(value[type].id);
  el.ariaLabel = `${self.labels[type]} ${value[type].label}`;

  const typesMap = { month: self.selectionMonthsMode, year: self.selectionYearsMode };
  const isDisabled = typesMap[type] === false || typesMap[type] === 'only-arrows';
  if (isDisabled) el.tabIndex = -1;
  el.disabled = isDisabled;
};

const visibilityTitle = (self: Calendar) => {
  const monthEls = self.context.mainElement.querySelectorAll<HTMLButtonElement>('[data-vc="month"]');
  const yearEls = self.context.mainElement.querySelectorAll<HTMLButtonElement>('[data-vc="year"]');
  const initDate = new Date(self.context.selectedYear as number, self.context.selectedMonth as number, 1);

  [monthEls, yearEls].forEach((els) => els?.forEach((el, index) => visibilityHandler(self, el, index, initDate, el.dataset.vc as 'month' | 'year')));
};

export default visibilityTitle;

```

### `package/src/scripts/handles/handleArrowKeys.ts`

```ts
import { focusRovingItem } from '@scripts/utils/rovingTabIndex';
import type { Calendar } from '@src/index';

const handleArrowKeys = (self: Calendar) => {
  type Grid = { container: string; row: string; item: string };
  const grids: Grid[] = [
    { container: '[data-vc="dates"]', row: '[data-vc-dates="row"]', item: '[data-vc-date-btn]' },
    { container: '[data-vc="months"]', row: '[data-vc-months="row"]', item: '[data-vc-months-month]' },
    { container: '[data-vc="years"]', row: '[data-vc-years="row"]', item: '[data-vc-years-year]' },
  ];

  const isEnabled = (button: HTMLButtonElement) => !button.disabled && button.getAttribute('aria-disabled') !== 'true';

  const getVerticalTarget = (gridEl: HTMLElement, grid: Grid, button: HTMLButtonElement, direction: -1 | 1) => {
    const currentRow = button.closest<HTMLElement>(grid.row);
    if (!currentRow) return button;

    const rows = Array.from(gridEl.querySelectorAll<HTMLElement>(grid.row));
    const rowIndex = rows.indexOf(currentRow);
    const columnIndex = Array.from(currentRow.children).indexOf(button.parentElement as Element);
    const targetRow = rows[rowIndex + direction];
    const target = targetRow?.children[columnIndex]?.querySelector<HTMLButtonElement>(grid.item);

    return target && isEnabled(target) ? target : button;
  };

  const onKeyDown = (event: KeyboardEvent) => {
    const target = (event.target as HTMLElement).closest<HTMLButtonElement>('button');
    if (!target || !['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key)) return;

    const grid = grids.find((item) => target.matches(item.item));
    const gridEl = grid ? target.closest<HTMLElement>(grid.container) : null;
    if (!grid || !gridEl || gridEl.closest('[data-vc-ghost]')) return;

    const buttons = Array.from(gridEl.querySelectorAll<HTMLButtonElement>(grid.item)).filter(isEnabled);
    const currentIndex = buttons.indexOf(target as HTMLButtonElement);
    if (currentIndex === -1) return;

    const nextButton = {
      ArrowUp: () => getVerticalTarget(gridEl, grid, target, -1),
      ArrowDown: () => getVerticalTarget(gridEl, grid, target, 1),
      ArrowLeft: () => buttons[Math.max(0, currentIndex - 1)],
      ArrowRight: () => buttons[Math.min(buttons.length - 1, currentIndex + 1)],
    }[event.key]!;

    // Arrow keys move within their grid and must not scroll the page along with them.
    event.preventDefault();
    nextButton()?.focus();
  };

  self.context.mainElement.addEventListener('keydown', onKeyDown);
  self.context.mainElement.addEventListener('focusin', focusRovingItem);

  return () => {
    self.context.mainElement.removeEventListener('keydown', onKeyDown);
    self.context.mainElement.removeEventListener('focusin', focusRovingItem);
  };
};

export default handleArrowKeys;

```

### `package/src/scripts/handles/handleClick/handleClick.ts`

```ts
import handleClickArrow from '@scripts/handles/handleClick/handleClickArrow';
import handleClickCollapse from '@scripts/handles/handleClick/handleClickCollapse';
import handleClickDate from '@scripts/handles/handleClick/handleClickDate';
import handleClickMonthOrYear from '@scripts/handles/handleClick/handleClickMonthOrYear';
import { handleClickWeekDay, handleClickWeekNumber } from '@scripts/handles/handleClick/handleClickWeek';
import type { Calendar } from '@src/index';

const handleClick = (self: Calendar) => {
  const clickEventHandler = (e: MouseEvent) => {
    handleClickArrow(self, e);
    handleClickWeekDay(self, e);
    handleClickWeekNumber(self, e);
    handleClickDate(self, e);
    handleClickMonthOrYear(self, e);
    handleClickCollapse(self, e);
  };

  self.context.mainElement.addEventListener('click', clickEventHandler);
  return () => self.context.mainElement.removeEventListener('click', clickEventHandler);
};

export default handleClick;

```

### `package/src/scripts/handles/handleClick/handleClickArrow.ts`

```ts
import handleNavigate, { type Route } from '@scripts/handles/handleNavigate';
import type { Calendar } from '@src/index';

const handleClickArrow = (self: Calendar, event: MouseEvent) => {
  const element = event.target as HTMLElement;
  const arrowEl: HTMLElement | null = element.closest('[data-vc-arrow]');

  if (!arrowEl) return;

  handleNavigate(self, arrowEl.dataset.vcArrow as Route, element);

  if (self.onClickArrow) self.onClickArrow(self, event);
};

export default handleClickArrow;

```

### `package/src/scripts/handles/handleClick/handleClickCollapse.ts`

```ts
import buildCollapse from '@scripts/handles/handleGestures/collapseTransition';
import type { Calendar } from '@src/index';

const handleClickCollapse = (self: Calendar, event: MouseEvent) => {
  if (!self.enableCollapse || !['default', 'week'].includes(self.context.currentType) || !(event.target as HTMLElement).closest('[data-vc="collapse"]')) return;

  const transition = buildCollapse(self);
  if (!transition) return;
  transition.settle(transition.from === 0);
};

export default handleClickCollapse;

```

### `package/src/scripts/handles/handleClick/handleClickDate.ts`

```ts
import updateDateModifiers from '@scripts/creators/createDates/updateDateModifiers';
import handleNavigate from '@scripts/handles/handleNavigate';
import handleSelectDate from '@scripts/handles/handleSelectDate';
import handleSelectDateRanged from '@scripts/handles/handleSelectDateRange/handleSelectDateRange';
import type { Calendar } from '@src/index';

const handleClickDate = (self: Calendar, event: MouseEvent) => {
  const element = event.target as HTMLElement;
  const dateBtnEl = element.closest<HTMLButtonElement>('[data-vc-date-btn]');

  if (!self.selectionDatesMode || !['single', 'multiple', 'multiple-ranged'].includes(self.selectionDatesMode) || !dateBtnEl) return;

  const dateEl = dateBtnEl.closest('[data-vc-date]') as HTMLElement;
  const daySelectionActions = {
    single: () => handleSelectDate(self, dateEl, false),
    multiple: () => handleSelectDate(self, dateEl, true),
    'multiple-ranged': () => handleSelectDateRanged(self, dateEl),
  };
  daySelectionActions[self.selectionDatesMode]();
  self.context.selectedDates?.sort((a, b) => +new Date(a) - +new Date(b));

  if (self.onClickDate) self.onClickDate(self, event);
  if (self.inputMode && self.context.inputElement && self.context.mainElement && self.onChangeToInput) self.onChangeToInput(self, event);

  const dayPrevEl = element.closest('[data-vc-date-month="prev"]');
  const dayNextEl = element.closest('[data-vc-date-month="next"]');

  const actionMapping = {
    prev: () => (self.enableMonthChangeOnDayClick ? handleNavigate(self, 'prev') : updateDateModifiers(self)),
    next: () => (self.enableMonthChangeOnDayClick ? handleNavigate(self, 'next') : updateDateModifiers(self)),
    current: () => updateDateModifiers(self),
  };

  actionMapping[dayPrevEl ? 'prev' : dayNextEl ? 'next' : 'current']();
};

export default handleClickDate;

```

### `package/src/scripts/handles/handleClick/handleClickMonthOrYear.ts`

```ts
import create from '@scripts/creators/create';
import createMonths from '@scripts/creators/createMonths';
import createYears from '@scripts/creators/createYears';
import setMonthOrYearModifier from '@scripts/creators/setMonthOrYearModifier';
import animate, { captureOpacity, playOpacity } from '@scripts/utils/animate';
import getColumnID from '@scripts/utils/getColumnID';
import getDate from '@scripts/utils/getDate';
import setContext from '@scripts/utils/setContext';
import type { Calendar, Range } from '@src/index';

const typeClick = ['month', 'year'] as const;

const WRAPPER = '[data-vc="wrapper"]';
const COLUMN = '[data-vc="column"]';

const getColumnIndex = (self: Calendar, el: HTMLElement) => {
  const columnEl = el.closest<HTMLElement>(COLUMN);
  if (!columnEl) return 0;
  return Array.from(self.context.mainElement.querySelectorAll<HTMLElement>(COLUMN)).indexOf(columnEl);
};

// Only one column is re-rendered, but the dim of the others changes along with it,
// so the opacity is captured before the render and played out afterwards.
const changeType = (self: Calendar, columnIndex: number, render: () => void) => {
  const dim = captureOpacity(self, COLUMN);
  animate(self, WRAPPER, 'fade', render, columnIndex);
  playOpacity(self, COLUMN, dim);
};

// Both callers leave the picker the same way: find which column is showing it, switch the
// context back, animate that column, and restore focus to the header that opened it.
const leavePicker = (self: Calendar, type: (typeof typeClick)[number]) => {
  const { columnID } = getColumnID(self, self.context.currentType);
  setContext(self, 'currentType', self.type);
  changeType(self, columnID, () => create(self));
  self.context.mainElement.querySelector<HTMLElement>(`[data-vc="${type}"]`)?.focus();
};

const getValue = (self: Calendar, type: (typeof typeClick)[number], id: number) => {
  const { currentValue, columnID } = getColumnID(self, type);

  if (self.context.currentType === 'month' && columnID >= 0) return id - columnID;
  if (self.context.currentType === 'year' && self.context.selectedYear !== currentValue) return id - 1;
  return id;
};

const handleMultipleYearSelection = (self: Calendar, itemEl: HTMLElement) => {
  const selectedYear = getValue(self, 'year', Number(itemEl.dataset.vcYearsYear));
  const dateMin = getDate(self.context.dateMin);
  const dateMax = getDate(self.context.dateMax);
  const monthCount = self.context.displayMonthsCount - 1;
  const { columnID } = getColumnID(self, 'year');

  const isBeforeMinDate = self.context.selectedMonth < dateMin.getMonth() && selectedYear <= dateMin.getFullYear();
  const isAfterMaxDate = self.context.selectedMonth > dateMax.getMonth() - monthCount + columnID && selectedYear >= dateMax.getFullYear();
  const isBeforeMinYear = selectedYear < dateMin.getFullYear();
  const isAfterMaxYear = selectedYear > dateMax.getFullYear();

  const newSelectedYear = isBeforeMinDate || isBeforeMinYear ? dateMin.getFullYear() : isAfterMaxDate || isAfterMaxYear ? dateMax.getFullYear() : selectedYear;
  const newSelectedMonth =
    isBeforeMinDate || isBeforeMinYear
      ? dateMin.getMonth()
      : isAfterMaxDate || isAfterMaxYear
        ? dateMax.getMonth() - monthCount + columnID
        : self.context.selectedMonth;

  setContext(self, 'selectedYear', newSelectedYear);
  setContext(self, 'selectedMonth', newSelectedMonth as Range<12>);
};

const handleMultipleMonthSelection = (self: Calendar, itemEl: HTMLElement) => {
  const column = itemEl.closest('[data-vc-column="month"]') as HTMLElement;
  const yearEl = column.querySelector('[data-vc="year"]') as HTMLElement;
  const selectedMonth = getValue(self, 'month', Number(itemEl.dataset.vcMonthsMonth));
  const selectedYear = Number(yearEl.dataset.vcYear);
  const dateMin = getDate(self.context.dateMin);
  const dateMax = getDate(self.context.dateMax);

  const isBeforeMinDate = selectedMonth < dateMin.getMonth() && selectedYear <= dateMin.getFullYear();
  const isAfterMaxDate = selectedMonth > dateMax.getMonth() && selectedYear >= dateMax.getFullYear();

  setContext(self, 'selectedYear', selectedYear);
  setContext(self, 'selectedMonth', (isBeforeMinDate ? dateMin.getMonth() : isAfterMaxDate ? dateMax.getMonth() : selectedMonth) as Range<12>);
};

const handleItemClick = (self: Calendar, event: MouseEvent, type: (typeof typeClick)[number], itemEl: HTMLButtonElement) => {
  const selectByType = {
    year: () => {
      if (self.type === 'multiple') return handleMultipleYearSelection(self, itemEl);
      setContext(self, 'selectedYear', Number(itemEl.dataset.vcYearsYear));
    },
    month: () => {
      if (self.type === 'multiple') return handleMultipleMonthSelection(self, itemEl);
      setContext(self, 'selectedMonth', Number(itemEl.dataset.vcMonthsMonth) as Range<12>);
    },
  };
  selectByType[type]();

  const actionByType = {
    year: () => self.onClickYear?.(self, event),
    month: () => self.onClickMonth?.(self, event),
  };
  actionByType[type]();

  if (self.context.currentType !== self.type) {
    leavePicker(self, type);
  } else {
    setMonthOrYearModifier(self, itemEl, type, true, true);
  }
};

// The picker is opened by a click, so the focus follows it onto its own tab stop. It must not
// move on any other render: navigating the year list would otherwise pull the focus off the arrow.
const focusPicker = (self: Calendar, type: (typeof typeClick)[number], columnEl: HTMLElement | null) =>
  (columnEl ?? self.context.mainElement).querySelector<HTMLElement>(`[data-vc-${type}s-${type}][tabindex="0"]`)?.focus();

const handleClickType = (self: Calendar, event: MouseEvent, type: (typeof typeClick)[number]) => {
  const target = event.target as HTMLElement;

  const headerEl = target.closest<HTMLElement>(`[data-vc="${type}"]`);
  const columnIndex = getColumnIndex(self, target);
  const createByType = {
    year: () => changeType(self, columnIndex, () => createYears(self, target)),
    month: () => changeType(self, columnIndex, () => createMonths(self, target)),
  };
  if (headerEl && self.onClickTitle) self.onClickTitle(self, event);
  if (headerEl && self.context.currentType !== type) {
    const columnEl = target.closest<HTMLElement>(COLUMN);
    createByType[type]();
    return focusPicker(self, type, columnEl);
  }

  const itemEl = target.closest<HTMLButtonElement>(`[data-vc-${type}s-${type}]`);
  if (itemEl) return handleItemClick(self, event, type, itemEl);

  const gridEl = target.closest<HTMLElement>('[data-vc="grid"]');
  const columnEl = target.closest<HTMLElement>('[data-vc="column"]');

  if ((self.context.currentType === type && headerEl) || (self.type === 'multiple' && self.context.currentType === type && gridEl && !columnEl)) {
    leavePicker(self, type);
  }
};

const handleClickMonthOrYear = (self: Calendar, event: MouseEvent) => {
  const typesMap = { month: self.selectionMonthsMode, year: self.selectionYearsMode };

  typeClick.forEach((type) => {
    if (!typesMap[type] || !event.target) return;
    handleClickType(self, event, type);
  });
};

export default handleClickMonthOrYear;

```

### `package/src/scripts/handles/handleClick/handleClickWeek.ts`

```ts
import type { Calendar } from '@src/index';

export const handleClickWeekNumber = (self: Calendar, event: MouseEvent) => {
  if (!self.enableWeekNumbers || !self.onClickWeekNumber) return;

  const weekNumberEl = (event.target as HTMLElement).closest<HTMLElement>('[data-vc-week-number]');
  const daysToWeeks = self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc-date-week-number]');

  if (!weekNumberEl || !daysToWeeks[0]) return;

  const weekNumberValue = Number(weekNumberEl.innerText);
  const yearWeek = Number(weekNumberEl.dataset.vcWeekYear);
  const daysOfThisWeek = Array.from(daysToWeeks).filter((day) => Number((day as HTMLElement).dataset.vcDateWeekNumber) === weekNumberValue);

  self.onClickWeekNumber(self, weekNumberValue, yearWeek, daysOfThisWeek, event);
};

export const handleClickWeekDay = (self: Calendar, event: MouseEvent) => {
  if (!self.onClickWeekDay) return;

  const weekDayEl = (event.target as HTMLElement).closest<HTMLElement>('[data-vc-week-day]');
  const columnEl = (event.target as HTMLElement).closest<HTMLElement>('[data-vc="column"]');
  const daysToWeeks = columnEl
    ? columnEl.querySelectorAll<HTMLElement>('[data-vc-date-week-day]')
    : self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc-date-week-day]');

  if (!weekDayEl || !daysToWeeks[0]) return;

  const weekDayValue = Number(weekDayEl.dataset.vcWeekDay);
  const daysOfThisWeek = Array.from(daysToWeeks).filter((day) => Number((day as HTMLElement).dataset.vcDateWeekDay) === weekDayValue);

  self.onClickWeekDay(self, weekDayValue, daysOfThisWeek, event);
};

```

### `package/src/scripts/handles/handleGestures/collapseTransition.ts`

```ts
import create from '@scripts/creators/create';
import createDates from '@scripts/creators/createDates/createDates';
import visibilityArrows from '@scripts/creators/visibilityArrows';
import { scrub, type Transition } from '@scripts/handles/handleGestures/transition';
import { collapseEffect, getTiming } from '@scripts/utils/animate';
import initWeek from '@scripts/utils/initVariables/initWeek';
import setContext from '@scripts/utils/setContext';
import updateNavigationA11y from '@scripts/utils/updateNavigationA11y';
import type { Calendar, TypesCalendar } from '@src/index';

const setType = (self: Calendar, type: TypesCalendar) => {
  self.type = type;
  setContext(self, 'currentType', type);
  create(self);
};

// Keep the collapse control mounted so its CSS rotation can run with the grid transition.
const stageDefault = (self: Calendar) => {
  self.type = 'default';
  setContext(self, 'currentType', 'default');
  createDates(self);
  visibilityArrows(self);
  updateNavigationA11y(self, 'month');
};

// Both directions animate the month DOM and swap to the resting layout only at an endpoint.
const buildCollapse = (self: Calendar): Transition | null => {
  const { mainElement } = self.context;
  if (!['default', 'week'].includes(self.context.currentType) || mainElement.querySelector('[data-vc-collapsing]')) return null;

  const datesEl = mainElement.querySelector<HTMLElement>('[data-vc="dates"]');
  if (!datesEl) return null;

  const wasCollapsed = self.context.currentType === 'week';
  if (wasCollapsed) stageDefault(self);
  else initWeek(self, true);

  const rows = Array.from(datesEl.querySelectorAll<HTMLElement>('[data-vc-dates="row"]'));
  if (!rows.length) {
    if (wasCollapsed) setType(self, 'week');
    return null;
  }

  const targetRow = rows.find((row) => row.querySelector(`[data-vc-date="${self.context.displayWeekDate}"]`)) ?? rows[0];
  const fromHeight = datesEl.offsetHeight;
  const targetHeight = targetRow.offsetHeight;

  const offset = targetRow.offsetTop - rows[0].offsetTop;
  const timing = { ...getTiming(self, collapseEffect), fill: 'both' as const };
  const duration = timing.duration;
  const canAnimate = typeof datesEl.animate === 'function';

  if (canAnimate) datesEl.dataset.vcCollapsing = '';

  const animations = canAnimate
    ? [
        datesEl.animate([{ height: `${fromHeight}px` }, { height: `${targetHeight}px` }], timing),
        ...rows.map((row) =>
          row.animate(
            [
              { transform: 'none', opacity: 1 },
              { transform: `translateY(${-offset}px)`, opacity: row === targetRow ? 1 : 0 },
            ],
            timing,
          ),
        ),
      ]
    : [];

  const { track, seek, settle } = scrub(self, animations, duration, (toWeek) => {
    animations.forEach((animation) => animation.cancel());
    if (self.context.isDestroyed || self.context.mainElement !== mainElement || !datesEl.isConnected) return;
    if (toWeek) return setType(self, 'week');
    if (wasCollapsed) return setType(self, 'default');
    datesEl.removeAttribute('data-vc-collapsing');
  });

  const from = wasCollapsed ? 1 : 0;
  seek(from);

  return { distance: fromHeight - targetHeight, from, track, seek, settle };
};

export default buildCollapse;

```

### `package/src/scripts/handles/handleGestures/dragTracker.ts`

```ts
const VELOCITY_WINDOW_MS = 170;
type Point = { x: number; y: number; time: number };

const pointOf = (event: PointerEvent): Point => ({ x: event.clientX, y: event.clientY, time: event.timeStamp });

export type DragTracker = ReturnType<typeof createDragTracker>;

const createDragTracker = (event: PointerEvent) => {
  const origin = pointOf(event);
  let start = origin;
  let last = origin;

  return {
    origin,

    move: (moveEvent: PointerEvent) => {
      last = pointOf(moveEvent);
      if (last.time - start.time > VELOCITY_WINDOW_MS) start = last;
    },

    velocity: (upEvent: PointerEvent, vertical: boolean) => {
      const elapsed = last.time - start.time;
      if (!elapsed || upEvent.timeStamp - last.time > VELOCITY_WINDOW_MS) return 0;
      return (vertical ? last.y - start.y : last.x - start.x) / elapsed;
    },
  };
};

export default createDragTracker;

```

### `package/src/scripts/handles/handleGestures/handleGestures.ts`

```ts
import buildCollapse from '@scripts/handles/handleGestures/collapseTransition';
import createDragTracker, { type DragTracker } from '@scripts/handles/handleGestures/dragTracker';
import buildSwipe from '@scripts/handles/handleGestures/swipeTransition';
import { clamp, type Transition } from '@scripts/handles/handleGestures/transition';
import type { Calendar } from '@src/index';

const SLOP = { mouse: 4, pen: 6, touch: 10 } as const;
const slopFor = (event: PointerEvent) => SLOP[event.pointerType as keyof typeof SLOP] ?? SLOP.touch;
const COMMIT = 0.25;
const PROJECTION = 200; // ms
const CLICK_GRACE = 500;

const SWIPE_SURFACE = '[data-vc="content"]';
const COLLAPSE_SURFACE = '[data-vc="collapse"]';

const gestureCleanups = new WeakMap<HTMLElement, () => void>();

export const cleanupGestures = (mainElement: HTMLElement) => gestureCleanups.get(mainElement)?.();

type Drag = {
  pointerId: number;
  tracker: DragTracker;
  slop: number;
  vertical: boolean;
  transition: Transition | null;
  sign: number;
  distance: number;
};

const handleGestures = (self: Calendar) => {
  const { mainElement } = self.context;
  cleanupGestures(mainElement);
  let drag: Drag | null = null;
  let draggedAt = 0;
  let activeListenersBound = false;

  const capture = (pointerId: number) => {
    try {
      mainElement.setPointerCapture(pointerId);
      return true;
    } catch {
      return false;
    }
  };

  const stopDragging = () => {
    const pointerId = drag?.pointerId;
    drag = null;
    mainElement.removeAttribute('data-vc-dragging');
    removeActiveListeners();
    if (pointerId !== undefined) release(pointerId);
  };

  const release = (pointerId: number) => {
    try {
      mainElement.releasePointerCapture(pointerId);
    } catch {
      // Pointer capture may already have been released by the browser.
    }
  };

  const deltaOf = (event: PointerEvent, current: Drag) =>
    current.vertical ? event.clientY - current.tracker.origin.y : event.clientX - current.tracker.origin.x;

  const progressOf = (event: PointerEvent, current: Drag) =>
    clamp((current.transition as Transition).from + (current.sign * deltaOf(event, current)) / current.distance);

  const onPointerDown = (event: PointerEvent) => {
    draggedAt = 0;
    if (!event.isPrimary || event.button !== 0) return;
    if (drag) stopDragging();

    const target = event.target as HTMLElement;
    const vertical = !!(self.enableCollapse && target.closest(COLLAPSE_SURFACE));
    const horizontal = !!(self.enableSwipe && target.closest(SWIPE_SURFACE) && !target.closest('[data-vc-ghost]'));
    if (!vertical && !horizontal) return;

    drag = { pointerId: event.pointerId, tracker: createDragTracker(event), slop: slopFor(event), vertical, transition: null, sign: -1, distance: 1 };
    addActiveListeners();
  };

  const startTransition = (event: PointerEvent, current: Drag, dx: number) => {
    if (!capture(event.pointerId)) return stopDragging();

    try {
      const transition = current.vertical ? buildCollapse(self) : buildSwipe(self, dx < 0 ? 'next' : 'prev', event.target as HTMLElement);
      if (!transition || !transition.distance) {
        return stopDragging();
      }

      transition.track();
      current.transition = transition;
      current.sign = current.vertical || dx < 0 ? -1 : 1;
      current.distance = transition.distance;
      mainElement.dataset.vcDragging = '';
    } catch (error) {
      stopDragging();
      throw error;
    }
  };

  const onPointerMove = (event: PointerEvent) => {
    const current = drag;
    if (!current || event.pointerId !== current.pointerId) return;

    current.tracker.move(event);
    const dx = event.clientX - current.tracker.origin.x;
    const dy = event.clientY - current.tracker.origin.y;

    if (!current.transition) {
      if (Math.abs(dx) < current.slop && Math.abs(dy) < current.slop) return;
      // Do not claim the page's vertical scroll from the horizontal swipe surface.
      if (current.vertical !== Math.abs(dy) > Math.abs(dx)) return stopDragging();
      startTransition(event, current, dx);
      if (!drag) return;
    }

    draggedAt = Date.now();
    (current.transition as Transition).seek(progressOf(event, current));
  };

  const endDrag = (event: PointerEvent, lost: boolean) => {
    const current = drag;
    if (!current || event.pointerId !== current.pointerId) return;

    const { transition } = current;
    if (transition) {
      const velocity = lost ? 0 : current.tracker.velocity(event, current.vertical);
      const projected = progressOf(event, current) + (current.sign * velocity * PROJECTION) / current.distance;
      const toEnd = transition.from === 0 ? projected > COMMIT : projected >= 1 - COMMIT;

      transition.settle(lost ? transition.from === 1 : toEnd);
      draggedAt = Date.now();
    }
    stopDragging();
  };

  const onPointerUp = (event: PointerEvent) => endDrag(event, false);
  const onPointerCancel = (event: PointerEvent) => endDrag(event, true);
  const onLostCapture = (event: PointerEvent) => {
    // Transferring implicit touch capture from the control emits a bubbling event from that control.
    if (event.target !== mainElement) return;
    endDrag(event, true);
  };

  const onClick = (event: MouseEvent) => {
    if (!draggedAt || Date.now() - draggedAt > CLICK_GRACE) return;
    draggedAt = 0;
    event.stopPropagation();
    event.preventDefault();
  };

  const activeWindowListeners = [
    ['pointermove', onPointerMove],
    ['pointerup', onPointerUp],
    ['pointercancel', onPointerCancel],
  ] as const;

  function addActiveListeners() {
    if (activeListenersBound) return;
    activeListenersBound = true;
    activeWindowListeners.forEach(([type, listener]) => window.addEventListener(type, listener as EventListener));
    mainElement.addEventListener('lostpointercapture', onLostCapture);
  }

  function removeActiveListeners() {
    if (!activeListenersBound) return;
    activeListenersBound = false;
    activeWindowListeners.forEach(([type, listener]) => window.removeEventListener(type, listener as EventListener));
    mainElement.removeEventListener('lostpointercapture', onLostCapture);
  }

  mainElement.addEventListener('pointerdown', onPointerDown);
  mainElement.addEventListener('click', onClick, { capture: true });

  const cleanup = () => {
    stopDragging();
    removeActiveListeners();
    mainElement.removeEventListener('pointerdown', onPointerDown);
    mainElement.removeEventListener('click', onClick, { capture: true });
    gestureCleanups.delete(mainElement);
  };

  gestureCleanups.set(mainElement, cleanup);
  return cleanup;
};

export default handleGestures;

```

### `package/src/scripts/handles/handleGestures/swipeTransition.ts`

```ts
import visibilityArrows from '@scripts/creators/visibilityArrows';
import visibilityTitle from '@scripts/creators/visibilityTitle';
import { scrub, type Transition } from '@scripts/handles/handleGestures/transition';
import { getNavigator, type Route } from '@scripts/handles/handleNavigate';
import { cleanupPending, createGhost, dropLayers, getTiming, type Layer, slideEffect } from '@scripts/utils/animate';
import type { Calendar } from '@src/index';

// Keep calendar state unchanged until the staged neighbouring period is committed.
const buildSwipe = (self: Calendar, route: Route, target: HTMLElement): Transition | null => {
  const navigator = getNavigator(self);
  if (!navigator) return null;

  const arrowEl = self.context.mainElement.querySelector<HTMLElement>(`[data-vc-arrow="${route}"]`);
  if (!arrowEl || arrowEl.style.visibility === 'hidden') return null;

  const { mainElement } = self.context;
  const containers = () => Array.from(mainElement.querySelectorAll<HTMLElement>(navigator.selector));
  const opposite: Route = route === 'next' ? 'prev' : 'next';
  const current = containers();

  if (!current.length) return null;

  if (typeof current[0].animate !== 'function') {
    const { track, seek, settle } = scrub(self, [], 0, (toEnd) => {
      if (!toEnd) return;
      navigator.shift(route);
      navigator.render(target);
      visibilityTitle(self);
      visibilityArrows(self);
    });
    return { distance: current[0].offsetWidth, from: 0, track, seek, settle };
  }

  cleanupPending(mainElement);

  navigator.shift(route);
  navigator.render(target);
  const staged = containers().map((el) => {
    el.parentElement?.setAttribute('data-vc-clip', '');
    return createGhost(el);
  });
  navigator.shift(opposite);
  navigator.render(target);

  const away = route === 'next' ? 100 : -100;
  const timing = { ...getTiming(self, slideEffect), fill: 'both' as const };

  const layers: Layer[] = containers().map((el, index) => {
    const ghost = staged[index];
    el.dataset.vcAnimating = '';
    el.parentElement?.setAttribute('data-vc-clip', '');
    el.parentElement?.appendChild(ghost);

    return {
      el,
      ghost,
      animations: [
        el.animate([{ transform: 'none' }, { transform: `translateX(${-away}%)` }], timing),
        ghost.animate([{ transform: `translateX(${away}%)` }, { transform: 'none' }], timing),
      ],
    };
  });

  if (!layers.length) return null;

  const animations = layers.flatMap((layer) => layer.animations);

  const drop = () => {
    animations.forEach((animation) => animation.cancel());
    dropLayers(layers);
  };

  // A queued finish must not touch layers already replaced by another transition.
  const isLive = () => layers[0].ghost.isConnected;

  const commit = () => {
    if (!isLive()) return;
    navigator.shift(route);
    navigator.render(target);
    drop();
    visibilityTitle(self);
    visibilityArrows(self);
  };

  const abort = () => drop();

  const { track, seek, settle } = scrub(self, animations, timing.duration, (toEnd) => (toEnd ? commit() : abort()));
  seek(0);

  return { distance: layers[0].el.offsetWidth, from: 0, track, seek, settle };
};

export default buildSwipe;

```

### `package/src/scripts/handles/handleGestures/transition.ts`

```ts
import { isEnabled } from '@scripts/utils/animate';
import type { Calendar } from '@src/index';

export type Transition = {
  distance: number;
  from: number;
  track: () => void;
  seek: (progress: number) => void;
  settle: (toEnd: boolean) => void;
};

export const clamp = (value: number) => Math.min(Math.max(value, 0), 1);

const MIN_SETTLE_DURATION_RATIO = 0.8;
const KEYFRAME_META = new Set(['offset', 'computedOffset', 'easing', 'composite']);

const cssName = (property: string) => property.replace(/[A-Z]/g, (letter) => `-${letter.toLowerCase()}`);

const getSettleFrames = (animation: Animation, toEnd: boolean) => {
  const effect = animation.effect as KeyframeEffect | null;
  const target = effect?.target;
  if (!effect || !(target instanceof Element)) return null;

  const keyframes = effect.getKeyframes();
  const endpoint = keyframes[toEnd ? keyframes.length - 1 : 0];
  if (!endpoint) return null;

  const computed = getComputedStyle(target);
  const current: Keyframe = {};
  const end: Keyframe = {};

  Object.entries(endpoint).forEach(([property, value]) => {
    if (KEYFRAME_META.has(property)) return;
    current[property] = computed.getPropertyValue(cssName(property));
    end[property] = value;
  });

  return { effect, keyframes: [current, end] };
};

export const scrub = (self: Calendar, animations: Animation[], duration: number, finish: (toEnd: boolean) => void) => {
  animations.forEach((animation) => animation.pause());
  const easing = animations[0]?.effect?.getTiming().easing ?? 'linear';
  let tracked = false;

  // Finish events can race with a manual settle.
  let settled = false;
  const done = (toEnd: boolean) => {
    if (settled) return;
    settled = true;
    finish(toEnd);
  };

  const track = () => {
    tracked = true;
    animations.forEach((animation) => animation.effect?.updateTiming({ easing: 'linear' }));
  };

  const seek = (progress: number) => {
    const time = clamp(progress) * duration;
    animations.forEach((animation) => {
      animation.currentTime = time;
    });
  };

  const settle = (toEnd: boolean) => {
    if (settled) return;
    if (!animations.length || !isEnabled(self) || animations[0].currentTime === (toEnd ? duration : 0)) return done(toEnd);

    if (tracked) {
      const progress = clamp(Number(animations[0].currentTime) / duration);
      const remaining = Math.abs(Number(toEnd) - progress);
      const settleDuration = duration * Math.max(remaining, MIN_SETTLE_DURATION_RATIO);
      // Start from computed pixels so restoring easing cannot move the content on release.
      const frames = animations.map((animation) => getSettleFrames(animation, toEnd));
      if (frames.every((frame) => frame !== null)) {
        frames.forEach((frame, index) => {
          if (!frame) return;
          const animation = animations[index];
          frame.effect.setKeyframes(frame.keyframes);
          animation.effect?.updateTiming({ duration: settleDuration, easing });
          animation.currentTime = 0;
          animation.playbackRate = 1;
          animation.play();
        });
        animations[0].onfinish = () => done(toEnd);
        return;
      }
    }

    animations.forEach((animation) => {
      animation.playbackRate = toEnd ? 1 : -1;
      animation.play();
    });
    animations[0].onfinish = () => done(toEnd);
  };

  return { track, seek, settle };
};

```

### `package/src/scripts/handles/handleInput.ts`

```ts
import createToInput from '@scripts/creators/createToInput';
import { show } from '@scripts/methods';
import canOpenOnFocus from '@scripts/utils/canOpenOnFocus';
import getRootNode from '@scripts/utils/getRootNode';
import setContext from '@scripts/utils/setContext';
import { clearSkipOpenOnFocus, shouldSkipOpenOnFocus } from '@scripts/utils/skipOpenOnFocus';
import type { Calendar } from '@src/index';

const handleInput = (self: Calendar) => {
  setContext(self, 'inputElement', self.context.mainElement as HTMLInputElement);
  const inputElement = self.context.inputElement as HTMLInputElement;
  // Announce that the field opens a picker. Only a form control has a role that carries it:
  // inputMode also accepts a plain element, which has none.
  if (['input', 'button', 'textarea'].includes(inputElement.localName)) {
    inputElement.setAttribute('aria-haspopup', 'dialog');
    if (inputElement.localName === 'button' || inputElement.getAttribute('role') === 'combobox') {
      inputElement.setAttribute('aria-expanded', 'false');
    }
  }

  const handleOpenCalendar = () => {
    if (self.context.inputModeInit) {
      setTimeout(() => show(self));
      return;
    }
    createToInput(self);
  };

  (self.context.inputElement as HTMLInputElement).addEventListener('click', handleOpenCalendar);

  const shouldHandleFocus = typeof self.openOnFocus === 'function' || self.openOnFocus === true;

  const handleOpenOnFocus = () => {
    if (shouldSkipOpenOnFocus(self)) {
      clearSkipOpenOnFocus(self);
      return;
    }
    if (!canOpenOnFocus(self)) return;
    handleOpenCalendar();
  };

  if (shouldHandleFocus) {
    (self.context.inputElement as HTMLInputElement).addEventListener('focus', handleOpenOnFocus);
  }

  const focusIntoCalendar = (event: KeyboardEvent) => {
    if (!self.context.isShowInInputMode) return false;
    if (getRootNode(self.context.mainElement).activeElement !== self.context.inputElement) return false;

    const isFocusable = (el: HTMLElement) => el.tabIndex >= 0 && !el.hasAttribute('disabled') && el.getAttribute('aria-disabled') !== 'true';

    const walker = document.createTreeWalker(self.context.mainElement, NodeFilter.SHOW_ELEMENT, {
      acceptNode: (node) => {
        const el = node as HTMLElement;
        if (!isFocusable(el)) return NodeFilter.FILTER_SKIP;
        return NodeFilter.FILTER_ACCEPT;
      },
    });

    const focusTarget = (walker.nextNode() as HTMLElement | null) ?? (isFocusable(self.context.mainElement) ? self.context.mainElement : null);

    if (!focusTarget || focusTarget.tabIndex < 0) return false;

    event.preventDefault();
    focusTarget.focus();
    return true;
  };

  const handleKeyIntoCalendar = (event: KeyboardEvent) => {
    const isTab = event.key === 'Tab' && !event.shiftKey;
    const isArrow = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'].includes(event.key);
    if (!isTab && !isArrow) return;
    focusIntoCalendar(event);
  };

  (self.context.inputElement as HTMLInputElement).addEventListener('keydown', handleKeyIntoCalendar);

  return () => {
    (self.context.inputElement as HTMLInputElement).removeEventListener('click', handleOpenCalendar);

    if (shouldHandleFocus) {
      (self.context.inputElement as HTMLInputElement).removeEventListener('focus', handleOpenOnFocus);
    }

    (self.context.inputElement as HTMLInputElement).removeEventListener('keydown', handleKeyIntoCalendar);
  };
};

export default handleInput;

```

### `package/src/scripts/handles/handleNavigate.ts`

```ts
import createDates from '@scripts/creators/createDates/createDates';
import createYears from '@scripts/creators/createYears';
import visibilityArrows from '@scripts/creators/visibilityArrows';
import visibilityTitle from '@scripts/creators/visibilityTitle';
import animate from '@scripts/utils/animate';
import getDate from '@scripts/utils/getDate';
import getDateString from '@scripts/utils/getDateString';
import getRootNode from '@scripts/utils/getRootNode';
import setContext from '@scripts/utils/setContext';
import setWeekDate from '@scripts/utils/setWeekDate';
import type { Calendar, Range } from '@src/index';

export type Route = 'prev' | 'next';

type Navigator = {
  selector: string;
  shift: (route: Route) => void;
  render: (target?: HTMLElement) => void;
};

const DATES = '[data-vc="dates"]';

const step = (route: Route, amount: number) => (route === 'next' ? amount : -amount);

const shiftMonth = (self: Calendar, route: Route) => {
  const jumpDate = getDate(getDateString(new Date(self.context.selectedYear, self.context.selectedMonth, 1)));
  jumpDate.setMonth(jumpDate.getMonth() + step(route, self.monthsToSwitch));
  setContext(self, 'selectedMonth', jumpDate.getMonth() as Range<12>);
  setContext(self, 'selectedYear', jumpDate.getFullYear());
};

const shiftWeek = (self: Calendar, route: Route) => {
  const weekStart = getDate(self.context.displayWeekDate);
  weekStart.setDate(weekStart.getDate() + step(route, 7));
  setWeekDate(self, weekStart);
};

export const getNavigator = (self: Calendar): Navigator | null => {
  const byMonth = { selector: DATES, shift: (route: Route) => shiftMonth(self, route), render: () => createDates(self) };

  return (
    {
      default: byMonth,
      multiple: byMonth,
      week: { selector: DATES, shift: (route: Route) => shiftWeek(self, route), render: () => createDates(self) },
      year: {
        selector: '[data-vc="years"]',
        shift: (route: Route) => setContext(self, 'displayYear', self.context.displayYear + step(route, 15)),
        render: (target?: HTMLElement) => createYears(self, target),
      },
      month: null,
    } satisfies Record<Calendar['type'], Navigator | null>
  )[self.context.currentType];
};

// The year list re-renders the whole layout, arrows included, so whatever was focused can be gone
// by the time it settles. Hand the focus back rather than let it drop to the document.
const keepFocusInside = (self: Calendar, route: Route, hadFocus: boolean) => {
  const { mainElement } = self.context;
  if (!hadFocus || mainElement.contains(getRootNode(mainElement).activeElement)) return;

  const arrowEl = mainElement.querySelector<HTMLElement>(`[data-vc-arrow="${route}"]`);
  if (arrowEl && arrowEl.style.visibility !== 'hidden') return arrowEl.focus();

  Array.from(mainElement.querySelectorAll<HTMLElement>('[tabindex="0"]'))
    .find((el) => !el.closest('[data-vc-ghost]'))
    ?.focus();
};

const handleNavigate = (self: Calendar, route: Route, target?: HTMLElement) => {
  const navigator = getNavigator(self);
  if (!navigator) return;

  const { mainElement } = self.context;
  const hadFocus = mainElement.contains(getRootNode(mainElement).activeElement);

  navigator.shift(route);
  visibilityTitle(self);
  visibilityArrows(self);
  animate(self, navigator.selector, route, () => navigator.render(target));
  keepFocusInside(self, route, hadFocus);
};

export default handleNavigate;

```

### `package/src/scripts/handles/handleSelectDate.ts`

```ts
import canToggleSelection from '@scripts/utils/canToggleSelection';
import setContext from '@scripts/utils/setContext';
import type { Calendar, FormatDateString } from '@src/index';

const handleSelectDate = (self: Calendar, dateEl: HTMLElement, multiple: boolean) => {
  const selectedDate = dateEl.dataset.vcDate as FormatDateString;
  const isSelected = dateEl.closest('[data-vc-date][data-vc-date-selected]');

  const isToggleAllowed = canToggleSelection(self);
  if (isSelected && !isToggleAllowed) return;

  const selectedDates = isSelected
    ? self.context.selectedDates.filter((date) => date !== selectedDate)
    : multiple
      ? [...self.context.selectedDates, selectedDate]
      : [selectedDate];
  setContext(self, 'selectedDates', selectedDates);
};

export default handleSelectDate;

```

### `package/src/scripts/handles/handleSelectDateRange/handleCancelSelectionDates.ts`

```ts
import createDateRangeTooltip from '@scripts/creators/createDates/createDateRangeTooltip';
import { optimizedHandleHoverDatesEvent } from '@scripts/handles/handleSelectDateRange/optimizedHandles';
import state from '@scripts/handles/handleSelectDateRange/state';
import { removeHoverEffect } from '@scripts/handles/handleSelectDateRange/toggleHoverEffect';
import setContext from '@scripts/utils/setContext';

const handleCancelSelectionDates = (e: KeyboardEvent) => {
  if (!state.self || e.key !== 'Escape') return;
  state.lastDateEl = null;
  setContext(state.self, 'selectedDates', []);
  state.self.context.mainElement!.removeEventListener('mousemove', optimizedHandleHoverDatesEvent);
  state.self.context.mainElement!.removeEventListener('keydown', handleCancelSelectionDates);
  createDateRangeTooltip(state.self, state.tooltipEl, null);
  removeHoverEffect();
};

export default handleCancelSelectionDates;

```

### `package/src/scripts/handles/handleSelectDateRange/handleHoverDatesEvent.ts`

```ts
import createDateRangeTooltip from '@scripts/creators/createDates/createDateRangeTooltip';
import state from '@scripts/handles/handleSelectDateRange/state';
import { addHoverEffect, removeHoverEffect } from '@scripts/handles/handleSelectDateRange/toggleHoverEffect';
import getDate from '@scripts/utils/getDate';
import type { FormatDateString } from '@src/index';

const isDragging = () => !!state.self?.context?.mainElement?.hasAttribute('data-vc-dragging');

const handleHoverDatesEvent = (target: HTMLElement | null) => {
  if (isDragging() || !target || !state.self?.context?.selectedDates[0]) return;

  if (!target.closest('[data-vc="dates"]')) {
    state.lastDateEl = null;
    createDateRangeTooltip(state.self, state.tooltipEl, null);
    removeHoverEffect();
    return;
  }

  const dateEl = target.closest<HTMLElement>('[data-vc-date]');
  if (!dateEl || state.lastDateEl === dateEl) return;

  state.lastDateEl = dateEl;
  createDateRangeTooltip(state.self, state.tooltipEl, dateEl);
  removeHoverEffect();

  const lastDateString = dateEl.dataset.vcDate as FormatDateString;
  const startDate = getDate(state.self.context.selectedDates[0]);
  const endDate = getDate(lastDateString);

  const firstDateEls = state.self.context.mainElement.querySelectorAll<HTMLElement>(`[data-vc-date="${state.self.context.selectedDates[0]}"]`);
  const lastDateEls = state.self.context.mainElement.querySelectorAll<HTMLElement>(`[data-vc-date="${lastDateString}"]`);

  const [firstDateElCorrect, lastDateElCorrect] = startDate < endDate ? [firstDateEls, lastDateEls] : [lastDateEls, firstDateEls];
  const [start, end] = startDate < endDate ? [startDate, endDate] : [endDate, startDate];

  for (let i = new Date(start); i <= end; i.setDate(i.getDate() + 1)) {
    addHoverEffect(i, firstDateElCorrect, lastDateElCorrect);
  }
};

export default handleHoverDatesEvent;

```

### `package/src/scripts/handles/handleSelectDateRange/handleHoverSelectedDatesRangeEvent.ts`

```ts
import createDateRangeTooltip from '@scripts/creators/createDates/createDateRangeTooltip';
import state from '@scripts/handles/handleSelectDateRange/state';

const isDragging = () => !!state.self?.context?.mainElement?.hasAttribute('data-vc-dragging');

const handleHoverSelectedDatesRangeEvent = (target: HTMLElement | null) => {
  if (isDragging()) return;
  const dateEl = target?.closest<HTMLElement>('[data-vc-date-selected]');

  if (!dateEl && state.lastDateEl) {
    state.lastDateEl = null;
    createDateRangeTooltip(state.self!, state.tooltipEl, null);
    return;
  }

  if (!dateEl || state.lastDateEl === dateEl) return;
  state.lastDateEl = dateEl;
  createDateRangeTooltip(state.self!, state.tooltipEl, dateEl);
};

export default handleHoverSelectedDatesRangeEvent;

```

### `package/src/scripts/handles/handleSelectDateRange/handleMouseLeave.ts`

```ts
import createDateRangeTooltip from '@scripts/creators/createDates/createDateRangeTooltip';
import state from '@scripts/handles/handleSelectDateRange/state';
import { removeHoverEffect } from '@scripts/handles/handleSelectDateRange/toggleHoverEffect';

const handleMouseLeave = () => {
  if (state.timeoutId !== null) clearTimeout(state.timeoutId);

  state.timeoutId = setTimeout(() => {
    state.lastDateEl = null;
    createDateRangeTooltip(state.self!, state.tooltipEl, null);
    removeHoverEffect();
  }, 50);
};

export default handleMouseLeave;

```

### `package/src/scripts/handles/handleSelectDateRange/handleSelectDateRange.ts`

```ts
import createDateRangeTooltip from '@scripts/creators/createDates/createDateRangeTooltip';
import handleCancelSelectionDates from '@scripts/handles/handleSelectDateRange/handleCancelSelectionDates';
import handleMouseLeave from '@scripts/handles/handleSelectDateRange/handleMouseLeave';
import { optimizedHandleHoverDatesEvent, optimizedHandleHoverSelectedDatesRangeEvent } from '@scripts/handles/handleSelectDateRange/optimizedHandles';
import state from '@scripts/handles/handleSelectDateRange/state';
import { removeHoverEffect } from '@scripts/handles/handleSelectDateRange/toggleHoverEffect';
import updateDisabledDates from '@scripts/handles/handleSelectDateRange/updateDisabledDates';
import canToggleSelection from '@scripts/utils/canToggleSelection';
import parseDates from '@scripts/utils/parseDates';
import setContext from '@scripts/utils/setContext';
import type { Calendar, FormatDateString } from '@src/index';

const handleSelectDateRange = (self: Calendar, dateEl: HTMLElement | null) => {
  state.self = self;
  state.lastDateEl = dateEl;

  removeHoverEffect();

  if (self.disableDatesGaps) {
    state.rangeMin = state.rangeMin ? state.rangeMin : self.context.displayDateMin;
    state.rangeMax = state.rangeMax ? state.rangeMax : self.context.displayDateMax;
  }

  if (!!self.onCreateDateRangeTooltip) {
    state.tooltipEl = self.context.mainElement.querySelector<HTMLElement>('[data-vc-date-range-tooltip]') as HTMLElement;
  }

  const formattedDate = dateEl?.dataset.vcDate as FormatDateString | undefined;
  if (formattedDate) {
    const selectedDateExists = self.context.selectedDates.length === 1 && self.context.selectedDates[0].includes(formattedDate);
    const selectedDates =
      selectedDateExists && !canToggleSelection(self)
        ? [formattedDate, formattedDate]
        : selectedDateExists && canToggleSelection(self)
          ? []
          : self.context.selectedDates.length > 1
            ? [formattedDate]
            : [...self.context.selectedDates, formattedDate];
    setContext(self, 'selectedDates', selectedDates);
    if (self.context.selectedDates.length > 1) self.context.selectedDates.sort((a, b) => +new Date(a) - +new Date(b));
  }

  const selectionHandlers = {
    set: () => {
      if (self.disableDatesGaps) updateDisabledDates();
      createDateRangeTooltip(state.self!, state.tooltipEl, dateEl);

      state.self!.context.mainElement!.removeEventListener('mousemove', optimizedHandleHoverSelectedDatesRangeEvent);
      state.self!.context.mainElement!.removeEventListener('mouseleave', handleMouseLeave);
      state.self!.context.mainElement!.removeEventListener('keydown', handleCancelSelectionDates);

      state.self!.context.mainElement!.addEventListener('mousemove', optimizedHandleHoverDatesEvent);
      state.self!.context.mainElement!.addEventListener('mouseleave', handleMouseLeave);
      state.self!.context.mainElement!.addEventListener('keydown', handleCancelSelectionDates);

      return () => {
        state.self!.context.mainElement!.removeEventListener('mousemove', optimizedHandleHoverDatesEvent);
        state.self!.context.mainElement!.removeEventListener('mouseleave', handleMouseLeave);
        state.self!.context.mainElement!.removeEventListener('keydown', handleCancelSelectionDates);
      };
    },
    reset: () => {
      const [startDate, endDate] = [self.context.selectedDates[0], self.context.selectedDates[self.context.selectedDates.length - 1]];
      const notSameDate = self.context.selectedDates[0] !== self.context.selectedDates[self.context.selectedDates.length - 1];
      const allDates = parseDates([`${startDate as string}:${endDate as string}`]);
      const actualDates = allDates.filter((d) => !self.context.disableDates.includes(d));

      const selectedDates = notSameDate
        ? self.enableEdgeDatesOnly
          ? [startDate, endDate]
          : actualDates
        : [self.context.selectedDates[0], self.context.selectedDates[0]];
      setContext(self, 'selectedDates', selectedDates);

      if (self.disableDatesGaps) {
        setContext(self, 'displayDateMin', state.rangeMin as FormatDateString);
        setContext(self, 'displayDateMax', state.rangeMax as FormatDateString);
      }

      state.self!.context.mainElement!.removeEventListener('mousemove', optimizedHandleHoverDatesEvent);
      state.self!.context.mainElement!.removeEventListener('mouseleave', handleMouseLeave);
      state.self!.context.mainElement!.removeEventListener('keydown', handleCancelSelectionDates);

      if (!self.onCreateDateRangeTooltip) return;
      if (!self.context.selectedDates[0]) {
        state.self!.context.mainElement!.removeEventListener('mousemove', optimizedHandleHoverSelectedDatesRangeEvent);
        state.self!.context.mainElement!.removeEventListener('mouseleave', handleMouseLeave);
        createDateRangeTooltip(state.self!, state.tooltipEl, null);
      }
      if (self.context.selectedDates[0]) {
        state.self!.context.mainElement!.addEventListener('mousemove', optimizedHandleHoverSelectedDatesRangeEvent);
        state.self!.context.mainElement!.addEventListener('mouseleave', handleMouseLeave);
        createDateRangeTooltip(state.self!, state.tooltipEl, dateEl);
      }

      return () => {
        state.self!.context.mainElement!.removeEventListener('mousemove', optimizedHandleHoverSelectedDatesRangeEvent);
        state.self!.context.mainElement!.removeEventListener('mouseleave', handleMouseLeave);
      };
    },
  };
  selectionHandlers[self.context.selectedDates.length === 1 ? 'set' : 'reset']();
};

export default handleSelectDateRange;

```

### `package/src/scripts/handles/handleSelectDateRange/optimizedHandles.ts`

```ts
import handleHoverDatesEvent from '@scripts/handles/handleSelectDateRange/handleHoverDatesEvent';
import handleHoverSelectedDatesRangeEvent from '@scripts/handles/handleSelectDateRange/handleHoverSelectedDatesRangeEvent';
import state from '@scripts/handles/handleSelectDateRange/state';

const optimizedHoverHandler = (callback: (target: HTMLElement | null) => void) => {
  return (e: MouseEvent) => {
    const closuredTarget = e.target as HTMLElement;
    if (!state.isHovering) {
      state.isHovering = true;
      requestAnimationFrame(() => {
        callback(closuredTarget);
        state.isHovering = false;
      });
    }
  };
};

export const optimizedHandleHoverDatesEvent = optimizedHoverHandler(handleHoverDatesEvent);

export const optimizedHandleHoverSelectedDatesRangeEvent = optimizedHoverHandler(handleHoverSelectedDatesRangeEvent);

```

### `package/src/scripts/handles/handleSelectDateRange/state.ts`

```ts
import type { Calendar, FormatDateString } from '@src/index';

const state: {
  self: Calendar | null;
  lastDateEl: HTMLElement | null;
  isHovering: boolean;
  rangeMin: FormatDateString | undefined;
  rangeMax: FormatDateString | undefined;
  tooltipEl: HTMLElement | null;
  timeoutId: NodeJS.Timeout | null;
} = {
  self: null,
  lastDateEl: null,
  isHovering: false,
  rangeMin: undefined,
  rangeMax: undefined,
  tooltipEl: null,
  timeoutId: null,
};

export default state;

```

### `package/src/scripts/handles/handleSelectDateRange/toggleHoverEffect.ts`

```ts
import state from '@scripts/handles/handleSelectDateRange/state';
import getDateString from '@scripts/utils/getDateString';

export const addHoverEffect = (date: Date, firstDateEls: NodeListOf<HTMLElement>, lastDateEls: NodeListOf<HTMLElement>) => {
  if (!state.self?.context?.selectedDates[0]) return;

  const formattedDate = getDateString(date);
  if (state.self.context.disableDates?.includes(formattedDate)) return;

  state.self.context.mainElement.querySelectorAll<HTMLElement>(`[data-vc-date="${formattedDate}"]`).forEach((d) => (d.dataset.vcDateHover = ''));
  firstDateEls.forEach((d) => (d.dataset.vcDateHover = 'first'));
  lastDateEls.forEach((d) => {
    if (d.dataset.vcDateHover === 'first') {
      d.dataset.vcDateHover = 'first-and-last';
    } else {
      d.dataset.vcDateHover = 'last';
    }
  });
};

export const removeHoverEffect = () => {
  if (!state.self?.context?.mainElement) return;
  const dateEls = state.self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc-date-hover]');
  dateEls.forEach((d) => d.removeAttribute('data-vc-date-hover'));
};

```

### `package/src/scripts/handles/handleSelectDateRange/updateDisabledDates.ts`

```ts
import state from '@scripts/handles/handleSelectDateRange/state';
import getDate from '@scripts/utils/getDate';
import getDateString from '@scripts/utils/getDateString';
import setContext from '@scripts/utils/setContext';

const updateDisabledDates = () => {
  if (!state.self?.context?.selectedDates?.[0] || !state.self.context.disableDates?.[0]) return;
  const selectedDate = getDate(state.self.context.selectedDates[0]);

  const [startDate, endDate] = state.self.context.disableDates
    .map((dateStr) => getDate(dateStr))
    .reduce<
      [Date | null, Date | null]
    >(([start, end], disabledDate) => [selectedDate >= disabledDate ? disabledDate : start, selectedDate < disabledDate && end === null ? disabledDate : end], [null, null]);

  if (startDate) setContext(state.self, 'displayDateMin', getDateString(new Date(startDate.setDate(startDate.getDate() + 1))));
  if (endDate) setContext(state.self, 'displayDateMax', getDateString(new Date(endDate.setDate(endDate.getDate() - 1))));

  const isDisablePast =
    state.self.disableDatesPast && !state.self.disableAllDates && getDate(state.self.context.displayDateMin) < getDate(state.self.context.dateToday);
  if (isDisablePast) setContext(state.self, 'displayDateMin', state.self.context.dateToday);
};

export default updateDisabledDates;

```

### `package/src/scripts/handles/handleTheme.ts`

```ts
import getRootNode from '@scripts/utils/getRootNode';
import observeHtmlElement from '@scripts/utils/observeHtmlElement';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const haveListener = {
  value: false,
  set: () => (haveListener.value = true),
  check: () => haveListener.value,
};

const setTheme = (htmlEl: HTMLElement, theme: Calendar['selectedTheme']) => (htmlEl.dataset.vcTheme = theme);

const addMediaQueryListener = (mediaQuery: MediaQueryList, listener: (event: MediaQueryList | MediaQueryListEvent) => void) => {
  if (mediaQuery.addEventListener) {
    mediaQuery.addEventListener('change', listener);
    return () => mediaQuery.removeEventListener('change', listener);
  }
  mediaQuery.addListener(listener);
  return () => mediaQuery.removeListener(listener);
};

const trackChangesThemeInSystemSettings = (self: Calendar, supportDarkTheme: MediaQueryList) => {
  setTheme(self.context.mainElement, supportDarkTheme.matches ? 'dark' : 'light');

  if (self.selectedTheme !== 'system' || self.context.cleanupSystemTheme) return;

  // document.querySelectorAll below can't reach into a Shadow DOM, so an instance rendered
  // inside one can't rely on the shared, page-wide broadcast listener - give it its own
  // listener instead, scoped to just this instance.
  if (getRootNode(self.context.mainElement) !== document) {
    const updateThisInstance = (event: MediaQueryList | MediaQueryListEvent) => setTheme(self.context.mainElement, event.matches ? 'dark' : 'light');
    setContext(self, 'cleanupSystemTheme', addMediaQueryListener(supportDarkTheme, updateThisInstance));
    return;
  }

  if (haveListener.check()) return;

  const changeDataAttrTheme = (event: MediaQueryList | MediaQueryListEvent) => {
    const calendarEls = document.querySelectorAll('[data-vc="calendar"]');
    calendarEls?.forEach((calendarEl) => setTheme(calendarEl as HTMLElement, event.matches ? 'dark' : 'light'));
  };

  addMediaQueryListener(supportDarkTheme, changeDataAttrTheme);
  haveListener.set();
};

const detectTheme = (self: Calendar, supportDarkTheme: MediaQueryList) => {
  const detectedThemeEl: HTMLElement | null = self.themeAttrDetect.length ? document.querySelector(self.themeAttrDetect) : null;
  const attr = (self.themeAttrDetect as string).replace(/^.*\[(.+)\]/g, (_, p1) => p1);

  if (!detectedThemeEl || detectedThemeEl.getAttribute(attr) === 'system') {
    trackChangesThemeInSystemSettings(self, supportDarkTheme);
    return;
  }

  const activeTheme = detectedThemeEl.getAttribute(attr);
  if (activeTheme) {
    setTheme(self.context.mainElement, activeTheme);
    observeHtmlElement(detectedThemeEl, attr, () => {
      const activeTheme = detectedThemeEl.getAttribute(attr);
      if (activeTheme) setTheme(self.context.mainElement, activeTheme);
    });
  } else {
    trackChangesThemeInSystemSettings(self, supportDarkTheme);
  }
};

const handleTheme = (self: Calendar) => {
  if (!(window.matchMedia('(prefers-color-scheme)').media !== 'not all')) {
    setTheme(self.context.mainElement, 'light');
    return;
  }

  if (self.selectedTheme === 'system') {
    detectTheme(self, window.matchMedia('(prefers-color-scheme: dark)'));
  } else {
    setTheme(self.context.mainElement, self.selectedTheme);
  }
};

export default handleTheme;

```

### `package/src/scripts/handles/handleTime/handleActions.ts`

```ts
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const handleActions = (self: Calendar, event: Event, value: string, type: 'hour' | 'minute') => {
  const typeMap = {
    hour: () => setContext(self, 'selectedHours', value),
    minute: () => setContext(self, 'selectedMinutes', value),
  };
  typeMap[type]();

  setContext(
    self,
    'selectedTime',
    `${self.context.selectedHours}:${self.context.selectedMinutes}${self.context.selectedKeeping ? ` ${self.context.selectedKeeping}` : ''}`,
  );

  if (self.onChangeTime) self.onChangeTime(self, event, false);
  if (self.inputMode && self.context.inputElement && self.context.mainElement && self.onChangeToInput) self.onChangeToInput(self, event);
};

export default handleActions;

```

### `package/src/scripts/handles/handleTime/handleClickKeepingTime.ts`

```ts
import handleActions from '@scripts/handles/handleTime/handleActions';
import setContext from '@scripts/utils/setContext';
import transformTime24 from '@scripts/utils/transformTime24';
import type { Calendar } from '@src/index';

const handleClickKeepingTime = (self: Calendar, keepingTimeEl: HTMLButtonElement, rangeHourEl: HTMLInputElement, max: number, min: number) => {
  const handleClickKeepingTimeAction = (event: Event) => {
    const newSelectedKeeping = self.context.selectedKeeping === 'AM' ? 'PM' : 'AM';
    const hour = transformTime24(self.context.selectedHours, newSelectedKeeping);

    if (!(Number(hour) <= max && Number(hour) >= min)) {
      if (self.onChangeTime) self.onChangeTime(self, event, true);
      return;
    }

    setContext(self, 'selectedKeeping', newSelectedKeeping);
    rangeHourEl.value = hour;

    handleActions(self, event, self.context.selectedHours, 'hour');

    keepingTimeEl.ariaLabel = `${self.labels.btnKeeping} ${self.context.selectedKeeping}`;
    keepingTimeEl.innerText = self.context.selectedKeeping as string;
  };

  keepingTimeEl.addEventListener('click', handleClickKeepingTimeAction);

  return () => {
    keepingTimeEl.removeEventListener('click', handleClickKeepingTimeAction);
  };
};

export default handleClickKeepingTime;

```

### `package/src/scripts/handles/handleTime/handleInput.ts`

```ts
import handleActions from '@scripts/handles/handleTime/handleActions';
import setContext from '@scripts/utils/setContext';
import transformTime12 from '@scripts/utils/transformTime12';
import transformTime24 from '@scripts/utils/transformTime24';
import type { Calendar, ContextVariables } from '@src/index';

const updateInputAndRange = (inputEl: HTMLInputElement, rangeEl: HTMLInputElement, valueInput: string, valueRange: string) => {
  inputEl.value = valueInput;
  rangeEl.value = valueRange;
};

const updateKeepingTime = (self: Calendar, keepingTimeEl: HTMLButtonElement | null, keeping: ContextVariables['selectedKeeping']) => {
  if (!keepingTimeEl || !keeping) return;
  setContext(self, 'selectedKeeping', keeping);
  keepingTimeEl.innerText = keeping;
};

const handleInput = (
  self: Calendar,
  rangeEl: HTMLInputElement,
  inputEl: HTMLInputElement,
  keepingTimeEl: HTMLButtonElement | null,
  type: 'hour' | 'minute',
  max: number,
  min: number,
) => {
  const handlers = {
    hour: (value: number, valueStr: string, event: Event) => {
      if (!self.selectionTimeMode) return;

      const timeMap = {
        12: () => {
          if (!self.context.selectedKeeping) return;
          const correctValue = Number(transformTime24(valueStr, self.context.selectedKeeping));
          if (!(correctValue <= max && correctValue >= min)) {
            updateInputAndRange(inputEl, rangeEl, self.context.selectedHours, self.context.selectedHours);
            if (self.onChangeTime) self.onChangeTime(self, event, true);
            return;
          }

          updateInputAndRange(inputEl, rangeEl, transformTime12(valueStr), transformTime24(valueStr, self.context.selectedKeeping));
          if (value > 12) updateKeepingTime(self, keepingTimeEl, 'PM');
          handleActions(self, event, transformTime12(valueStr), type);
        },
        24: () => {
          if (!(value <= max && value >= min)) {
            updateInputAndRange(inputEl, rangeEl, self.context.selectedHours, self.context.selectedHours);
            if (self.onChangeTime) self.onChangeTime(self, event, true);
            return;
          }

          updateInputAndRange(inputEl, rangeEl, valueStr, valueStr);
          handleActions(self, event, valueStr, type);
        },
      };
      timeMap[self.selectionTimeMode]();
    },
    minute: (value: number, valueStr: string, event: Event) => {
      if (!(value <= max && value >= min)) {
        inputEl.value = self.context.selectedMinutes;
        if (self.onChangeTime) self.onChangeTime(self, event, true);
        return;
      }

      inputEl.value = valueStr;
      rangeEl.value = valueStr;
      handleActions(self, event, valueStr, type);
    },
  };

  const handleInputAction = (event: Event) => {
    const value = Number(inputEl.value);
    const valueStr = inputEl.value.padStart(2, '0');
    if (handlers[type]) handlers[type](value, valueStr, event);
  };

  inputEl.addEventListener('change', handleInputAction);

  return () => {
    inputEl.removeEventListener('change', handleInputAction);
  };
};

export default handleInput;

```

### `package/src/scripts/handles/handleTime/handleRange.ts`

```ts
import handleActions from '@scripts/handles/handleTime/handleActions';
import setContext from '@scripts/utils/setContext';
import transformTime12 from '@scripts/utils/transformTime12';
import type { Calendar } from '@src/index';

const updateInputAndTime = (self: Calendar, inputEl: HTMLInputElement, event: Event, type: 'hour' | 'minute', value: string) => {
  inputEl.value = value;
  handleActions(self, event, value, type);
};

const updateKeepingTime = (self: Calendar, keepingTimeEl: HTMLButtonElement | null, keeping: 'AM' | 'PM') => {
  if (!keepingTimeEl) return;
  setContext(self, 'selectedKeeping', keeping);
  keepingTimeEl.innerText = keeping;
};

const handleRange = (
  self: Calendar,
  rangeEl: HTMLInputElement,
  inputEl: HTMLInputElement,
  keepingTimeEl: HTMLButtonElement | null,
  type: 'hour' | 'minute',
) => {
  const handleRangeAction = (event: Event) => {
    const value = Number(rangeEl.value);
    const valueStr = rangeEl.value.padStart(2, '0');

    const isHourType = type === 'hour';
    const isFormat24 = self.selectionTimeMode === 24;
    const isAM = value > 0 && value < 12;

    if (isHourType && !isFormat24) updateKeepingTime(self, keepingTimeEl, value === 0 || isAM ? 'AM' : 'PM');
    updateInputAndTime(self, inputEl, event, type, isHourType && !isFormat24 && !isAM ? transformTime12(rangeEl.value) : valueStr);
  };

  rangeEl.addEventListener('input', handleRangeAction);

  return () => {
    rangeEl.removeEventListener('input', handleRangeAction);
  };
};

export default handleRange;

```

### `package/src/scripts/handles/handleTime/handleTime.ts`

```ts
import handleClickKeepingTime from '@scripts/handles/handleTime/handleClickKeepingTime';
import handleInput from '@scripts/handles/handleTime/handleInput';
import handleRange from '@scripts/handles/handleTime/handleRange';
import type { Calendar } from '@src/index';

const handleMouseOver = (inputEl: HTMLInputElement) => inputEl.setAttribute('data-vc-input-focus', '');

const handleMouseOut = (inputEl: HTMLInputElement) => inputEl.removeAttribute('data-vc-input-focus');

const handleTime = (self: Calendar, timeEl: HTMLElement) => {
  const rangeHourEl = timeEl.querySelector<HTMLInputElement>('[data-vc-time-range="hour"] input');
  const rangeMinuteEl = timeEl.querySelector<HTMLInputElement>('[data-vc-time-range="minute"] input');
  const inputHourEl = timeEl.querySelector<HTMLInputElement>('[data-vc-time-input="hour"] input[name="hour"]');
  const inputMinuteEl = timeEl.querySelector<HTMLInputElement>('[data-vc-time-input="minute"] input[name="minute"]');
  const keepingTimeEl = timeEl.querySelector<HTMLButtonElement>('[data-vc-time="keeping"]');

  if (!rangeHourEl || !rangeMinuteEl || !inputHourEl || !inputMinuteEl) return;

  const handleMouseOverEvent = (event: MouseEvent) => {
    if (event.target === rangeHourEl) handleMouseOver(inputHourEl);
    if (event.target === rangeMinuteEl) handleMouseOver(inputMinuteEl);
  };

  const handleMouseOutEvent = (event: MouseEvent) => {
    if (event.target === rangeHourEl) handleMouseOut(inputHourEl);
    if (event.target === rangeMinuteEl) handleMouseOut(inputMinuteEl);
  };

  timeEl.addEventListener('mouseover', handleMouseOverEvent);
  timeEl.addEventListener('mouseout', handleMouseOutEvent);

  handleInput(self, rangeHourEl, inputHourEl, keepingTimeEl, 'hour', self.timeMaxHour, self.timeMinHour);
  handleInput(self, rangeMinuteEl, inputMinuteEl, keepingTimeEl, 'minute', self.timeMaxMinute, self.timeMinMinute);

  handleRange(self, rangeHourEl, inputHourEl, keepingTimeEl, 'hour');
  handleRange(self, rangeMinuteEl, inputMinuteEl, keepingTimeEl, 'minute');

  if (keepingTimeEl) handleClickKeepingTime(self, keepingTimeEl, rangeHourEl, self.timeMaxHour, self.timeMinHour);

  return () => {
    timeEl.removeEventListener('mouseover', handleMouseOverEvent);
    timeEl.removeEventListener('mouseout', handleMouseOutEvent);
  };
};

export default handleTime;

```

### `package/src/scripts/layouts/default.ts`

```ts
import type { Calendar } from '@src/index';

const layoutDefault = (self: Calendar) => `
  <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
    <#ArrowPrev [month] />
    <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
      <#Month />
      <#Year />
    </div>
    <#ArrowNext [month] />
  </div>
  <div class="${self.styles.wrapper}" data-vc="wrapper">
    <#WeekNumbers />
    <div class="${self.styles.content}" data-vc="content" role="grid">
      <#Week />
      <#Dates />
      <#DateRangeTooltip />
    </div>
  </div>
  <#Collapse />
  <#ControlTime />
`;

export default layoutDefault;

```

### `package/src/scripts/layouts/month.ts`

```ts
import type { Calendar } from '@src/index';

const layoutMonths = (self: Calendar) => `
  <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
    <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
      <#Month />
      <#Year />
    </div>
  </div>
  <div class="${self.styles.wrapper}" data-vc="wrapper">
    <div class="${self.styles.content}" data-vc="content">
      <#Months />
    </div>
  </div>
`;
export default layoutMonths;

```

### `package/src/scripts/layouts/multiple.ts`

```ts
import type { Calendar } from '@src/index';

const layoutMultiple = (self: Calendar) => `
  <div class="${self.styles.controls}" data-vc="controls" role="group" aria-label="${self.labels.navigation}">
    <#ArrowPrev [month] />
    <#ArrowNext [month] />
  </div>
  <div class="${self.styles.grid}" data-vc="grid">
    <#Multiple>
      <div class="${self.styles.column}" data-vc="column" role="group">
        <div class="${self.styles.header}" data-vc="header">
          <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
            <#Month />
            <#Year />
          </div>
        </div>
        <div class="${self.styles.wrapper}" data-vc="wrapper">
          <#WeekNumbers />
          <div class="${self.styles.content}" data-vc="content" role="grid">
            <#Week />
            <#Dates />
          </div>
        </div>
      </div>
    <#/Multiple>
    <#DateRangeTooltip />
  </div>
  <#ControlTime />
`;

export default layoutMultiple;

```

### `package/src/scripts/layouts/week.ts`

```ts
import type { Calendar } from '@src/index';

const layoutWeek = (self: Calendar) => `
  <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
    <#ArrowPrev [week] />
    <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
      <#Month />
      <#Year />
    </div>
    <#ArrowNext [week] />
  </div>
  <div class="${self.styles.wrapper}" data-vc="wrapper">
    <#WeekNumbers />
    <div class="${self.styles.content}" data-vc="content" role="grid">
      <#Week />
      <#Dates />
      <#DateRangeTooltip />
    </div>
  </div>
  <#Collapse />
  <#ControlTime />
`;

export default layoutWeek;

```

### `package/src/scripts/layouts/year.ts`

```ts
import type { Calendar } from '@src/index';

const layoutYears = (self: Calendar) => `
  <div class="${self.styles.header}" data-vc="header" role="group" aria-label="${self.labels.navigation}">
    <#ArrowPrev [year] />
    <div class="${self.styles.headerContent}" data-vc-header="content" aria-live="polite" aria-atomic="true">
      <#Month />
      <#Year />
    </div>
    <#ArrowNext [year] />
  </div>
  <div class="${self.styles.wrapper}" data-vc="wrapper">
    <div class="${self.styles.content}" data-vc="content">
      <#Years />
    </div>
  </div>
`;

export default layoutYears;

```

### `package/src/scripts/methods/destroy.ts`

```ts
import { cleanupGestures } from '@scripts/handles/handleGestures/handleGestures';
import { cleanupPending } from '@scripts/utils/animate';
import errorMessages from '@scripts/utils/getErrorMessages';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const destroy = (self: Calendar) => {
  if (!self.context.isInit) throw new Error(errorMessages.notInit);
  if (self.context.isDestroyed) throw new Error(errorMessages.alreadyDestroyed);

  cleanupGestures(self.context.mainElement);
  cleanupPending(self.context.mainElement);
  self.context.cleanupSystemTheme?.();

  if (self.inputMode) {
    if (self.context.mainElement !== self.context.inputElement) {
      self.context.mainElement.parentElement?.removeChild(self.context.mainElement);
    }
    self.context.inputElement?.replaceWith?.(self.context.originalElement);
    setContext(self, 'inputElement', undefined);
  } else {
    self.context.mainElement.replaceWith?.(self.context.originalElement);
  }

  setContext(self, 'mainElement', self.context.originalElement);
  setContext(self, 'isDestroyed', true);
  if (self.onDestroy) self.onDestroy(self);
};

export default destroy;

```

### `package/src/scripts/methods/hide.ts`

```ts
import getRootNode from '@scripts/utils/getRootNode';
import setContext from '@scripts/utils/setContext';
import { setSkipOpenOnFocus } from '@scripts/utils/skipOpenOnFocus';
import { hideFromAT } from '@scripts/utils/toggleTabbing';
import type { Calendar } from '@src/index';

const hide = (self: Calendar) => {
  if (!self.context.isShowInInputMode || !self.context.currentType) return;

  // `inert` blurs whatever it covers, so where the focus stands has to be read before it is set
  const hasFocusInside = self.context.mainElement.contains(getRootNode(self.context.mainElement).activeElement);

  self.context.mainElement.dataset.vcCalendarHidden = '';
  setContext(self, 'isShowInInputMode', false);
  if (self.inputMode) hideFromAT(self.context.mainElement);
  if (self.context.inputElement?.hasAttribute('aria-expanded')) self.context.inputElement.setAttribute('aria-expanded', 'false');

  if (self.context.cleanupHandlers[0]) {
    self.context.cleanupHandlers.forEach((cleanup) => cleanup());
    setContext(self, 'cleanupHandlers', []);
  }

  if (self.inputMode && self.context.inputElement && hasFocusInside) {
    const shouldHandleFocus = typeof self.openOnFocus === 'function' || self.openOnFocus === true;
    if (shouldHandleFocus) setSkipOpenOnFocus(self);
    self.context.inputElement.focus();
  }

  if (self.onHide) self.onHide(self);
};

export default hide;

```

### `package/src/scripts/methods/index.ts`

```ts
import destroy from '@scripts/methods/destroy';
import hide from '@scripts/methods/hide';
import init from '@scripts/methods/init';
import reset from '@scripts/methods/reset';
import set from '@scripts/methods/set';
import show from '@scripts/methods/show';
import update from '@scripts/methods/update';

export { init, update, reset, destroy, show, hide, set };

```

### `package/src/scripts/methods/init.ts`

```ts
import create from '@scripts/creators/create';
import updateDateModifiers from '@scripts/creators/createDates/updateDateModifiers';
import handleArrowKeys from '@scripts/handles/handleArrowKeys';
import handleClick from '@scripts/handles/handleClick/handleClick';
import handleGestures from '@scripts/handles/handleGestures/handleGestures';
import handleInput from '@scripts/handles/handleInput';
import handleSelectDateRange from '@scripts/handles/handleSelectDateRange/handleSelectDateRange';
import errorMessages from '@scripts/utils/getErrorMessages';
import initAllVariables from '@scripts/utils/initVariables/initAllVariables';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const init = (self: Calendar) => {
  if (self.context.isInit) throw new Error(errorMessages.alreadyInit);

  setContext(self, 'originalElement', self.context.mainElement.cloneNode(true) as HTMLElement);
  setContext(self, 'isInit', true);

  if (self.inputMode) return handleInput(self);

  initAllVariables(self);
  create(self);
  if (self.selectionDatesMode === 'multiple-ranged' && self.context.selectedDates.length === 1) {
    handleSelectDateRange(self, null);
    updateDateModifiers(self);
  }
  if (self.onInit) self.onInit(self);
  handleArrowKeys(self);
  // Gestures may be enabled later through set().
  handleGestures(self);
  return handleClick(self);
};

export default init;

```

### `package/src/scripts/methods/reset.ts`

```ts
import create from '@scripts/creators/create';
import handleDayRangedSelection from '@scripts/handles/handleSelectDateRange/handleSelectDateRange';
import { cleanupPending } from '@scripts/utils/animate';
import initAllVariables from '@scripts/utils/initVariables/initAllVariables';
import setContext from '@scripts/utils/setContext';
import type { Calendar, Reset } from '@src/index';

const reset = (self: Calendar, { year, month, dates, time, locale }: Reset, recreate = true) => {
  cleanupPending(self.context.mainElement);

  const previousSelected = {
    year: self.selectedYear,
    month: self.selectedMonth,
    dates: self.selectedDates,
    time: self.selectedTime,
  };

  self.selectedYear = year ? previousSelected.year : self.context.selectedYear;
  self.selectedMonth = month ? previousSelected.month : self.context.selectedMonth;
  self.selectedTime = time ? previousSelected.time : self.context.selectedTime;

  self.selectedDates =
    dates === 'only-first' && self.context.selectedDates?.[0]
      ? [self.context.selectedDates[0]]
      : dates === true
        ? previousSelected.dates
        : self.context.selectedDates;

  if (locale) {
    const locale = {
      months: { short: [], long: [] },
      weekdays: { short: [], long: [] },
    };
    setContext(self, 'locale', locale);
  }

  initAllVariables(self);
  if (recreate) create(self);

  self.selectedYear = previousSelected.year;
  self.selectedMonth = previousSelected.month;
  self.selectedDates = previousSelected.dates;
  self.selectedTime = previousSelected.time;
  if (self.selectionDatesMode === 'multiple-ranged' && dates) handleDayRangedSelection(self, null);
};

export default reset;

```

### `package/src/scripts/methods/set.ts`

```ts
import update from '@scripts/methods/update';
import replaceProperties from '@scripts/utils/replaceProperties';
import type { Calendar, Options, Reset } from '@src/index';

const set = (self: Calendar, options: Options, resetOptions?: Partial<Reset>) => {
  replaceProperties(self, options);
  if (self.context.isInit) update(self, resetOptions);
};

export default set;

```

### `package/src/scripts/methods/show.ts`

```ts
import hide from '@scripts/methods/hide';
import setPosition from '@scripts/utils/positions/setPosition';
import setContext from '@scripts/utils/setContext';
import { showToAT } from '@scripts/utils/toggleTabbing';
import type { Calendar } from '@src/index';

const show = (self: Calendar) => {
  if (self.context.isShowInInputMode) return;

  if (!self.context.currentType) {
    self.context.mainElement.click();
    return;
  }

  setContext(self, 'cleanupHandlers', []);
  setContext(self, 'isShowInInputMode', true);
  if (self.inputMode) showToAT(self.context.mainElement);
  setPosition(self.context.inputElement, self.context.mainElement, self.positionToInput);
  self.context.mainElement.removeAttribute('data-vc-calendar-hidden');
  if (self.context.inputElement?.hasAttribute('aria-expanded')) self.context.inputElement.setAttribute('aria-expanded', 'true');

  const handleResize = () => {
    setPosition(self.context.inputElement, self.context.mainElement, self.positionToInput);
  };
  window.addEventListener('resize', handleResize);
  self.context.cleanupHandlers.push(() => window.removeEventListener('resize', handleResize));

  const handleEscapeKey = (e: KeyboardEvent) => {
    if (e.key === 'Escape') hide(self);
  };
  document.addEventListener('keydown', handleEscapeKey);
  self.context.cleanupHandlers.push(() => document.removeEventListener('keydown', handleEscapeKey));

  const documentClickEvent = (e: MouseEvent) => {
    // use composedPath() rather than e.target: for a calendar rendered inside a Shadow DOM,
    // a document-level listener sees e.target retargeted to the shadow host, which would
    // never match inputElement/mainElement and incorrectly close the calendar on its own clicks
    const clickedEl = (e.composedPath()[0] ?? e.target) as HTMLElement;
    if (clickedEl === self.context.inputElement || self.context.mainElement.contains(clickedEl)) return;
    hide(self);
  };
  document.addEventListener('click', documentClickEvent, { capture: true });
  self.context.cleanupHandlers.push(() => document.removeEventListener('click', documentClickEvent, { capture: true }));

  if (self.onShow) self.onShow(self);
};

export default show;

```

### `package/src/scripts/methods/update.ts`

```ts
import reset from '@scripts/methods/reset';
import errorMessages from '@scripts/utils/getErrorMessages';
import type { Calendar, Reset } from '@src/index';

const update = (self: Calendar, resetOptions?: Partial<Reset>) => {
  if (!self.context.isInit) throw new Error(errorMessages.notInit);
  const defaultReset = { year: true, month: true, dates: true, time: true, locale: true };
  reset(self, { ...defaultReset, ...resetOptions }, !(self.inputMode && !self.context.inputModeInit));
  if (self.onUpdate) self.onUpdate(self);
};

export default update;

```

### `package/src/scripts/utils/animate.ts`

```ts
import type { Calendar } from '@src/index';

type AnimationEffect = 'prev' | 'next' | 'fade';

type Effect = {
  enter?: string;
  leave?: string;
  group: 'slide' | 'fade' | 'collapse';
  duration: number;
  easing: string;
};

const EASING = 'cubic-bezier(0.4, 0, 0.2, 1)';

export const slideEffect: Effect = { group: 'slide', duration: 250, easing: EASING };

const effects: Record<AnimationEffect, Effect> = {
  prev: { ...slideEffect, enter: 'translateX(-100%)', leave: 'translateX(100%)' },
  next: { ...slideEffect, enter: 'translateX(100%)', leave: 'translateX(-100%)' },
  fade: { group: 'fade', duration: 150, easing: EASING },
};

export const collapseEffect: Effect = { group: 'collapse', duration: 300, easing: EASING };

export const isEnabled = (self: Calendar) =>
  !!self.animation && typeof Element.prototype.animate === 'function' && !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export const getTiming = (self: Calendar, effect: Effect) => {
  const options = typeof self.animation === 'object' ? self.animation : {};
  const scoped = options[effect.group] ?? {};
  return {
    duration: scoped.duration ?? options.duration ?? effect.duration,
    easing: scoped.easing ?? options.easing ?? effect.easing,
  };
};

const LAYOUT_PROPS = [
  'display',
  'flexDirection',
  'gridTemplateColumns',
  'gridTemplateRows',
  'rowGap',
  'columnGap',
  'alignItems',
  'alignContent',
  'justifyItems',
  'justifyContent',
  'padding',
] as const;

const GRID_SELECTOR = '[data-vc="dates"], [data-vc="months"], [data-vc="years"]';

export const createGhost = (el: HTMLElement) => {
  const ghost = document.createElement('div');
  const computed = getComputedStyle(el);
  ghost.dataset.vcGhost = '';
  ghost.ariaHidden = 'true';
  ghost.setAttribute('inert', '');
  LAYOUT_PROPS.forEach((prop) => {
    ghost.style[prop] = computed[prop];
  });
  ghost.style.top = `${el.offsetTop}px`;
  ghost.style.left = `${el.offsetLeft}px`;
  ghost.style.width = `${el.offsetWidth}px`;
  ghost.style.height = `${el.offsetHeight}px`;
  // Root type changes can otherwise restyle the outgoing grid before it disappears.
  el.querySelectorAll<HTMLElement>(GRID_SELECTOR).forEach((grid) => {
    grid.style.height = `${grid.offsetHeight}px`;
    grid.style.flex = 'none';
  });
  ghost.append(...el.children);
  return ghost;
};

const stopAnimating = (el: HTMLElement) => {
  el.removeAttribute('data-vc-animating');
  el.removeAttribute('data-vc-collapsing');
  el.parentElement?.removeAttribute('data-vc-clip');
};

export const cleanupPending = (mainElement: HTMLElement) => {
  mainElement.querySelectorAll<HTMLElement>('[data-vc-ghost]').forEach((ghost) => {
    ghost.getAnimations().forEach((animation) => animation.cancel());
    ghost.remove();
  });
  mainElement.querySelectorAll<HTMLElement>('[data-vc-animating], [data-vc-collapsing]').forEach((el) => {
    el.getAnimations().forEach((animation) => animation.cancel());
    stopAnimating(el);
  });
};

// Freshly inserted grids cannot continue the CSS opacity transition from the old grid.
export const captureOpacity = (self: Calendar, selector: string) =>
  isEnabled(self) ? Array.from(self.context.mainElement.querySelectorAll<HTMLElement>(selector)).map((el) => getComputedStyle(el).opacity) : [];

export const playOpacity = (self: Calendar, selector: string, captured: string[]) => {
  if (!captured.length) return;
  const timing = getTiming(self, effects.fade);
  self.context.mainElement.querySelectorAll<HTMLElement>(selector).forEach((el, index) => {
    const from = captured[index];
    const to = getComputedStyle(el).opacity;
    if (from === undefined || from === to) return;
    el.animate([{ opacity: from }, { opacity: to }], timing);
  });
};

export type Layer = {
  el: HTMLElement;
  ghost: HTMLElement;
  animations: Animation[];
};

export const buildTransition = (self: Calendar, selector: string, effectName: AnimationEffect, render: () => void, onlyIndex?: number) => {
  const { mainElement } = self.context;
  cleanupPending(mainElement);

  const effect = effects[effectName];
  const timing = getTiming(self, effect);
  // Keep the ghost at its endpoint until the queued finish handler removes it.
  const ghostTiming: KeyframeAnimationOptions = { ...timing, fill: 'forwards' };

  const snapshots = Array.from(mainElement.querySelectorAll<HTMLElement>(selector)).map((el, index) => {
    if (onlyIndex !== undefined && onlyIndex !== index) return null;
    el.parentElement?.setAttribute('data-vc-clip', '');
    return { ghost: createGhost(el) };
  });

  render();

  const layers: Layer[] = [];

  mainElement.querySelectorAll<HTMLElement>(selector).forEach((el, index) => {
    const snapshot = snapshots[index];
    if (!snapshot) return;

    if (!el.children.length) {
      el.append(...snapshot.ghost.children);
      stopAnimating(el);
      return;
    }

    el.dataset.vcAnimating = '';
    el.parentElement?.setAttribute('data-vc-clip', '');
    el.parentElement?.appendChild(snapshot.ghost);

    const [leave, enter]: [Keyframe[], Keyframe[]] = effect.enter
      ? [
          [{ transform: 'none' }, { transform: effect.leave as string }],
          [{ transform: effect.enter }, { transform: 'none' }],
        ]
      : [
          [{ opacity: 1 }, { opacity: 0 }],
          [{ opacity: 0 }, { opacity: 1 }],
        ];

    layers.push({ el, ghost: snapshot.ghost, animations: [snapshot.ghost.animate(leave, ghostTiming), el.animate(enter, timing)] });
  });

  return { layers, duration: timing.duration };
};

// A queued finish must not remove clipping installed by a newer transition.
export const dropLayers = (layers: Layer[]) =>
  layers
    .filter(({ ghost }) => ghost.isConnected)
    .forEach(({ el, ghost }) => {
      ghost.remove();
      stopAnimating(el);
    });

const animate = (self: Calendar, selector: string, effectName: AnimationEffect, render: () => void, onlyIndex?: number) => {
  if (!isEnabled(self)) return render();

  const { layers } = buildTransition(self, selector, effectName, render, onlyIndex);
  layers.forEach((layer) => {
    layer.animations[1].onfinish = () => dropLayers([layer]);
  });
};

export default animate;

```

### `package/src/scripts/utils/canOpenOnFocus.ts`

```ts
import resolveToggle from '@scripts/utils/resolveToggle';
import type { Calendar } from '@src/index';

const canOpenOnFocus = (self: Calendar): boolean => {
  return resolveToggle(self, self.openOnFocus);
};

export default canOpenOnFocus;

```

### `package/src/scripts/utils/canToggleSelection.ts`

```ts
import resolveToggle from '@scripts/utils/resolveToggle';
import type { Calendar } from '@src/index';

const canToggleSelection = (self: Calendar): boolean => {
  return resolveToggle(self, self.enableDateToggle);
};

export default canToggleSelection;

```

### `package/src/scripts/utils/getColumnID.ts`

```ts
import type { Calendar } from '@src/index';

const getColumnID = (self: Calendar, type: string) => {
  if (self.type !== 'multiple') return { currentValue: null, columnID: 0 };

  const columnEls = self.context.mainElement.querySelectorAll<HTMLElement>('[data-vc="column"]');
  const columnID = Array.from(columnEls).findIndex((col) => col.closest(`[data-vc-column="${type}"]`));

  return {
    currentValue: columnID >= 0 ? Number(columnEls[columnID].querySelector<HTMLElement>(`[data-vc="${type}"]`)?.getAttribute(`data-vc-${type}`)) : null,
    columnID: Math.max(columnID, 0),
  };
};

export default getColumnID;

```

### `package/src/scripts/utils/getDate.ts`

```ts
import type { FormatDateString } from '@src/index';

const getDate: (date: FormatDateString) => Date = (date: FormatDateString) => new Date(`${date}T00:00:00`);

export default getDate;

```

### `package/src/scripts/utils/getDateString.ts`

```ts
import type { FormatDateString } from '@src/index';

const getDateString: (date: Date) => FormatDateString = (date: Date) => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');

  return `${year}-${month}-${day}` as FormatDateString;
};

export default getDateString;

```

### `package/src/scripts/utils/getErrorMessages.ts`

```ts
const errorMessages = {
  notFoundSelector: (selector: HTMLElement | string) =>
    `${selector} is not found, check the first argument passed to new Calendar. If the element lives inside a Shadow DOM, a string selector can't reach it - resolve the element yourself (e.g. shadowRoot.querySelector(...)) and pass it directly instead.`,
  notInit: 'The calendar has not been initialized, please initialize it using the "init()" method first.',
  alreadyInit: 'The calendar has already been initialized, calling init() again is not allowed. Create a new Calendar instance instead.',
  alreadyDestroyed: 'The calendar has already been destroyed, calling destroy() again is not allowed.',
  notLocale: 'You specified an incorrect language label or did not specify the required number of values ​​for «locale.weekdays» or «locale.months».',
  incorrectTime: 'The value of the time property can be: false, 12 or 24.',
  incorrectMonthsCount:
    'For the «multiple» calendar type, the «displayMonthsCount» parameter can have a value from 2 to 12, and for all others it cannot be greater than 1.',
  incorrectCollapseType: 'The «enableCollapse» parameter is only supported by the «default» and «week» calendar types.',
};

export default errorMessages;

```

### `package/src/scripts/utils/getLocalDate.ts`

```ts
import type { FormatDateString } from '@src/index';

const getLocalDate = (): FormatDateString => {
  const now = new Date();
  return new Date(now.getTime() - now.getTimezoneOffset() * 60000).toISOString().substring(0, 10) as FormatDateString;
};

export default getLocalDate;

```

### `package/src/scripts/utils/getLocale.ts`

```ts
import errorMessages from '@scripts/utils/getErrorMessages';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const capitalizeFirstLetter = (str: string): string => str.charAt(0).toUpperCase() + str.slice(1).replace(/\./, '');

const getLocaleWeekday = (self: Calendar, dayIndex: number, locale: string): void => {
  const date = new Date(`1978-01-0${dayIndex + 1}T00:00:00.000Z`);
  const weekdayShort = date.toLocaleString(locale, { weekday: 'short', timeZone: 'UTC' });
  const weekdayLong = date.toLocaleString(locale, { weekday: 'long', timeZone: 'UTC' });
  self.context.locale.weekdays.short.push(capitalizeFirstLetter(weekdayShort));
  self.context.locale.weekdays.long.push(capitalizeFirstLetter(weekdayLong));
};

const getLocaleMonth = (self: Calendar, monthIndex: number, locale: string): void => {
  const date = new Date(`1978-${String(monthIndex + 1).padStart(2, '0')}-01T00:00:00.000Z`);
  const monthShort = date.toLocaleString(locale, { month: 'short', timeZone: 'UTC' });
  const monthLong = date.toLocaleString(locale, { month: 'long', timeZone: 'UTC' });
  self.context.locale.months.short.push(capitalizeFirstLetter(monthShort));
  self.context.locale.months.long.push(capitalizeFirstLetter(monthLong));
};

const getLocale = (self: Calendar): void => {
  const isHasContextLocale =
    self.context.locale.weekdays.short[6] &&
    self.context.locale.weekdays.long[6] &&
    self.context.locale.months.short[11] &&
    self.context.locale.months.long[11];

  if (isHasContextLocale) return;

  if (typeof self.locale !== 'string') {
    const isManually = self.locale?.weekdays?.short[6] && self.locale?.weekdays?.long[6] && self.locale?.months?.short[11] && self.locale?.months?.long[11];
    if (!isManually) throw new Error(errorMessages.notLocale);
    setContext(self, 'locale', { ...self.locale });
    return;
  }

  if (typeof self.locale === 'string' && !self.locale.length) throw new Error(errorMessages.notLocale);

  Array.from({ length: 7 }, (_, i) => getLocaleWeekday(self, i, self.locale as string));
  Array.from({ length: 12 }, (_, i) => getLocaleMonth(self, i, self.locale as string));
};

export default getLocale;

```

### `package/src/scripts/utils/getLocaleString.ts`

```ts
import type { FormatDateString } from '@src/index';

let formatterKey = '';
let formatter: Intl.DateTimeFormat | undefined;

const getLocaleString = (dateStr: FormatDateString, locale: string, options: Intl.DateTimeFormatOptions) => {
  const key = JSON.stringify([locale, options]);

  if (!formatter || formatterKey !== key) {
    formatter = new Intl.DateTimeFormat(locale, options);
    formatterKey = key;
  }

  return formatter.format(new Date(`${dateStr}T00:00:00.000Z`));
};

export default getLocaleString;

```

### `package/src/scripts/utils/getRootNode.ts`

```ts
const getRootNode = (el: HTMLElement): Document | ShadowRoot => (el.getRootNode ? el.getRootNode() : document) as Document | ShadowRoot;

export default getRootNode;

```

### `package/src/scripts/utils/getWeekNumber.ts`

```ts
import getDate from '@scripts/utils/getDate';
import type { FormatDateString, WeekDayID } from '@src/index';

const getWeekNumber = (date: FormatDateString, weekStartDay: WeekDayID) => {
  const currentDate = getDate(date);
  const currentDay = (currentDate.getDay() - weekStartDay + 7) % 7;
  currentDate.setDate(currentDate.getDate() + 3 - currentDay);

  const yearStart = new Date(currentDate.getFullYear(), 0, 1);
  const weekNumber = Math.ceil(((+currentDate - +yearStart) / 86400000 + 1) / 7);

  return {
    year: currentDate.getFullYear(),
    week: weekNumber,
  };
};

export default getWeekNumber;

```

### `package/src/scripts/utils/getWeekStart.ts`

```ts
import type { WeekDayID } from '@src/index';

const getWeekStart = (date: Date, firstWeekday: WeekDayID) => {
  const weekStart = new Date(date);
  weekStart.setDate(date.getDate() - ((date.getDay() - firstWeekday + 7) % 7));
  return weekStart;
};

export default getWeekStart;

```

### `package/src/scripts/utils/initVariables/initAllVariables.ts`

```ts
import errorMessages from '@scripts/utils/getErrorMessages';
import initMonthsCount from '@scripts/utils/initVariables/initMonthsCount';
import initRange from '@scripts/utils/initVariables/initRange';
import initSelectedDates from '@scripts/utils/initVariables/initSelectedDates';
import initSelectedMonthYear from '@scripts/utils/initVariables/initSelectedMonthYear';
import initTime from '@scripts/utils/initVariables/initTime';
import initWeek from '@scripts/utils/initVariables/initWeek';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const initAllVariables = (self: Calendar) => {
  if (self.enableCollapse && !['default', 'week'].includes(self.type)) throw new Error(errorMessages.incorrectCollapseType);
  setContext(self, 'currentType', self.type);
  initMonthsCount(self);
  initRange(self);
  initSelectedMonthYear(self);
  initSelectedDates(self);
  initWeek(self);
  initTime(self);
};

export default initAllVariables;

```

### `package/src/scripts/utils/initVariables/initMonthsCount.ts`

```ts
import errorMessages from '@scripts/utils/getErrorMessages';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const initMonthsCount = (self: Calendar) => {
  if (self.type === 'multiple' && (self.displayMonthsCount <= 1 || self.displayMonthsCount > 12)) throw new Error(errorMessages.incorrectMonthsCount);
  if (self.type !== 'multiple' && self.displayMonthsCount > 1) throw new Error(errorMessages.incorrectMonthsCount);
  setContext(self, 'displayMonthsCount', self.displayMonthsCount ? self.displayMonthsCount : self.type === 'multiple' ? 2 : 1);
};

export default initMonthsCount;

```

### `package/src/scripts/utils/initVariables/initRange.ts`

```ts
import getDate from '@scripts/utils/getDate';
import parseDates from '@scripts/utils/parseDates';
import resolveDate from '@scripts/utils/resolveDate';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const initRange = (self: Calendar) => {
  // set self.context.displayDateMin, self.context.displayDateMax
  const dateMin = resolveDate(self.dateMin, self.dateMin);
  const dateMax = resolveDate(self.dateMax, self.dateMax);
  const displayDateMin = resolveDate(self.displayDateMin, dateMin);
  const displayDateMax = resolveDate(self.displayDateMax, dateMax);

  setContext(self, 'dateToday', resolveDate(self.dateToday, self.dateToday));

  setContext(self, 'displayDateMin', displayDateMin ? (getDate(dateMin) >= getDate(displayDateMin) ? dateMin : displayDateMin) : dateMin);
  setContext(self, 'displayDateMax', displayDateMax ? (getDate(dateMax) <= getDate(displayDateMax) ? dateMax : displayDateMax) : dateMax);

  const isDisablePast = self.disableDatesPast && !self.disableAllDates && getDate(displayDateMin) < getDate(self.context.dateToday);
  setContext(self, 'displayDateMin', isDisablePast ? self.context.dateToday : self.disableAllDates ? self.context.dateToday : displayDateMin);
  setContext(self, 'displayDateMax', self.disableAllDates ? self.context.dateToday : displayDateMax);

  // set self.context.disableDates
  setContext(
    self,
    'disableDates',
    self.disableDates[0] && !self.disableAllDates ? parseDates(self.disableDates) : self.disableAllDates ? [self.context.displayDateMin] : [],
  );
  if (self.context.disableDates.length > 1) self.context.disableDates.sort((a, b) => +new Date(a) - +new Date(b));

  // set self.context.enableDates
  setContext(self, 'enableDates', self.enableDates[0] ? parseDates(self.enableDates) : []);
  if (self.context.enableDates?.[0] && self.context.disableDates?.[0])
    setContext(
      self,
      'disableDates',
      self.context.disableDates.filter((d) => !self.context.enableDates.includes(d)),
    );
  if (self.context.enableDates.length > 1) self.context.enableDates.sort((a, b) => +new Date(a) - +new Date(b));

  if (self.context.enableDates?.[0] && self.disableAllDates) {
    setContext(self, 'displayDateMin', self.context.enableDates[0]);
    setContext(self, 'displayDateMax', self.context.enableDates[self.context.enableDates.length - 1]);
  }

  // set self.context.dateMin and self.context.dateMax
  setContext(self, 'dateMin', self.displayDisabledDates ? dateMin : self.context.displayDateMin);
  setContext(self, 'dateMax', self.displayDisabledDates ? dateMax : self.context.displayDateMax);
};

export default initRange;

```

### `package/src/scripts/utils/initVariables/initSelectedDates.ts`

```ts
import parseDates from '@scripts/utils/parseDates';
import setContext from '@scripts/utils/setContext';
import type { Calendar } from '@src/index';

const initSelectedDates = (self: Calendar) => {
  setContext(self, 'selectedDates', self.selectedDates?.[0] ? parseDates(self.selectedDates) : []);
};

export default initSelectedDates;

```

### `package/src/scripts/utils/initVariables/initSelectedMonthYear.ts`

```ts
import getDate from '@scripts/utils/getDate';
import parseDates from '@scripts/utils/parseDates';
import setContext from '@scripts/utils/setContext';
import type { Calendar, Range } from '@src/index';
import resolveDate from '@src/scripts/utils/resolveDate';

const displayClosestValidDate = (self: Calendar) => {
  const isBefore = (date1: string | Date, date2: Date) => new Date(date1).getTime() < date2.getTime();
  const isAfter = (date1: string | Date, date2: Date) => new Date(date1).getTime() > date2.getTime();

  const gotoMonthYear = (dateOrStr: Date) => {
    const gotoDate = new Date(dateOrStr);
    setInitialContext(self, gotoDate.getMonth() as Range<12>, gotoDate.getFullYear());
  };

  if (self.displayDateMin && self.displayDateMin !== 'today' && isAfter(self.displayDateMin as string, new Date())) {
    const parsedDate = self.selectedDates.length && self.selectedDates[0] ? parseDates(self.selectedDates)[0] : self.displayDateMin;
    gotoMonthYear(getDate(resolveDate(parsedDate, self.displayDateMin)));
    return true;
  }

  if (self.displayDateMax && self.displayDateMax !== 'today' && isBefore(self.displayDateMax as string, new Date())) {
    const parsedDate = self.selectedDates.length && self.selectedDates[0] ? parseDates(self.selectedDates)[0] : self.displayDateMax;
    gotoMonthYear(getDate(resolveDate(parsedDate, self.displayDateMax)));
    return true;
  }

  return false;
};

const setInitialContext = (self: Calendar, month: Range<12>, year: number) => {
  setContext(self, 'selectedMonth', month);
  setContext(self, 'selectedYear', year);
  setContext(self, 'displayYear', year);
};

const initSelectedMonthYear = (self: Calendar) => {
  const isJumpToSelectedDate = self.enableJumpToSelectedDate && self.selectedDates?.[0] && self.selectedMonth === undefined && self.selectedYear === undefined;

  if (isJumpToSelectedDate) {
    const selectedDate = getDate(parseDates(self.selectedDates)[0]);
    setInitialContext(self, selectedDate.getMonth() as Range<12>, selectedDate.getFullYear());
    return;
  }

  if (displayClosestValidDate(self)) return;

  const isValidMonth = self.selectedMonth !== undefined && Number(self.selectedMonth) >= 0 && Number(self.selectedMonth) < 12;
  const isValidYear = self.selectedYear !== undefined && Number(self.selectedYear) >= 0 && Number(self.selectedYear) <= 9999;

  setInitialContext(
    self,
    (isValidMonth ? Number(self.selectedMonth) : getDate(self.context.dateToday).getMonth()) as Range<12>,
    isValidYear ? Number(self.selectedYear) : getDate(self.context.dateToday).getFullYear(),
  );
};

export default initSelectedMonthYear;

```

### `package/src/scripts/utils/initVariables/initTime.ts`

```ts
import errorMessages from '@scripts/utils/getErrorMessages';
import setContext from '@scripts/utils/setContext';
import transformTime12 from '@scripts/utils/transformTime12';
import type { Calendar } from '@src/index';

const initTime = (self: Calendar) => {
  if (!self.selectionTimeMode) return;

  if (![12, 24].includes(self.selectionTimeMode)) throw new Error(errorMessages.incorrectTime);

  const isTime12 = self.selectionTimeMode === 12;
  const timeRegex = isTime12 ? /^(0[1-9]|1[0-2]):([0-5][0-9]) ?(AM|PM)?$/i : /^([0-1]?[0-9]|2[0-3]):([0-5][0-9])$/;

  let [hours, minutes, keeping]: string[] | null[] = self.selectedTime?.match(timeRegex)?.slice(1) ?? [];

  if (!hours) {
    hours = isTime12 ? transformTime12(String(self.timeMinHour)) : String(self.timeMinHour);
    minutes = String(self.timeMinMinute);
    keeping = isTime12 ? (Number(transformTime12(String(self.timeMinHour))) >= 12 ? 'PM' : 'AM') : null;
  } else if (isTime12 && !keeping) {
    keeping = 'AM';
  }

  setContext(self, 'selectedHours', hours.padStart(2, '0'));
  setContext(self, 'selectedMinutes', minutes.padStart(2, '0'));
  setContext(self, 'selectedKeeping', keeping as 'AM' | 'PM' | null);
  setContext(self, 'selectedTime', `${self.context.selectedHours}:${self.context.selectedMinutes}${keeping ? ` ${keeping}` : ''}`);
};

export default initTime;

```

### `package/src/scripts/utils/initVariables/initWeek.ts`

```ts
import getDate from '@scripts/utils/getDate';
import getDateString from '@scripts/utils/getDateString';
import getWeekStart from '@scripts/utils/getWeekStart';
import setContext from '@scripts/utils/setContext';
import type { Calendar, FormatDateString } from '@src/index';

// Preserve the displayed week across update() while it still overlaps the selected month.
const initWeek = (self: Calendar, reanchor = false) => {
  const { displayWeekDate, selectedMonth, selectedYear, selectedDates, dateToday } = self.context;

  const isSelectedMonth = (date: Date) => date.getMonth() === selectedMonth && date.getFullYear() === selectedYear;

  if (displayWeekDate && !reanchor) {
    const weekStart = getDate(displayWeekDate);
    const weekEnd = new Date(weekStart);
    weekEnd.setDate(weekStart.getDate() + 6);
    if (isSelectedMonth(weekStart) || isSelectedMonth(weekEnd)) {
      if (weekStart.getDay() === self.firstWeekday) return;

      // The fourth day determines which month owns a straddling week.
      const reference = new Date(weekStart);
      reference.setDate(weekStart.getDate() + 3);
      setContext(self, 'displayWeekDate', getDateString(getWeekStart(reference, self.firstWeekday)));
      return;
    }
  }

  const anchor = ([selectedDates?.[0], dateToday].filter(Boolean) as FormatDateString[]).map(getDate).find(isSelectedMonth);
  setContext(self, 'displayWeekDate', getDateString(getWeekStart(anchor ?? new Date(selectedYear, selectedMonth, 1), self.firstWeekday)));
};

export default initWeek;

```

### `package/src/scripts/utils/observeHtmlElement.ts`

```ts
const trackChangesHTMLElement = (htmlEl: HTMLElement, attr: string, actions: () => void) => {
  const changes = (mutationsList: MutationRecord[]) => {
    for (let i = 0; i < mutationsList.length; i++) {
      const record = mutationsList[i];
      if (record.attributeName === attr) {
        actions();
        break;
      }
    }
  };
  const observer = new MutationObserver(changes);
  observer.observe(htmlEl, { attributes: true });
};

export default trackChangesHTMLElement;

```

### `package/src/scripts/utils/parseComponent.ts`

```ts
import { getComponent } from '@scripts/components';
import type { Calendar } from '@src/index';

export const parseLayout = (self: Calendar, template: string): string => {
  return template
    .replace(/[\n\t]/g, '')
    .replace(/<#(?!\/?Multiple)(.*?)>/g, (_, tagContent) => {
      const type = (tagContent.match(/\[(.*?)\]/) || [])[1];
      const componentName = tagContent.replace(/[/\s\n\t]|\[(.*?)\]/g, '');
      const component = getComponent(componentName);
      const htmlContent = component ? component(self, type ?? null) : '';
      return self.sanitizerHTML(htmlContent);
    })
    .replace(/[\n\t]/g, '');
};

export const parseMultipleLayout = (self: Calendar, template: string): string => {
  return template
    .replace(/<#Multiple>(.*?)<#\/Multiple>/gs, (_, content) => {
      const repeatedContent = Array(self.context.displayMonthsCount).fill(content).join('');
      return self.sanitizerHTML(repeatedContent);
    })
    .replace(/[\n\t]/g, '');
};

```

### `package/src/scripts/utils/parseDates.ts`

```ts
import getDate from '@scripts/utils/getDate';
import getDateString from '@scripts/utils/getDateString';
import type { FormatDateString } from '@src/index';

const parseDates: (dates: Array<number | string | Date>) => FormatDateString[] = (dates: Array<number | string | Date>) =>
  dates.reduce((accumulator: FormatDateString[], date) => {
    if (date instanceof Date || typeof date === 'number') {
      const d = date instanceof Date ? date : new Date(date);
      accumulator.push(getDateString(d));
    } else if (date.match(/^(\d{4}-\d{2}-\d{2})$/g)) {
      accumulator.push(date as FormatDateString);
    } else {
      date.replace(/(\d{4}-\d{2}-\d{2}).*?(\d{4}-\d{2}-\d{2})/g, (_, startDateStr, endDateStr) => {
        const startDate = getDate(startDateStr);
        const endDate = getDate(endDateStr);
        const currentDate = new Date(startDate.getTime());

        for (currentDate; currentDate <= endDate; currentDate.setDate(currentDate.getDate() + 1)) {
          accumulator.push(getDateString(currentDate));
        }
        return _;
      });
    }
    return accumulator;
  }, []);

export default parseDates;

```

### `package/src/scripts/utils/positions/calculateAvailableSpace.ts`

```ts
import getOffset from '@scripts/utils/positions/getOffset';
import getViewportDimensions from '@scripts/utils/positions/getViewportDimensions';
import getWindowScrollPosition from '@scripts/utils/positions/getWindowScrollPosition';

/**
 * Calculates the available space for each side of the DOM element.
 * @param {HTMLElement} element - The DOM element to calculate space for.
 * @returns {{ top: number, bottom: number, left: number, right: number }} An object containing the available space on the top, bottom, left, and right sides of the element.
 */

function calculateAvailableSpace(element: HTMLElement): { top: number; bottom: number; left: number; right: number } {
  const { top: scrollTop, left: scrollLeft } = getWindowScrollPosition();
  const { top: elementTop, left: elementLeft } = getOffset(element);
  const { vh: viewportHeight, vw: viewportWidth } = getViewportDimensions();

  const elementOffsetTop = elementTop - scrollTop;
  const elementOffsetLeft = elementLeft - scrollLeft;

  return {
    top: elementOffsetTop,
    bottom: viewportHeight - (elementOffsetTop + element.clientHeight),
    left: elementOffsetLeft,
    right: viewportWidth - (elementOffsetLeft + element.clientWidth),
  };
}

export default calculateAvailableSpace;

```

### `package/src/scripts/utils/positions/findBestPickerPosition.ts`

```ts
import getAvailablePosition from '@scripts/utils/positions/getAvailablePosition';
import type { Positions } from '@src/index';

/**
 * Determines the best position for displaying a calendar picker relative to an input element.
 * @param {HTMLInputElement} input - The input element.
 * @param {HTMLElement} calendar - The calendar picker modal.
 * @returns {Positions | Positions[]} The best position(s) for the calendar picker modal.
 */

function findBestPickerPosition(input: HTMLInputElement, calendar: HTMLElement): Positions | Positions[] {
  const position: Positions | Positions[] = 'left';

  if (!calendar || !input) return position;

  const { canShow, parentPositions } = getAvailablePosition(input, calendar);
  const isCenterPosition = canShow.left && canShow.right;

  const bestPosition: Positions | Positions[] =
    isCenterPosition && canShow.bottom
      ? 'center'
      : isCenterPosition && canShow.top
        ? ['top', 'center']
        : Array.isArray(parentPositions)
          ? [parentPositions[0] === 'bottom' ? 'top' : 'bottom', ...parentPositions.slice(1)]
          : parentPositions;

  return bestPosition || position;
}

export default findBestPickerPosition;

```

### `package/src/scripts/utils/positions/getAvailablePosition.ts`

```ts
import calculateAvailableSpace from '@scripts/utils/positions/calculateAvailableSpace';
import getOffset from '@scripts/utils/positions/getOffset';
import getViewportDimensions from '@scripts/utils/positions/getViewportDimensions';
import type { Positions } from '@src/index';

/**
 * Determines available positions for displaying a picker element relative to a parent element,
 * considering available space and margin offset.
 * @param {HTMLElement} parentElm - The input element.
 * @param {HTMLElement} pickerElm - The calendar picker modal.
 * @param {number} marginOffset - Margin offset applied when the picker is opened.
 * @returns {{ canShow: { top: boolean, bottom: boolean, left: boolean, right: boolean }, parentPositions: Positions[] }}
 * An object containing the possible display positions and parent element positions.
 */

function getAvailablePosition(parentElm: HTMLElement, pickerElm: HTMLElement, marginOffset = 5) {
  const canShow = {
    top: true,
    bottom: true,
    left: true,
    right: true,
  };
  const parentPositions: Positions[] = [];

  if (!pickerElm || !parentElm) return { canShow, parentPositions };

  const { bottom: spaceBottom, top: spaceTop } = calculateAvailableSpace(parentElm);
  const { top: pickerOffsetTop, left: pickerOffsetLeft } = getOffset(parentElm);
  const { height: pickerHeight, width: pickerWidth } = pickerElm.getBoundingClientRect();
  const { vh, vw } = getViewportDimensions();
  const bodyCenterCoordinate = { x: vw / 2, y: vh / 2 };

  const positionMappings: Array<{ condition: boolean; position: Positions }> = [
    { condition: pickerOffsetTop < bodyCenterCoordinate.y, position: 'top' },
    { condition: pickerOffsetTop > bodyCenterCoordinate.y, position: 'bottom' },
    { condition: pickerOffsetLeft < bodyCenterCoordinate.x, position: 'left' },
    { condition: pickerOffsetLeft > bodyCenterCoordinate.x, position: 'right' },
  ];

  positionMappings.forEach(({ condition, position }) => {
    if (condition) parentPositions.push(position);
  });

  Object.assign(canShow, {
    top: pickerHeight <= spaceTop - marginOffset,
    bottom: pickerHeight <= spaceBottom - marginOffset,
    left: pickerWidth <= pickerOffsetLeft,
    right: pickerWidth <= vw - pickerOffsetLeft,
  });

  return { canShow, parentPositions };
}

export default getAvailablePosition;

```

### `package/src/scripts/utils/positions/getOffset.ts`

```ts
import type { HtmlElementPosition } from '@src/index';

/**
 * Get the offset position of an HTML element relative to the viewport.
 * @param {HTMLElement | null} element - The HTML element whose position is to be calculated.
 * @returns {HtmlElementPosition} An object containing the top, bottom, left, and right offset positions of the element.
 */

function getOffset(element?: HTMLElement | null): HtmlElementPosition {
  if (!element || !element.getBoundingClientRect) return { top: 0, bottom: 0, left: 0, right: 0 };

  const box = element.getBoundingClientRect();
  const docElem = document.documentElement;

  return {
    bottom: box.bottom,
    right: box.right,
    top: box.top + window.scrollY - docElem.clientTop,
    left: box.left + window.scrollX - docElem.clientLeft,
  };
}

export default getOffset;

```

### `package/src/scripts/utils/positions/getViewportDimensions.ts`

```ts
/**
 * Get the dimensions of the viewport.
 * @returns {{ vw: number; vh: number; }} An object containing the viewport width (`vw`) and height (`vh`).
 */

function getViewportDimensions() {
  return {
    vw: Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0),
    vh: Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0),
  };
}

export default getViewportDimensions;

```

### `package/src/scripts/utils/positions/getWindowScrollPosition.ts`

```ts
/**
 * Get the current scroll position of the window.
 * @returns {{ left: number, top: number }} An object containing the horizontal (left) and vertical (top) scroll positions.
 */

function getWindowScrollPosition(): { left: number; top: number } {
  return {
    left: window.scrollX || document.documentElement.scrollLeft || 0,
    top: window.scrollY || document.documentElement.scrollTop || 0,
  };
}

export default getWindowScrollPosition;

```

### `package/src/scripts/utils/positions/setPosition.ts`

```ts
import findBestPickerPosition from '@scripts/utils/positions/findBestPickerPosition';
import getOffset from '@scripts/utils/positions/getOffset';
import getViewportDimensions from '@scripts/utils/positions/getViewportDimensions';
import type { Calendar } from '@src/index';

/** Set the calendar picker position according to the user's choice coming from `positionToInput` option. */

const setPosition = (input: HTMLInputElement | undefined, calendar: HTMLElement, position: Calendar['positionToInput']) => {
  if (!input) return;
  const pos = position === 'auto' ? findBestPickerPosition(input, calendar) : position;

  const getPosition = {
    top: -calendar.offsetHeight,
    bottom: input.offsetHeight,
    left: 0,
    center: input.offsetWidth / 2 - calendar.offsetWidth / 2,
    right: input.offsetWidth - calendar.offsetWidth,
  };

  const YPosition = !Array.isArray(pos) ? 'bottom' : pos[0];
  const XPosition = !Array.isArray(pos) ? pos : pos[1];

  // add data attribute with Y position
  calendar.dataset.vcPosition = YPosition;

  const { top: offsetTop, left: offsetLeft } = getOffset(input);
  const top = offsetTop + getPosition[YPosition];
  let left = offsetLeft + getPosition[XPosition];

  // make sure the new position is not outside the viewport,
  // if so then change position to have enough space to show full picker
  const { vw } = getViewportDimensions();
  if (left + calendar.clientWidth > vw) {
    const scrollbarWidth = window.innerWidth - document.body.clientWidth;
    left = vw - calendar.clientWidth - scrollbarWidth;
  } else if (left < 0) {
    left = 0;
  }

  Object.assign(calendar.style, { left: `${left}px`, top: `${top}px` });
};

export default setPosition;

```

### `package/src/scripts/utils/replaceProperties.ts`

```ts
const replaceProperties = <T extends object>(original: T, replacement: T) => {
  const keys = Object.keys(replacement) as Array<keyof T>;
  for (let i = 0; i < keys.length; i++) {
    const key = keys[i];
    if (
      typeof original[key] === 'object' &&
      original[key] !== null &&
      typeof replacement[key] === 'object' &&
      replacement[key] !== null &&
      !(replacement[key] instanceof Date) &&
      !Array.isArray(replacement[key])
    ) {
      replaceProperties(original[key] as object, replacement[key] as object);
    } else if (replacement[key] !== undefined) {
      original[key] = replacement[key];
    }
  }
};

export default replaceProperties;

```

### `package/src/scripts/utils/resolveDate.ts`

```ts
import getLocalDate from '@scripts/utils/getLocalDate';
import parseDates from '@scripts/utils/parseDates';
import type { DateAny, FormatDateString } from '@src/index';

const resolveDate = (date: 'today' | Date | number | string | null | undefined, defaultDate: DateAny): FormatDateString => {
  if (date === 'today') return getLocalDate();
  if (date instanceof Date || typeof date === 'number' || typeof date === 'string') return parseDates([date])[0];
  return defaultDate as FormatDateString;
};

export default resolveDate;

```

### `package/src/scripts/utils/resolveToggle.ts`

```ts
import type { Calendar, ToggleSelected } from '@src/index';

const resolveToggle = (self: Calendar, value?: ToggleSelected): boolean => {
  if (value !== undefined) return typeof value === 'function' ? value(self) : value;
  return true;
};

export default resolveToggle;

```

### `package/src/scripts/utils/rovingTabIndex.ts`

```ts
import type { Calendar } from '@src/index';

type Group = { container: string; item: string; active: string[] };

// A grid is a single tab stop: the arrow keys reach the rest of its cells.
const groups: Group[] = [
  {
    container: '[data-vc="dates"]',
    item: '[data-vc-date-btn]',
    active: ['[data-vc-date-selected] [data-vc-date-btn]', '[data-vc-date-today] [data-vc-date-btn]'],
  },
  { container: '[data-vc="months"]', item: '[data-vc-months-month]', active: ['[data-vc-months-month-selected]'] },
  { container: '[data-vc="years"]', item: '[data-vc-years-year]', active: ['[data-vc-years-year-selected]'] },
];

const isEnabled = (el: HTMLElement) => !el.hasAttribute('disabled') && el.getAttribute('aria-disabled') !== 'true';

const getActiveItem = (containerEl: HTMLElement, group: Group, items: HTMLElement[]) => {
  const preferred = group.active.map((selector) => containerEl.querySelector<HTMLElement>(selector)).find((el): el is HTMLElement => !!el && isEnabled(el));
  return preferred ?? items.find(isEnabled) ?? items[0];
};

const setRovingItem = (containerEl: HTMLElement, group: Group, activeEl: HTMLElement | null) => {
  const items = Array.from(containerEl.querySelectorAll<HTMLElement>(group.item));
  if (!items[0]) return;
  const active = activeEl && isEnabled(activeEl) ? activeEl : getActiveItem(containerEl, group, items);
  items.forEach((item) => {
    item.tabIndex = item === active ? 0 : -1;
  });
};

export const focusRovingItem = (event: FocusEvent) => {
  const target = event.target as HTMLElement;
  const group = groups.find((item) => target.matches?.(item.item));
  const containerEl = group ? target.closest<HTMLElement>(group.container) : null;
  if (group && containerEl) setRovingItem(containerEl, group, target);
};

const updateRovingTabIndex = (self: Calendar) => {
  groups.forEach((group) => {
    self.context.mainElement.querySelectorAll<HTMLElement>(group.container).forEach((containerEl) => {
      if (containerEl.closest('[data-vc-ghost]')) return;
      setRovingItem(containerEl, group, null);
    });
  });
};

export default updateRovingTabIndex;

```

### `package/src/scripts/utils/setContext.ts`

```ts
/* eslint-disable @typescript-eslint/no-explicit-any */
import type { Calendar, ContextVariables } from '@src/index';

const setContext = <K extends keyof ContextVariables>(self: Calendar, name: K, value: ContextVariables[K]) => {
  (self.context as any)[name] = value;
};

export default setContext;

```

### `package/src/scripts/utils/setWeekDate.ts`

```ts
import getDateString from '@scripts/utils/getDateString';
import setContext from '@scripts/utils/setContext';
import type { Calendar, Range } from '@src/index';

// The fourth day determines which month owns a straddling week.
const setWeekDate = (self: Calendar, weekStart: Date) => {
  const reference = new Date(weekStart);
  reference.setDate(weekStart.getDate() + 3);

  setContext(self, 'displayWeekDate', getDateString(weekStart));
  setContext(self, 'selectedMonth', reference.getMonth() as Range<12>);
  setContext(self, 'selectedYear', reference.getFullYear());
};

export default setWeekDate;

```

### `package/src/scripts/utils/skipOpenOnFocus.ts`

```ts
import type { Calendar } from '@src/index';

const skipOpenOnFocus = new WeakSet<Calendar>();

export const shouldSkipOpenOnFocus = (self: Calendar) => skipOpenOnFocus.has(self);

export const setSkipOpenOnFocus = (self: Calendar) => {
  skipOpenOnFocus.add(self);
};

export const clearSkipOpenOnFocus = (self: Calendar) => {
  skipOpenOnFocus.delete(self);
};

```

### `package/src/scripts/utils/toggleTabbing.ts`

```ts
const PREV_TABINDEX_ATTR = 'data-vc-prev-tabindex';

const isFocusable = (el: HTMLElement) => el.tabIndex >= 0 && !el.hasAttribute('disabled') && el.getAttribute('aria-disabled') !== 'true';

const storePrevTabIndex = (el: HTMLElement) => {
  if (el.hasAttribute(PREV_TABINDEX_ATTR)) return;
  const prev = el.getAttribute('tabindex');
  el.setAttribute(PREV_TABINDEX_ATTR, prev ?? '');
};

const restorePrevTabIndex = (el: HTMLElement) => {
  if (!el.hasAttribute(PREV_TABINDEX_ATTR)) return;
  const prev = el.getAttribute(PREV_TABINDEX_ATTR);
  if (prev === '' || prev === null) {
    el.removeAttribute('tabindex');
  } else {
    el.setAttribute('tabindex', prev);
  }
  el.removeAttribute(PREV_TABINDEX_ATTR);
};

export const disableTabbing = (root: HTMLElement) => {
  if (isFocusable(root)) {
    storePrevTabIndex(root);
    root.tabIndex = -1;
  }

  const walker = document.createTreeWalker(root, NodeFilter.SHOW_ELEMENT, {
    acceptNode: (node) => (isFocusable(node as HTMLElement) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP),
  });

  while (walker.nextNode()) {
    const el = walker.currentNode as HTMLElement;
    storePrevTabIndex(el);
    el.tabIndex = -1;
  }
};

export const restoreTabbing = (root: HTMLElement) => {
  restorePrevTabIndex(root);
  root.querySelectorAll<HTMLElement>(`[${PREV_TABINDEX_ATTR}]`).forEach(restorePrevTabIndex);
};

// `inert` takes the closed popup out of the focus order and the accessibility tree in one go;
// the tabindex bookkeeping above stays as the fallback for browsers that do not support it.
export const hideFromAT = (root: HTMLElement) => {
  root.setAttribute('inert', '');
  root.ariaHidden = 'true';
  disableTabbing(root);
};

export const showToAT = (root: HTMLElement) => {
  root.removeAttribute('inert');
  root.removeAttribute('aria-hidden');
  restoreTabbing(root);
};

```

### `package/src/scripts/utils/transformTime12.ts`

```ts
const transformTime12 = (hour: string): string => {
  const hourMap: { [key: number]: string } = {
    0: '12',
    13: '01',
    14: '02',
    15: '03',
    16: '04',
    17: '05',
    18: '06',
    19: '07',
    20: '08',
    21: '09',
    22: '10',
    23: '11',
  };

  return hourMap[Number(hour)] || String(hour);
};

export default transformTime12;

```

### `package/src/scripts/utils/transformTime24.ts`

```ts
const transformTime24 = (hour: string, keeping: 'AM' | 'PM') => {
  const hourMap: { [key: number]: { [key: string]: string } } = {
    0: { AM: '00', PM: '12' },
    1: { AM: '01', PM: '13' },
    2: { AM: '02', PM: '14' },
    3: { AM: '03', PM: '15' },
    4: { AM: '04', PM: '16' },
    5: { AM: '05', PM: '17' },
    6: { AM: '06', PM: '18' },
    7: { AM: '07', PM: '19' },
    8: { AM: '08', PM: '20' },
    9: { AM: '09', PM: '21' },
    10: { AM: '10', PM: '22' },
    11: { AM: '11', PM: '23' },
    12: { AM: '00', PM: '12' },
  };

  return hourMap[Number(hour)]?.[keeping] || String(hour);
};

export default transformTime24;

```

### `package/src/scripts/utils/updateNavigationA11y.ts`

```ts
import type { Calendar } from '@src/index';

export type NavigationType = 'month' | 'year' | 'week';
export type NavigationRoute = 'prev' | 'next';

export const getCollapseA11y = (self: Calendar) => {
  const expanded = self.context.currentType !== 'week';
  return { expanded, label: expanded ? self.labels.collapse : self.labels.expand };
};

export const getArrowLabel = (self: Calendar, route: NavigationRoute, type: NavigationType) => self.labels[`arrow${route === 'prev' ? 'Prev' : 'Next'}`][type];

const updateNavigationA11y = (self: Calendar, type: NavigationType) => {
  const collapseEl = self.context.mainElement.querySelector<HTMLElement>('[data-vc="collapse"]');
  if (collapseEl) {
    const { expanded, label } = getCollapseA11y(self);
    collapseEl.ariaExpanded = String(expanded);
    collapseEl.ariaLabel = label;
  }

  (['prev', 'next'] as const).forEach((route) => {
    const arrowEl = self.context.mainElement.querySelector<HTMLElement>(`[data-vc-arrow="${route}"]`);
    if (arrowEl) arrowEl.ariaLabel = getArrowLabel(self, route, type);
  });
};

export default updateNavigationA11y;

```

### `package/src/styles.ts`

```ts
const styles = {
  calendar: 'vc',
  controls: 'vc-controls',
  grid: 'vc-grid',
  column: 'vc-column',
  header: 'vc-header',
  headerContent: 'vc-header__content',
  month: 'vc-month',
  year: 'vc-year',
  arrowPrev: 'vc-arrow vc-arrow_prev',
  arrowNext: 'vc-arrow vc-arrow_next',
  wrapper: 'vc-wrapper',
  content: 'vc-content',
  months: 'vc-months',
  monthsRow: 'vc-months__row',
  monthsCell: 'vc-months__cell',
  monthsMonth: 'vc-months__month',
  years: 'vc-years',
  yearsRow: 'vc-years__row',
  yearsCell: 'vc-years__cell',
  yearsYear: 'vc-years__year',
  week: 'vc-week',
  weekDay: 'vc-week__day',
  weekDayBtn: 'vc-week__day-btn',
  weekNumbers: 'vc-week-numbers',
  weekNumbersTitle: 'vc-week-numbers__title',
  weekNumbersContent: 'vc-week-numbers__content',
  weekNumber: 'vc-week-number',
  collapse: 'vc-collapse',
  dates: 'vc-dates',
  datesRow: 'vc-dates__row',
  date: 'vc-date',
  dateBtn: 'vc-date__btn',
  datePopup: 'vc-date__popup',
  dateRangeTooltip: 'vc-date-range-tooltip',
  time: 'vc-time',
  timeContent: 'vc-time__content',
  timeHour: 'vc-time__hour',
  timeMinute: 'vc-time__minute',
  timeKeeping: 'vc-time__keeping',
  timeRanges: 'vc-time__ranges',
  timeRange: 'vc-time__range',
};

export default styles;

```

### `package/src/styles/index.css`

```css
@import './layout.css';
@import './themes/light.css';
@import './themes/dark.css';

```

### `package/src/styles/layout.css`

```css
[data-vc='calendar'] {
  @apply relative box-border min-w-[272px] flex flex-col p-4 rounded-xl opacity-100 transition-opacity select-none;
}

[data-vc='calendar']:focus-visible,
[data-vc='calendar'] button:focus-visible,
[data-vc='calendar'] [tabindex='0']:focus-visible {
  @apply outline outline-1 -outline-offset-1 rounded-lg;
}

[data-vc='calendar'][data-vc-type='multiple'] [data-vc='dates'] {
  @apply grow-0;
}

[data-vc='calendar'][data-vc-calendar-hidden] {
  @apply opacity-0 pointer-events-none [&_*]:!pointer-events-none;
}

[data-vc='calendar'][data-vc-input] {
  @apply absolute;
}

[data-vc='calendar'][data-vc-input][data-vc-position='bottom'] {
  @apply mt-1;
}

[data-vc='calendar'][data-vc-input][data-vc-position='top'] {
  @apply -mt-1;
}

[data-vc='controls'] {
  @apply absolute z-20 left-0 right-0 top-0 flex justify-between items-center pt-5 px-4 pointer-events-none box-content;
}

[data-vc-arrow] {
  @apply relative pointer-events-auto block w-6 h-6 cursor-pointer border-0 bg-transparent
	before:content-[''] before:absolute before:left-0 before:top-0 before:w-full before:h-full before:bg-no-repeat before:bg-center;
}

[data-vc-arrow='prev']::before {
  transform: rotateZ(90deg);
}

[data-vc-arrow='next']::before {
  transform: rotateZ(-90deg);
}

[data-vc='grid'] {
  @apply flex flex-wrap gap-7 grow;
}

[data-vc='grid'][data-vc-grid='hidden'] [data-vc='column'] {
  @apply opacity-30 pointer-events-none;
}

[data-vc='grid'][data-vc-grid='hidden'] [data-vc='column'][data-vc-column='month'],
[data-vc='grid'][data-vc-grid='hidden'] [data-vc='column'][data-vc-column='year'] {
  @apply opacity-100 pointer-events-auto;
}

[data-vc='column'] {
  @apply min-w-[240px] flex flex-col grow;
}

[data-vc='header'] {
  @apply relative flex items-center mb-3;
}

[data-vc-header='content'] {
  @apply grid grid-flow-col auto-cols-max items-center justify-center px-4 whitespace-pre-wrap grow;
}

[data-vc='month'],
[data-vc='year'] {
  @apply text-base font-bold cursor-pointer rounded p-1 border-0 bg-transparent disabled:pointer-events-none;
}

[data-vc='wrapper'] {
  @apply flex grow;
}

[data-vc='content'] {
  @apply flex flex-col grow;
}

[data-vc='months'] {
  @apply grid grid-cols-1 grid-rows-[auto] gap-y-4 items-center grow;
}

[data-vc-months='row'] {
  @apply grid grid-cols-4 gap-x-1 items-center w-full;
}

[data-vc='years'] {
  @apply grid grid-cols-1 grid-rows-[auto] gap-y-4 items-center grow;
}

[data-vc-years='row'] {
  @apply grid grid-cols-5 gap-x-1 items-center w-full;
}

[data-vc-months='cell'],
[data-vc-years='cell'] {
  @apply flex items-center justify-center w-full;
}

[data-vc-months-month],
[data-vc-years-year] {
  @apply flex items-center justify-center w-full h-10 text-center text-xs font-semibold p-1 rounded-lg border-0 break-all cursor-pointer disabled:pointer-events-none;
}

[data-vc-week='numbers'] {
  @apply flex flex-col;
}

[data-vc-week-numbers='title'] {
  @apply text-xs font-bold flex items-center min-h-6 justify-center mb-1.5;
}

[data-vc-week-numbers='content'] {
  @apply grid grid-flow-row items-center justify-items-center gap-y-1 py-0.5;
}

[data-vc-week-number] {
  @apply text-xs font-semibold w-full min-h-[1.875rem] min-w-[1.875rem] flex items-center justify-center cursor-pointer bg-transparent border-none p-0 m-0;
}

[data-vc='week'] {
  @apply grid grid-cols-[repeat(7,_1fr)] justify-items-center mb-1.5;
}

[data-vc-week-day] {
  @apply text-xs font-bold w-full min-h-6 min-w-[1.875rem] flex items-center justify-center bg-transparent border-none p-0 m-0;
}

[data-vc-week-day-btn] {
  @apply text-xs font-bold w-full h-full min-h-6 flex items-center justify-center cursor-pointer bg-transparent border-none p-0 m-0;
}

/* The published stylesheet ships without Tailwind's preflight, so any utility whose value is
   composed from several `--tw-*` variables resolves to an invalid declaration and is dropped.
   Transform and touch-action are written out by hand for that reason. */
[data-vc='collapse'] {
  @apply relative block shrink-0 w-full h-4 mt-1 -mb-1 cursor-pointer border-0 bg-transparent touch-none
	before:content-[''] before:absolute before:left-1/2 before:top-1/2 before:w-8 before:h-[3px] before:rounded-full
	surehover:before:w-4 surehover:before:h-4 surehover:before:rounded-none surehover:before:bg-no-repeat surehover:before:bg-center;
}

[data-vc='collapse']::before {
  transform: translate(-50%, -50%);
}

@media (hover: hover) and (pointer: fine) {
  [data-vc='collapse']::before {
    transform: translate(-50%, -50%) rotate(180deg);
  }

  [data-vc-type='week'] [data-vc='collapse']::before,
  [data-vc-type='default']:has([data-vc-collapsing]) [data-vc='collapse']::before {
    transform: translate(-50%, -50%) rotate(0deg);
  }

  [data-vc-type='week']:has([data-vc-collapsing]) [data-vc='collapse']::before {
    transform: translate(-50%, -50%) rotate(180deg);
  }
}

@media (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference) {
  [data-vc='collapse']::before {
    transition: transform 200ms ease-in-out;
  }
}

[data-vc-swipe] [data-vc='content'] {
  touch-action: pan-y;
}

[data-vc-dragging] {
  @apply cursor-grabbing [&_*]:!cursor-grabbing;
}

/* Prevent row redistribution while the grid height is animated. */
[data-vc-collapsing] {
  @apply flex-none [align-content:start];
  overflow: hidden;
  overflow: clip;
}

/* `clip` prevents focus scrolling; `hidden` is its fallback. Relative positioning keeps absolute
   ghosts inside the clipping context. */
[data-vc-clip] {
  @apply relative;
  overflow: hidden;
  overflow: clip;
}

[data-vc-ghost] {
  @apply absolute pointer-events-none;
  overflow: hidden;
  overflow: clip;
}

[data-vc='dates'] {
  @apply grid grid-cols-1 grid-rows-[auto] justify-items-center items-center grow pointer-events-none;
}

[data-vc='dates'][data-vc-dates-disabled] [data-vc-date-btn] {
  @apply cursor-default;
}

[data-vc-dates='row'] {
  @apply grid grid-cols-[repeat(7,_1fr)] justify-items-center items-center w-full;
}

[data-vc-date] {
  @apply relative w-full flex items-center justify-center py-0.5 pointer-events-auto;
}

[data-vc-date][data-vc-date-disabled],
[data-vc-date][data-vc-date-disabled] [data-vc-date-btn],
[data-vc-date]:not(:has([data-vc-date-btn])) {
  @apply pointer-events-none;
}

[data-vc-date][data-vc-date-hover] [data-vc-date-btn] {
  @apply rounded-none;
}

[data-vc-date][data-vc-date-hover='first'] [data-vc-date-btn] {
  @apply rounded-r-none rounded-l-lg;
}

[data-vc-date][data-vc-date-hover='last'] [data-vc-date-btn] {
  @apply rounded-l-none rounded-r-lg;
}

[data-vc-date][data-vc-date-hover='first-and-last'] [data-vc-date-btn] {
  @apply rounded-lg;
}

[data-vc-date][data-vc-date-hover='first'][data-vc-date-selected] [data-vc-date-btn] {
  @apply rounded-l-lg;
}

[data-vc-date][data-vc-date-hover='last'][data-vc-date-selected] [data-vc-date-btn] {
  @apply rounded-r-lg;
}

[data-vc-date][data-vc-date-selected='first'] [data-vc-date-btn] {
  @apply rounded-r-none rounded-l-lg;
}

[data-vc-date][data-vc-date-selected='last'] [data-vc-date-btn] {
  @apply rounded-l-none rounded-r-lg;
}

[data-vc-date][data-vc-date-selected='first-and-last'] [data-vc-date-btn] {
  @apply rounded-l-lg rounded-r-lg;
}

[data-vc-date][data-vc-date-selected='middle'] [data-vc-date-btn] {
  @apply rounded-none;
}

[data-vc-date][data-vc-date-disabled] + [data-vc-date-selected] [data-vc-date-btn],
[data-vc-date][data-vc-date-disabled] + [data-vc-date-hover] [data-vc-date-btn] {
  @apply rounded-l-lg;
}

[data-vc-date][data-vc-date-hover]:has(+ [data-vc-date-disabled]) [data-vc-date-btn],
[data-vc-date][data-vc-date-selected]:has(+ [data-vc-date-disabled]) [data-vc-date-btn] {
  @apply rounded-r-lg;
}

[data-vc-date-btn]:focus-visible + [data-vc-date-popup],
[data-vc-date-btn]:hover + [data-vc-date-popup],
[data-vc-date-popup]:focus-visible,
[data-vc-date-popup]:hover {
  @apply opacity-100 pointer-events-auto;
}

[data-vc-date-btn] {
  @apply text-xs font-normal w-full h-full min-h-[1.875rem] min-w-[1.875rem] flex items-center justify-center rounded-lg border-0 p-0 cursor-pointer transition-all duration-75;
}

[data-vc-date][data-vc-date-today] [data-vc-date-btn] {
  @apply font-bold;
}

[data-vc-date-popup] {
  transform: translateX(-50%);
  @apply absolute z-20 min-w-20 max-w-36 py-1 px-2 text-xs font-normal rounded-lg transition-opacity duration-75 opacity-0 pointer-events-none hover:opacity-100 hover:pointer-events-auto;
}

[data-vc-date-range-tooltip] {
  transform: translate(-50%, -100%);
  @apply absolute z-30 max-w-36 py-1 px-2 text-xs font-normal rounded-md pointer-events-none;
}

[data-vc-date-range-tooltip='hidden'] {
  @apply opacity-0;
}

[data-vc-date-range-tooltip='visible'] {
  @apply opacity-100;
}

[data-vc='time'] {
  @apply grid grid-cols-[auto_1fr] gap-3 border-solid border-t border-b-0 border-l-0 border-r-0 pt-3 mt-3;
}

[data-vc-time='content'] {
  @apply grid grid-flow-col items-center;
}

[data-vc-time-input='hour'] {
  @apply relative w-7 mr-[0.35rem] after:content-[':'] after:block after:absolute after:-right-[5px] after:top-1/2 after:mt-[calc(-50%_+_1px)];
}

[data-vc-time-input='minute'] {
  @apply w-7;
}

[data-vc-time-input='hour'] input,
[data-vc-time-input='minute'] input {
  @apply box-border relative block text-lg leading-[1.125rem] font-semibold text-center w-full p-[0.125rem] m-0 border-0 rounded select-text disabled:cursor-default disabled:hover:bg-transparent focus-visible:outline-1 focus-visible:outline;
}

[data-vc-time='keeping'] {
  @apply ml-[1px] cursor-pointer text-[0.69rem] w-[22px] rounded mt-1 disabled:cursor-default disabled:hover:bg-transparent focus-visible:outline-1 focus-visible:outline bg-transparent border-0 p-0;
}

[data-vc-time='ranges'] {
  @apply grid grid-flow-row;
}

[data-vc-time-range] {
  @apply text-[0] relative z-10 before:left-0 after:right-0;
}

[data-vc-time-range]::before,
[data-vc-time-range]::after {
  content: '';
  transform: translateY(-50%);
  @apply w-[1px] h-2 absolute z-10 pointer-events-none top-1/2;
}

[data-vc-time-range] input {
  @apply w-full relative appearance-none h-6 cursor-pointer m-0 outline-0;
}

[data-vc-time-range] input::-webkit-slider-thumb {
  @apply appearance-none -mt-2 relative z-20 box-border border border-solid h-4 w-3 shadow-none rounded cursor-pointer;
}

[data-vc-time-range] input::-moz-range-thumb {
  @apply relative z-20 box-border border border-solid h-4 w-3 shadow-none rounded cursor-pointer;
}

[data-vc-time-range] input::-webkit-slider-runnable-track {
  @apply box-border w-full h-[1px] mt-[1px] cursor-pointer shadow-none;
}

[data-vc-time-range] input::-moz-range-track {
  @apply box-border w-full h-[1px] mt-[1px] cursor-pointer shadow-none;
}

```

### `package/src/styles/themes/dark.css`

```css
[data-vc-theme='dark'].vc {
  @apply bg-[var(--vc-bg,theme(colors.slate.900))] text-[var(--vc-color,theme(colors.white))];
}

[data-vc-theme='dark'].vc[data-vc-input] {
  @apply shadow-[0_9px_20px_rgba(0,0,0,.1)];
}

[data-vc-theme='dark'].vc:focus-visible,
[data-vc-theme='dark'].vc button:focus-visible,
[data-vc-theme='dark'].vc [tabindex='0']:focus-visible {
  @apply outline-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='dark'] .vc-arrow {
  @apply bg-transparent before:bg-dark-arrow surehover:hover:before:opacity-60;
}

[data-vc-theme='dark'] .vc-header__content {
  @apply text-[var(--vc-header-color,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-month,
[data-vc-theme='dark'] .vc-year {
  @apply text-[var(--vc-title-color,theme(colors.white))] surehover:hover:text-[var(--vc-title-color-hover,theme(colors.slate.500))] disabled:text-[var(--vc-title-color-disabled,theme(colors.slate.700))] disabled:opacity-80;
}

[data-vc-theme='dark'] .vc-months__month,
[data-vc-theme='dark'] .vc-years__year {
  @apply bg-[var(--vc-months-years-bg,theme(colors.slate.900))] text-[var(--vc-months-years-color,theme(colors.white))] surehover:hover:bg-[var(--vc-months-years-bg-hover,theme(colors.slate.800))] disabled:text-[var(--vc-months-years-color-disabled,theme(colors.slate.700))] disabled:opacity-80 disabled:surehover:hover:text-[var(--vc-months-years-color-disabled,theme(colors.slate.700))];
}

[data-vc-theme='dark'] .vc-months__month[data-vc-months-month-selected],
[data-vc-theme='dark'] .vc-years__year[data-vc-years-year-selected] {
  @apply bg-[var(--vc-months-years-bg-selected,theme(colors.slate.500))] text-[var(--vc-months-years-color-selected,theme(colors.white))] surehover:hover:bg-[var(--vc-months-years-bg-selected,theme(colors.slate.500))] surehover:hover:text-[var(--vc-months-years-color-selected,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-collapse {
  @apply before:bg-[var(--vc-collapse-color,theme(colors.slate.600))]
	surehover:before:bg-transparent surehover:before:bg-dark-collapse surehover:hover:before:opacity-60;
}

[data-vc-theme='dark'] .vc-week-numbers__title {
  @apply text-[var(--vc-week-numbers-title-color,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-week-number {
  @apply text-[var(--vc-week-number-color,theme(colors.white))] surehover:hover:text-[var(--vc-week-number-color-hover,theme(colors.slate.300))];
}

[data-vc-theme='dark'] .vc-week__day {
  @apply text-[var(--vc-week-day-color,theme(colors.white))];
}

[data-vc-theme='dark'] button.vc-week__day {
  @apply surehover:hover:text-[var(--vc-week-day-color-hover,theme(colors.slate.300))];
}

[data-vc-theme='dark'] .vc-week__day[data-vc-week-day-off] {
  @apply text-[var(--vc-week-day-off-color,theme(colors.rose.500))];
}

[data-vc-theme='dark'] button.vc-week__day[data-vc-week-day-off] {
  @apply surehover:hover:text-[var(--vc-week-day-off-color-hover,theme(colors.rose.600))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-weekend-bg,rgb(244_63_94_/_0.8))] text-[var(--vc-date-range-middle-weekend-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-range-middle-weekend-bg,rgb(244_63_94_/_0.8))] surehover:hover:text-[var(--vc-date-range-middle-weekend-color,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.800))] text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.300))] surehover:hover:bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.800))] surehover:hover:text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.300))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-bg,rgb(6_182_212_/_0.8))] text-[var(--vc-date-range-middle-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-range-middle-bg,rgb(6_182_212_/_0.8))] surehover:hover:text-[var(--vc-date-range-middle-color,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-selected='middle'][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.800))] text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.300))] surehover:hover:bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.800))] surehover:hover:text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.300))];
}

[data-vc-theme='dark'] .vc-date__btn {
  @apply text-[var(--vc-date-color,theme(colors.slate.400))] bg-[var(--vc-date-bg,theme(colors.slate.900))] surehover:hover:bg-[var(--vc-date-bg-hover,theme(colors.slate.800))] surehover:hover:text-[var(--vc-date-color-hover,theme(colors.slate.200))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-today] .vc-date__btn {
  @apply text-[var(--vc-date-today-color,theme(colors.cyan.500))] surehover:hover:text-[var(--vc-date-today-color,theme(colors.cyan.500))] bg-[var(--vc-date-today-bg,theme(colors.slate.800))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-today][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-today-outside-color,theme(colors.slate.600))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-outside-color,theme(colors.slate.600))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-disabled-color,theme(colors.slate.700))] opacity-80;
}

[data-vc-theme='dark'] .vc-date[data-vc-date-hover] .vc-date__btn {
  @apply bg-[var(--vc-date-hover-bg,theme(colors.slate.800))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-hover='first'] .vc-date__btn {
  @apply bg-[var(--vc-date-hover-edge-bg,theme(colors.slate.700))] surehover:hover:bg-[var(--vc-date-hover-edge-bg,theme(colors.slate.700))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-color,theme(colors.rose.500))] surehover:hover:bg-[var(--vc-date-weekend-bg-hover,theme(colors.slate.800))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-hover] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-hover] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-hover-bg,theme(colors.slate.800))] text-[var(--vc-date-weekend-color,theme(colors.rose.500))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-hover='first'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-hover='first'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-hover-edge-bg,theme(colors.slate.700))] surehover:hover:bg-[var(--vc-date-weekend-hover-edge-bg,theme(colors.slate.700))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-disabled] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-disabled-color,theme(colors.slate.700))] opacity-80;
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-today] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-today] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-color,theme(colors.rose.500))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-disabled] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-disabled-color,theme(colors.slate.700))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-outside-bg,theme(colors.slate.900))] text-[var(--vc-date-weekend-outside-color,theme(colors.slate.600))] surehover:hover:bg-[var(--vc-date-weekend-outside-bg-hover,theme(colors.slate.800))] surehover:hover:text-[var(--vc-date-weekend-outside-color-hover,theme(colors.slate.300))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-hover][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-hover][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-hover][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-hover][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-outside-hover-bg,theme(colors.slate.800))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-outside-color,theme(colors.slate.400))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-disabled][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-disabled][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-disabled][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-disabled][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-disabled-outside-color,theme(colors.slate.700))] opacity-80;
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-selected-bg,theme(colors.rose.500))] text-[var(--vc-date-weekend-selected-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-weekend-selected-bg,theme(colors.rose.500))] surehover:hover:text-[var(--vc-date-weekend-selected-color,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-weekend][data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-holiday][data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.700))] text-[var(--vc-date-selected-outside-color,theme(colors.slate.300))] surehover:hover:bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.700))] surehover:hover:text-[var(--vc-date-selected-outside-color,theme(colors.slate.300))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-bg,theme(colors.cyan.500))] text-[var(--vc-date-selected-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-selected-bg,theme(colors.cyan.500))] surehover:hover:text-[var(--vc-date-selected-color,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-date[data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='dark'] .vc-date[data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.700))] text-[var(--vc-date-selected-outside-color,theme(colors.slate.300))] surehover:hover:bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.700))] surehover:hover:text-[var(--vc-date-selected-outside-color,theme(colors.slate.300))];
}

[data-vc-theme='dark'] .vc-date__popup {
  @apply text-[var(--vc-date-popup-color,theme(colors.white))] bg-[var(--vc-date-popup-bg,theme(colors.slate.800))] shadow-[inset_0_0_0_1px_rgb(255_255_255_/_0.05)];
}

[data-vc-theme='dark'] .vc-date-range-tooltip {
  @apply text-[var(--vc-date-range-tooltip-color,theme(colors.slate.400))] bg-[var(--vc-date-range-tooltip-bg,theme(colors.slate.800))] shadow-[inset_0_0_0_1px_rgb(255_255_255_/_0.05)];
}

[data-vc-theme='dark'] .vc-time {
  @apply border-[var(--vc-time-border-color,theme(colors.slate.800))];
}

[data-vc-theme='dark'] .vc-time__hour,
[data-vc-theme='dark'] .vc-time__minute {
  @apply after:text-[var(--vc-time-separator-color,theme(colors.white))];
}

[data-vc-theme='dark'] .vc-time__hour input,
[data-vc-theme='dark'] .vc-time__minute input {
  @apply text-[var(--vc-time-input-color,theme(colors.white))] bg-[var(--vc-time-input-bg,theme(colors.slate.900))] surehover:hover:bg-[var(--vc-time-input-bg-hover,theme(colors.slate.700))] focus-visible:outline-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='dark'] .vc-time__hour input[data-vc-input-focus],
[data-vc-theme='dark'] .vc-time__minute input[data-vc-input-focus] {
  @apply bg-[var(--vc-time-input-bg-hover,theme(colors.slate.700))];
}

[data-vc-theme='dark'] .vc-time__keeping {
  @apply text-[var(--vc-time-keeping-color,theme(colors.slate.500))] surehover:hover:bg-[var(--vc-time-input-bg-hover,theme(colors.slate.700))] surehover:hover:text-[var(--vc-time-keeping-color-hover,theme(colors.slate.400))] focus-visible:outline-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='dark'] .vc-time__range input {
  @apply bg-[var(--vc-time-range-bg,theme(colors.slate.900))];
}

[data-vc-theme='dark'] .vc-time__range::before,
[data-vc-theme='dark'] .vc-time__range::after {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.600))];
}

[data-vc-theme='dark'] .vc-time__range:hover input::-webkit-slider-thumb {
  @apply border-[var(--vc-time-range-thumb-border-hover,theme(colors.slate.400))];
}

[data-vc-theme='dark'] .vc-time__range:hover input::-moz-range-thumb {
  @apply border-[var(--vc-time-range-thumb-border-hover,theme(colors.slate.400))];
}

[data-vc-theme='dark'] .vc-time__range input:focus-visible::-webkit-slider-thumb {
  @apply border-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='dark'] .vc-time__range input:focus-visible::-moz-range-thumb {
  @apply border-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='dark'] .vc-time__range input::-webkit-slider-thumb {
  @apply border-[var(--vc-time-range-thumb-border,theme(colors.slate.600))] bg-[var(--vc-time-range-thumb-bg,theme(colors.slate.800))];
}

[data-vc-theme='dark'] .vc-time__range input::-moz-range-thumb {
  @apply border-[var(--vc-time-range-thumb-border,theme(colors.slate.600))] bg-[var(--vc-time-range-thumb-bg,theme(colors.slate.800))];
}

[data-vc-theme='dark'] .vc-time__range input::-webkit-slider-runnable-track {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.600))];
}

[data-vc-theme='dark'] .vc-time__range input::-moz-range-track {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.600))];
}

```

### `package/src/styles/themes/light.css`

```css
[data-vc-theme='light'].vc {
  @apply bg-[var(--vc-bg,theme(colors.white))] text-[var(--vc-color,theme(colors.slate.900))];
}

[data-vc-theme='light'].vc[data-vc-input] {
  @apply shadow-[0_9px_20px_rgba(0,0,0,.1)];
}

[data-vc-theme='light'].vc:focus-visible,
[data-vc-theme='light'].vc button:focus-visible,
[data-vc-theme='light'].vc [tabindex='0']:focus-visible {
  @apply outline-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='light'] .vc-arrow {
  @apply bg-transparent before:bg-light-arrow surehover:hover:before:opacity-60;
}

[data-vc-theme='light'] .vc-header__content {
  @apply text-[var(--vc-header-color,theme(colors.slate.900))];
}

[data-vc-theme='light'] .vc-month,
[data-vc-theme='light'] .vc-year {
  @apply text-[var(--vc-title-color,theme(colors.slate.900))] surehover:hover:text-[var(--vc-title-color-hover,theme(colors.slate.500))] disabled:text-[var(--vc-title-color-disabled,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-months__month,
[data-vc-theme='light'] .vc-years__year {
  @apply bg-[var(--vc-months-years-bg,theme(colors.white))] text-[var(--vc-months-years-color,theme(colors.slate.500))] surehover:hover:bg-[var(--vc-months-years-bg-hover,theme(colors.slate.100))] disabled:text-[var(--vc-months-years-color-disabled,theme(colors.slate.300))] disabled:surehover:hover:text-[var(--vc-months-years-color-disabled,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-months__month[data-vc-months-month-selected],
[data-vc-theme='light'] .vc-years__year[data-vc-years-year-selected] {
  @apply bg-[var(--vc-months-years-bg-selected,theme(colors.cyan.500))] text-[var(--vc-months-years-color-selected,theme(colors.white))] surehover:hover:bg-[var(--vc-months-years-bg-selected,theme(colors.cyan.500))] surehover:hover:text-[var(--vc-months-years-color-selected,theme(colors.white))];
}

[data-vc-theme='light'] .vc-collapse {
  @apply before:bg-[var(--vc-collapse-color,theme(colors.slate.300))]
	surehover:before:bg-transparent surehover:before:bg-light-collapse surehover:hover:before:opacity-60;
}

[data-vc-theme='light'] .vc-week-numbers__title {
  @apply text-[var(--vc-week-numbers-title-color,theme(colors.slate.500))];
}

[data-vc-theme='light'] .vc-week-number {
  @apply text-[var(--vc-week-number-color,theme(colors.slate.500))] surehover:hover:text-[var(--vc-week-number-color-hover,theme(colors.slate.600))];
}

[data-vc-theme='light'] .vc-week__day {
  @apply text-[var(--vc-week-day-color,theme(colors.slate.500))];
}

[data-vc-theme='light'] button.vc-week__day {
  @apply surehover:hover:text-[var(--vc-week-day-color-hover,theme(colors.slate.600))];
}

[data-vc-theme='light'] .vc-week__day[data-vc-week-day-off] {
  @apply text-[var(--vc-week-day-off-color,theme(colors.rose.500))];
}

[data-vc-theme='light'] button.vc-week__day[data-vc-week-day-off] {
  @apply surehover:hover:text-[var(--vc-week-day-off-color-hover,theme(colors.rose.600))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-weekend-bg,rgb(244_63_94_/_0.7))] text-[var(--vc-date-range-middle-weekend-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-range-middle-weekend-bg,rgb(244_63_94_/_0.7))] surehover:hover:text-[var(--vc-date-range-middle-weekend-color,theme(colors.white))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.500))] surehover:hover:bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] surehover:hover:text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.500))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-bg,rgb(6_182_212_/_0.7))] text-[var(--vc-date-range-middle-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-range-middle-bg,rgb(6_182_212_/_0.7))] surehover:hover:text-[var(--vc-date-range-middle-color,theme(colors.white))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.500))] surehover:hover:bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] surehover:hover:text-[var(--vc-date-range-middle-outside-color,theme(colors.slate.500))];
}

[data-vc-theme='light'] .vc-date__btn {
  @apply text-[var(--vc-date-color,theme(colors.slate.900))] bg-[var(--vc-date-bg,theme(colors.white))] surehover:hover:bg-[var(--vc-date-bg-hover,theme(colors.slate.100))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-today] .vc-date__btn {
  @apply text-[var(--vc-date-today-color,theme(colors.cyan.500))] surehover:hover:text-[var(--vc-date-today-color,theme(colors.cyan.500))] bg-[var(--vc-date-today-bg,theme(colors.slate.100))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-today][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-today-outside-color,theme(colors.slate.500))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-outside-color,theme(colors.slate.400))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-disabled-color,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-hover] .vc-date__btn {
  @apply bg-[var(--vc-date-hover-bg,theme(colors.slate.100))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-hover='first'] .vc-date__btn {
  @apply bg-[var(--vc-date-hover-edge-bg,theme(colors.slate.200))] surehover:hover:bg-[var(--vc-date-hover-edge-bg,theme(colors.slate.200))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-color,theme(colors.rose.500))] surehover:hover:bg-[var(--vc-date-weekend-bg-hover,theme(colors.rose.50))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-hover] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-hover] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-hover-bg,theme(colors.rose.50))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-hover='first'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-hover='first'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-hover-edge-bg,theme(colors.rose.100))] surehover:hover:bg-[var(--vc-date-weekend-hover-edge-bg,theme(colors.rose.100))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-disabled] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-disabled-color,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-today] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-today] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-color,theme(colors.rose.500))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-disabled] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-disabled-color,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-outside-bg,theme(colors.white))] text-[var(--vc-date-weekend-outside-color,theme(colors.slate.400))] surehover:hover:bg-[var(--vc-date-weekend-outside-bg-hover,theme(colors.slate.100))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-hover][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-hover][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-hover][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-hover][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-outside-hover-bg,theme(colors.slate.100))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-outside-color,theme(colors.slate.400))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-disabled][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-disabled][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-disabled][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-disabled][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-disabled-outside-color,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-selected-bg,theme(colors.rose.500))] text-[var(--vc-date-weekend-selected-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-weekend-selected-bg,theme(colors.rose.500))] surehover:hover:text-[var(--vc-date-weekend-selected-color,theme(colors.white))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-weekend][data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-holiday][data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] text-[var(--vc-date-selected-outside-color,theme(colors.slate.500))] surehover:hover:bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] surehover:hover:text-[var(--vc-date-selected-outside-color,theme(colors.slate.500))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-bg,theme(colors.cyan.500))] text-[var(--vc-date-selected-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-selected-bg,theme(colors.cyan.500))] surehover:hover:text-[var(--vc-date-selected-color,theme(colors.white))];
}

[data-vc-theme='light'] .vc-date[data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='light'] .vc-date[data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] text-[var(--vc-date-selected-outside-color,theme(colors.slate.500))] surehover:hover:bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] surehover:hover:text-[var(--vc-date-selected-outside-color,theme(colors.slate.500))];
}

[data-vc-theme='light'] .vc-date__popup {
  @apply text-[var(--vc-date-popup-color,theme(colors.slate.900))] bg-[var(--vc-date-popup-bg,theme(colors.white))] shadow-[0_3px_15px_rgba(85,_85,_85,_0.2)];
}

[data-vc-theme='light'] .vc-date-range-tooltip {
  @apply text-[var(--vc-date-range-tooltip-color,theme(colors.slate.500))] bg-[var(--vc-date-range-tooltip-bg,theme(colors.slate.50))] shadow-[0px_1px_4px_rgba(85,85,85,0.2)];
}

[data-vc-theme='light'] .vc-time {
  @apply border-[var(--vc-time-border-color,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-time__hour,
[data-vc-theme='light'] .vc-time__minute {
  @apply after:text-[var(--vc-time-separator-color,theme(colors.slate.900))];
}

[data-vc-theme='light'] .vc-time__hour input,
[data-vc-theme='light'] .vc-time__minute input {
  @apply text-[var(--vc-time-input-color,theme(colors.slate.900))] bg-[var(--vc-time-input-bg,theme(colors.white))] surehover:hover:bg-[var(--vc-time-input-bg-hover,theme(colors.orange.100))] focus-visible:outline-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='light'] .vc-time__hour input[data-vc-input-focus],
[data-vc-theme='light'] .vc-time__minute input[data-vc-input-focus] {
  @apply bg-[var(--vc-time-input-bg-hover,theme(colors.orange.100))];
}

[data-vc-theme='light'] .vc-time__keeping {
  @apply text-[var(--vc-time-keeping-color,theme(colors.slate.500))] surehover:hover:bg-[var(--vc-time-input-bg-hover,theme(colors.orange.100))] focus-visible:outline-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='light'] .vc-time__range input {
  @apply bg-[var(--vc-time-range-bg,theme(colors.white))];
}

[data-vc-theme='light'] .vc-time__range::before,
[data-vc-theme='light'] .vc-time__range::after {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-time__range:hover input::-webkit-slider-thumb {
  @apply border-[var(--vc-time-range-thumb-border-hover,theme(colors.slate.400))];
}

[data-vc-theme='light'] .vc-time__range:hover input::-moz-range-thumb {
  @apply border-[var(--vc-time-range-thumb-border-hover,theme(colors.slate.400))];
}

[data-vc-theme='light'] .vc-time__range input:focus-visible::-webkit-slider-thumb {
  @apply border-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='light'] .vc-time__range input:focus-visible::-moz-range-thumb {
  @apply border-[var(--vc-focus-outline-color,theme(colors.orange.300))];
}

[data-vc-theme='light'] .vc-time__range input::-webkit-slider-thumb {
  @apply border-[var(--vc-time-range-thumb-border,theme(colors.slate.300))] bg-[var(--vc-time-range-thumb-bg,theme(colors.white))];
}

[data-vc-theme='light'] .vc-time__range input::-moz-range-thumb {
  @apply border-[var(--vc-time-range-thumb-border,theme(colors.slate.300))] bg-[var(--vc-time-range-thumb-bg,theme(colors.white))];
}

[data-vc-theme='light'] .vc-time__range input::-webkit-slider-runnable-track {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.300))];
}

[data-vc-theme='light'] .vc-time__range input::-moz-range-track {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.300))];
}

```

### `package/src/styles/themes/slate-light.css`

```css
[data-vc-theme='slate-light'].vc {
  @apply bg-[var(--vc-bg,theme(colors.slate.100))] text-[var(--vc-color,theme(colors.gray.800))];
}

[data-vc-theme='slate-light'].vc_to-input {
  @apply shadow-[0_9px_20px_rgba(0,0,0,.05)];
}

[data-vc-theme='slate-light'].vc:focus-visible,
[data-vc-theme='slate-light'].vc button:focus-visible,
[data-vc-theme='slate-light'].vc [tabindex='0']:focus-visible {
  @apply outline-[var(--vc-focus-outline-color,theme(colors.blue.300))];
}

[data-vc-theme='slate-light'] .vc-arrow {
  @apply bg-transparent before:bg-light-arrow surehover:hover:before:opacity-60;
}

[data-vc-theme='slate-light'] .vc-header__content {
  @apply text-[var(--vc-header-color,theme(colors.gray.800))];
}

[data-vc-theme='slate-light'] .vc-month,
[data-vc-theme='slate-light'] .vc-year {
  @apply text-[var(--vc-title-color,theme(colors.gray.800))] surehover:hover:text-[var(--vc-title-color-hover,theme(colors.gray.600))] disabled:text-[var(--vc-title-color-disabled,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-months__month,
[data-vc-theme='slate-light'] .vc-years__year {
  @apply bg-[var(--vc-months-years-bg,theme(colors.slate.100))] text-[var(--vc-months-years-color,theme(colors.gray.600))] surehover:hover:bg-[var(--vc-months-years-bg-hover,theme(colors.slate.200))] disabled:text-[var(--vc-months-years-color-disabled,theme(colors.gray.400))] disabled:surehover:hover:text-[var(--vc-months-years-color-disabled,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-months__month[data-vc-months-month-selected],
[data-vc-theme='slate-light'] .vc-years__year[data-vc-years-year-selected] {
  @apply bg-[var(--vc-months-years-bg-selected,theme(colors.blue.500))] text-[var(--vc-months-years-color-selected,theme(colors.white))] surehover:hover:bg-[var(--vc-months-years-bg-selected,theme(colors.blue.500))] surehover:hover:text-[var(--vc-months-years-color-selected,theme(colors.white))];
}

[data-vc-theme='slate-light'] .vc-collapse {
  @apply before:bg-[var(--vc-collapse-color,theme(colors.slate.300))]
	surehover:before:bg-transparent surehover:before:bg-light-collapse surehover:hover:before:opacity-60;
}

[data-vc-theme='slate-light'] .vc-week-numbers__title {
  @apply text-[var(--vc-week-numbers-title-color,theme(colors.gray.600))];
}

[data-vc-theme='slate-light'] .vc-week-number {
  @apply text-[var(--vc-week-number-color,theme(colors.gray.600))] surehover:hover:text-[var(--vc-week-number-color-hover,theme(colors.gray.800))];
}

[data-vc-theme='slate-light'] .vc-week__day {
  @apply text-[var(--vc-week-day-color,theme(colors.gray.600))];
}

[data-vc-theme='slate-light'] button.vc-week__day {
  @apply surehover:hover:text-[var(--vc-week-day-color-hover,theme(colors.gray.800))];
}

[data-vc-theme='slate-light'] .vc-week__day[data-vc-week-day-off] {
  @apply text-[var(--vc-week-day-off-color,theme(colors.red.500))];
}

[data-vc-theme='slate-light'] button.vc-week__day[data-vc-week-day-off] {
  @apply surehover:hover:text-[var(--vc-week-day-off-color-hover,theme(colors.red.600))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-weekend-bg,rgb(239_68_68_/_0.8))] text-[var(--vc-date-range-middle-weekend-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-range-middle-weekend-bg,rgb(239_68_68_/_0.8))] surehover:hover:text-[var(--vc-date-range-middle-weekend-color,theme(colors.white))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-weekend][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-holiday][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] text-[var(--vc-date-range-middle-outside-color,theme(colors.gray.600))] surehover:hover:bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] surehover:hover:text-[var(--vc-date-range-middle-outside-color,theme(colors.gray.600))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-bg,rgb(59_130_246_/_0.8))] text-[var(--vc-date-range-middle-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-range-middle-bg,rgb(59_130_246_/_0.8))] surehover:hover:text-[var(--vc-date-range-middle-color,theme(colors.white))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-month='prev'][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected='middle'][data-vc-date-month='next'][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] text-[var(--vc-date-range-middle-outside-color,theme(colors.gray.600))] surehover:hover:bg-[var(--vc-date-range-middle-outside-bg,theme(colors.slate.200))] surehover:hover:text-[var(--vc-date-range-middle-outside-color,theme(colors.gray.600))];
}

[data-vc-theme='slate-light'] .vc-date__btn {
  @apply text-[var(--vc-date-color,theme(colors.gray.800))] bg-[var(--vc-date-bg,theme(colors.slate.100))] surehover:hover:bg-[var(--vc-date-bg-hover,theme(colors.slate.200))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-today] .vc-date__btn {
  @apply text-[var(--vc-date-today-color,theme(colors.blue.500))] surehover:hover:text-[var(--vc-date-today-color,theme(colors.blue.500))] bg-[var(--vc-date-today-bg,theme(colors.slate.200))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-today][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-today-outside-color,theme(colors.gray.600))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-outside-color,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-disabled-color,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-hover] .vc-date__btn {
  @apply bg-[var(--vc-date-hover-bg,theme(colors.slate.200))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-hover='first'] .vc-date__btn {
  @apply bg-[var(--vc-date-hover-edge-bg,theme(colors.slate.300))] surehover:hover:bg-[var(--vc-date-hover-edge-bg,theme(colors.slate.300))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-color,theme(colors.red.500))] surehover:hover:bg-[var(--vc-date-weekend-bg-hover,theme(colors.slate.200))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-hover] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-hover] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-hover-bg,theme(colors.slate.200))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-hover='last'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-hover='first'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-hover='first'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-hover-edge-bg,theme(colors.slate.300))] surehover:hover:bg-[var(--vc-date-weekend-hover-edge-bg,theme(colors.slate.300))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-disabled] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-disabled-color,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-today] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-today] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-color,theme(colors.red.500))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-disabled] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-disabled] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-disabled-color,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-outside-bg,theme(colors.slate.100))] text-[var(--vc-date-weekend-outside-color,theme(colors.gray.400))] surehover:hover:bg-[var(--vc-date-weekend-outside-bg-hover,theme(colors.slate.200))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-hover][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-hover][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-hover][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-hover][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-outside-hover-bg,theme(colors.slate.200))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-today][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-today][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-today-outside-color,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-disabled][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-disabled][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-disabled][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-disabled][data-vc-date-month='next'] .vc-date__btn {
  @apply text-[var(--vc-date-weekend-disabled-outside-color,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-selected] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-weekend-selected-bg,theme(colors.red.500))] text-[var(--vc-date-weekend-selected-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-weekend-selected-bg,theme(colors.red.500))] surehover:hover:text-[var(--vc-date-weekend-selected-color,theme(colors.white))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-weekend][data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-holiday][data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] text-[var(--vc-date-selected-outside-color,theme(colors.gray.600))] surehover:hover:bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] surehover:hover:text-[var(--vc-date-selected-outside-color,theme(colors.gray.600))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-bg,theme(colors.blue.500))] text-[var(--vc-date-selected-color,theme(colors.white))] surehover:hover:bg-[var(--vc-date-selected-bg,theme(colors.blue.500))] surehover:hover:text-[var(--vc-date-selected-color,theme(colors.white))];
}

[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected][data-vc-date-month='prev'] .vc-date__btn,
[data-vc-theme='slate-light'] .vc-date[data-vc-date-selected][data-vc-date-month='next'] .vc-date__btn {
  @apply bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] text-[var(--vc-date-selected-outside-color,theme(colors.gray.600))] surehover:hover:bg-[var(--vc-date-selected-outside-bg,theme(colors.slate.300))] surehover:hover:text-[var(--vc-date-selected-outside-color,theme(colors.gray.600))];
}

[data-vc-theme='slate-light'] .vc-date__popup {
  @apply text-[var(--vc-date-popup-color,theme(colors.gray.800))] bg-[var(--vc-date-popup-bg,theme(colors.white))] shadow-[0_3px_15px_rgba(85,_85,_85,_0.1)];
}

[data-vc-theme='slate-light'] .vc-date-range-tooltip {
  @apply text-[var(--vc-date-range-tooltip-color,theme(colors.slate.500))] bg-[var(--vc-date-range-tooltip-bg,theme(colors.slate.50))] shadow-[0px_1px_4px_rgba(85,85,85,0.2)];
}

[data-vc-theme='slate-light'] .vc-time {
  @apply border-[var(--vc-time-border-color,theme(colors.gray.300))];
}

[data-vc-theme='slate-light'] .vc-time__hour,
[data-vc-theme='slate-light'] .vc-time__minute {
  @apply after:text-[var(--vc-time-separator-color,theme(colors.gray.800))];
}

[data-vc-theme='slate-light'] .vc-time__hour input,
[data-vc-theme='slate-light'] .vc-time__minute input {
  @apply text-[var(--vc-time-input-color,theme(colors.gray.800))] bg-[var(--vc-time-input-bg,theme(colors.slate.100))] surehover:hover:bg-[var(--vc-time-input-bg-hover,theme(colors.blue.100))] focus-visible:outline-[var(--vc-focus-outline-color,theme(colors.blue.300))];
}

[data-vc-theme='slate-light'] .vc-time__hour input[data-vc-input-focus],
[data-vc-theme='slate-light'] .vc-time__minute input[data-vc-input-focus] {
  @apply bg-[var(--vc-time-input-bg-hover,theme(colors.blue.100))];
}

[data-vc-theme='slate-light'] .vc-time__keeping {
  @apply text-[var(--vc-time-keeping-color,theme(colors.gray.600))] surehover:hover:bg-[var(--vc-time-input-bg-hover,theme(colors.blue.100))] focus-visible:outline-[var(--vc-focus-outline-color,theme(colors.blue.300))];
}

[data-vc-theme='slate-light'] .vc-time__range input {
  @apply bg-[var(--vc-time-range-bg,theme(colors.slate.100))];
}

[data-vc-theme='slate-light'] .vc-time__range::before,
[data-vc-theme='slate-light'] .vc-time__range::after {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.300))];
}

[data-vc-theme='slate-light'] .vc-time__range:hover input::-webkit-slider-thumb {
  @apply border-[var(--vc-time-range-thumb-border-hover,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-time__range:hover input::-moz-range-thumb {
  @apply border-[var(--vc-time-range-thumb-border-hover,theme(colors.gray.400))];
}

[data-vc-theme='slate-light'] .vc-time__range input:focus-visible::-webkit-slider-thumb {
  @apply border-[var(--vc-focus-outline-color,theme(colors.blue.300))];
}

[data-vc-theme='slate-light'] .vc-time__range input:focus-visible::-moz-range-thumb {
  @apply border-[var(--vc-focus-outline-color,theme(colors.blue.300))];
}

[data-vc-theme='slate-light'] .vc-time__range input::-webkit-slider-thumb {
  @apply border-[var(--vc-time-range-thumb-border,theme(colors.gray.300))] bg-[var(--vc-time-range-thumb-bg,theme(colors.slate.100))];
}

[data-vc-theme='slate-light'] .vc-time__range input::-moz-range-thumb {
  @apply border-[var(--vc-time-range-thumb-border,theme(colors.gray.300))] bg-[var(--vc-time-range-thumb-bg,theme(colors.slate.100))];
}

[data-vc-theme='slate-light'] .vc-time__range input::-webkit-slider-runnable-track {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.300))];
}

[data-vc-theme='slate-light'] .vc-time__range input::-moz-range-track {
  @apply bg-[var(--vc-time-range-track-color,theme(colors.slate.300))];
}

```

### `package/src/types.ts`

```ts
import type { Calendar } from '@src/index';
import type labels from '@src/labels';
import type options from '@src/options';
import type styles from '@src/styles';

type LeadingZero = `0${number}`;

type MM = LeadingZero | 10 | 11 | 12;

type DD = LeadingZero | `${1 | 2}${number}` | 30 | 31;

export type FormatDateString = `${number}-${MM}-${DD}`;

export type MonthsCount = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12;

export type Positions = 'bottom' | 'top' | 'center' | 'left' | 'right';

export type YPosition = 'bottom' | 'top';

export type XPosition = 'left' | 'center' | 'right';

export type PositionToInput = 'auto' | XPosition | [YPosition, XPosition];

export type Range<N extends number, Acc extends number[] = []> = Acc['length'] extends N ? Acc[number] : Range<N, [...Acc, Acc['length']]>;

export type ToggleSelected = boolean | ((self: Calendar) => boolean);

export type TypesCalendar = 'default' | 'multiple' | 'month' | 'year' | 'week';

export type DateMode = 'single' | 'multiple' | 'multiple-ranged';

export type DateAny = Date | number | FormatDateString | 'today';

export type DatesArr = Array<Date | number | string>;

export type TimeControl = 'all' | 'range';

export type AnimationTiming = {
  duration?: number;
  easing?: string;
};

// Nested values win over the ones set at the top level.
export type AnimationOptions = AnimationTiming & {
  slide?: AnimationTiming;
  fade?: AnimationTiming;
  collapse?: AnimationTiming;
};

export type TimePicker = 'AM' | 'PM';

export type ThemesDefault = 'light' | 'dark' | 'system';

export type WeekDayID = 0 | 1 | 2 | 3 | 4 | 5 | 6;

export type WeekDays<T> = [...T[]];

export type LocaleStated = {
  months: {
    long: string[];
    short: string[];
  };
  weekdays: {
    long: string[];
    short: string[];
  };
};

export type Locale = string | LocaleStated;

export type Popup = {
  modifier?: string;
  html?: string;
};

export type PopupDateKey = FormatDateString | `${FormatDateString}:${FormatDateString}`;

export type Popups = {
  [date in PopupDateKey]: Popup;
};

export type HtmlElementPosition = {
  top: number;
  bottom: number;
  left: number;
  right: number;
};

export type Reset = {
  year: boolean;
  month: boolean;
  dates: boolean | 'only-first';
  time: boolean;
  locale: boolean;
};

export type ContextVariables = {
  isInit: boolean;
  isDestroyed: boolean;
  isShowInInputMode: boolean;
  inputModeInit: boolean;
  openOnFocus: ToggleSelected;
  cleanupHandlers: Array<() => void>;
  cleanupSystemTheme?: () => void;
  currentType: TypesCalendar;
  locale: LocaleStated;
  mainElement: HTMLElement;
  originalElement: HTMLElement;
  inputElement?: HTMLInputElement;
  dateToday: FormatDateString;
  dateMin: FormatDateString;
  dateMax: FormatDateString;
  displayDateMin: FormatDateString;
  displayDateMax: FormatDateString;
  displayYear: number;
  displayWeekDate: FormatDateString;
  displayMonthsCount: MonthsCount;
  disableDates: FormatDateString[];
  enableDates: FormatDateString[];
  selectedDates: FormatDateString[];
  selectedMonth: Range<12>;
  selectedYear: number;
  selectedHours: string;
  selectedMinutes: string;
  selectedKeeping: TimePicker | null;
  selectedTime: string;
};

export type Styles = typeof styles;

export type Labels = typeof labels;

export type LabelsOptions = Partial<Omit<Labels, 'arrowNext' | 'arrowPrev'>> & {
  arrowNext?: Partial<Labels['arrowNext']>;
  arrowPrev?: Partial<Labels['arrowPrev']>;
};

export type Layouts = {
  default: string;
  multiple: string;
  month: string;
  year: string;
  week: string;
};

export type Options = Omit<Partial<options>, 'popups' | 'labels' | 'layouts' | 'styles'> & {
  popups?: Partial<Popups>;
  labels?: LabelsOptions;
  layouts?: Partial<Layouts>;
  styles?: Partial<Styles>;
};

```

### `package/src/utils/index.ts`

```ts
import getDateOriginal from '@scripts/utils/getDate';
import getDateStringOriginal from '@scripts/utils/getDateString';
import getWeekNumberOriginal from '@scripts/utils/getWeekNumber';
import parseDatesOriginal from '@scripts/utils/parseDates';
import type { FormatDateString, WeekDayID } from '@src/types';

export const parseDates = (dates: string[]) => parseDatesOriginal(dates);

export const getDateString = (date: Date) => getDateStringOriginal(date);

export const getDate = (date: FormatDateString) => getDateOriginal(date);

export const getWeekNumber = (date: FormatDateString, weekStartDay: WeekDayID) => getWeekNumberOriginal(date, weekStartDay);

```

### `postcss.config.js`

```js
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};

```

### `README.md`

```md
package/public/README.md
```

### `tailwind.config.js`

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./demo/**/*.{html,css}', './src/**/*.{js,ts}'],
  theme: {
    extend: {
      screens: {
        surehover: { raw: '(hover: hover) and (pointer: fine)' },
      },
      backgroundImage: {
        'light-arrow':
          'url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAyNCAyNCc+PHBhdGggZmlsbD0nIzBmMTcyYScgZD0nTTEyIDE2Yy0uMyAwLS41LS4xLS43LS4zbC02LTZjLS40LS40LS40LTEgMC0xLjRzMS0uNCAxLjQgMGw1LjMgNS4zIDUuMy01LjNjLjQtLjQgMS0uNCAxLjQgMHMuNCAxIDAgMS40bC02IDZjLS4yLjItLjQuMy0uNy4zeicvPjwvc3ZnPg==")',
        'dark-arrow':
          'url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCAyNCAyNCc+PHBhdGggZmlsbD0nI2ZmZicgZD0nTTEyIDE2Yy0uMyAwLS41LS4xLS43LS4zbC02LTZjLS40LS40LS40LTEgMC0xLjRzMS0uNCAxLjQgMGw1LjMgNS4zIDUuMy01LjNjLjQtLjQgMS0uNCAxLjQgMHMuNCAxIDAgMS40bC02IDZjLS4yLjItLjQuMy0uNy4zeicvPjwvc3ZnPg==")',
        'light-collapse':
          'url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iIzBmMTcyYSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMS44NjcgNi4wOTdhLjc1Ljc1IDAgMCAxIDEuMDM2LS4yM0w4IDkuMTExbDUuMDk3LTMuMjQ0YS43NS43NSAwIDAgMSAuODA2IDEuMjY2bC01LjUgMy41YS43NS43NSAwIDAgMS0uODA2IDBsLTUuNS0zLjVhLjc1Ljc1IDAgMCAxLS4yMy0xLjAzNiIgY2xpcC1ydWxlPSJldmVub2RkIi8+PC9zdmc+")',
        'dark-collapse':
          'url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbD0iI2ZmZiIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMS44NjcgNi4wOTdhLjc1Ljc1IDAgMCAxIDEuMDM2LS4yM0w4IDkuMTExbDUuMDk3LTMuMjQ0YS43NS43NSAwIDAgMSAuODA2IDEuMjY2bC01LjUgMy41YS43NS43NSAwIDAgMS0uODA2IDBsLTUuNS0zLjVhLjc1Ljc1IDAgMCAxLS4yMy0xLjAzNiIgY2xpcC1ydWxlPSJldmVub2RkIi8+PC9zdmc+")',
        'light-mode': 'linear-gradient(145deg, rgb(6 182 212 / 4%) 12%, rgb(6 182 212 / 10%) 42%, rgb(6 182 212 / 5%) 60%, rgb(6 182 212 / 18%) 85%)',
        'dark-mode': 'linear-gradient(145deg, rgb(6 182 212 / 0%) 12%, rgb(6 182 212 / 3%) 42%, rgb(6 182 212 / 10%) 60%, rgb(6 182 212 / 4%) 85%)',
      },
    },
  },
  corePlugins: {
    borderOpacity: false,
    textOpacity: false,
  },
};

```

### `tsconfig.json`

```json
{
  "compilerOptions": {
    "baseUrl": "./",
    "outDir": "./build/",
    "target": "ESNext",
    "allowJs": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "ESNext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": false,
    "noEmit": true,
    "types": ["cypress", "node", "vite"],
    "paths": {
      "@scripts/*": ["./package/src/scripts/*"],
      "@src/*": ["./package/src/*"],
      "@package/*": ["./package/*"],
      "@/*": ["./*"],
      "vanilla-calendar-pro": ["./package/src/index.ts"],
      "vanilla-calendar-pro/types": ["package/src/types.ts"]
    }
  },
  "include": ["**/*.ts", "**/*.js", "**/*.mjs", "**/*.cy.ts"],
  "exclude": ["node_modules", "next/*"]
}

```

### `tsconfig.main.json`

```json
{
  "compilerOptions": {
    "baseUrl": "./",
    "target": "ESNext",
    "allowJs": true,
    "esModuleInterop": true,
    "declaration": true,
    "emitDeclarationOnly": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "ESNext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": false,
    "paths": {
      "@scripts/*": ["./package/src/scripts/*"],
      "@src/*": ["./package/src/*"],
      "@package/*": ["./package/*"],
      "@/*": ["./*"]
    }
  },
  "include": ["package/src/*.ts"],
  "exclude": ["node_modules"]
}

```

### `tsconfig.utils.json`

```json
{
  "compilerOptions": {
    "baseUrl": "./",
    "target": "ESNext",
    "allowJs": true,
    "esModuleInterop": true,
    "declaration": true,
    "emitDeclarationOnly": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "ESNext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": false,
    "paths": {
      "@scripts/*": ["./package/src/scripts/*"],
      "@src/*": ["./package/src/*"],
      "@package/*": ["./package/*"],
      "@/*": ["./*"]
    }
  },
  "include": ["package/src/utils/index.ts"],
  "exclude": ["node_modules"]
}

```

### `vite-env.d.ts`

```ts
/// <reference types="vite/client" />

```

### `vite.config.ts`

```ts
import fs from 'fs';
import path, { resolve } from 'path';
import { defineConfig } from 'vite';

const getInputVite: () => { [key: string]: string } = () => {
  const pages: string[] = [];

  function fromDir(startPath: string, filter: string): void {
    if (!fs.existsSync(startPath)) {
      console.log('no dir ', startPath);
      return;
    }

    const files: string[] = fs.readdirSync(startPath);
    for (let i = 0; i < files.length; i++) {
      const filename: string = path.join(startPath, files[i]);
      const stat: fs.Stats = fs.lstatSync(filename);
      if (stat.isDirectory()) {
        fromDir(filename, filter);
      } else if (filename.endsWith(filter)) {
        pages.push(filename);
      }
    }
  }

  fromDir('./demo/pages', '.html');

  return pages.reduce((acc: { [key: string]: string }, current: string, index: number) => {
    acc['0'] = resolve(__dirname, 'demo', 'index.html');
    acc[(index + 1).toString()] = resolve(__dirname, current);
    return acc;
  }, {});
};

export default defineConfig({
  root: './demo',
  build: {
    assetsDir: '',
    outDir: 'build',
    target: 'ES6',
    cssCodeSplit: true,
    minify: 'terser',
    rollupOptions: {
      input: getInputVite(),
    },
  },
  server: {
    port: 5173,
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './'),
      '@package': resolve(__dirname, './package'),
      '@src': resolve(__dirname, './package/src'),
      '@scripts': resolve(__dirname, './package/src/scripts'),
    },
  },
});

```
